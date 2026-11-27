// stripe-webhook: recebe os avisos da Stripe. Só aqui uma reserva paga passa a serviço na app.
// - checkout.session.completed / async_payment_succeeded (pago) → serviço novo na app + preço + pagamento recebido + email de confirmação
// - checkout.session.expired / async_payment_failed → fica registado, nada entra na app
// - charge.refunded → o serviço fica "cancelado" na app, com o valor reembolsado (os reembolsos fazem-se no painel da Stripe)
// Modo de teste → empresa demo (settings.site_test_bookings); modo real → empresa com settings.site_bookings (ou a primeira).
// Segredos: STRIPE_WEBHOOK_SECRET (whsec_...), RESEND_API_KEY (opcional; sem ela não sai email), EMAIL_FROM (opcional), EMAIL_COPY (opcional).
const SB = Deno.env.get("SUPABASE_URL")!, SR = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const db = (path: string, init: RequestInit = {}) => fetch(`${SB}/rest/v1/${path}`, { ...init, headers: { apikey: SR, authorization: `Bearer ${SR}`, "content-type": "application/json", prefer: "return=representation", ...(init.headers || {}) } });
const ok = (msg = "ok") => new Response(msg, { status: 200 });

async function verify(raw: string, header: string, secret: string): Promise<boolean> {
  const parts = Object.fromEntries(header.split(",").map((p) => p.split("=", 2)).filter((p) => p.length === 2).map(([k, v]) => [k, v]));
  const sigs = header.split(",").filter((p) => p.startsWith("v1=")).map((p) => p.slice(3));
  const t = Number(parts.t);
  if (!t || !sigs.length || Math.abs(Date.now() / 1000 - t) > 300) return false;
  const k = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const mac = new Uint8Array(await crypto.subtle.sign("HMAC", k, new TextEncoder().encode(`${t}.${raw}`)));
  const hex = [...mac].map((b) => b.toString(16).padStart(2, "0")).join("");
  return sigs.some((s) => s.length === hex.length && [...s].reduce((a, c, i) => a | (c.charCodeAt(0) ^ hex.charCodeAt(i)), 0) === 0);
}

const VEH: Record<string, string | null> = { E: "Sedan Executive", S: "Sedan Executive", V: "Van VIP", T: "Van", P: null, M: null };
const SEAT = ["Cadeira de criança", "Child seat", "Silla infantil", "Siège enfant"], BOOST = ["Assento elevatório", "Booster seat", "Elevador", "Rehausseur"];
const eurTxt = (c: number) => (c / 100).toFixed(2).replace(".", ",") + " €";

function serviceType(p: Record<string, any>) {
  if (p.svc === 2) return "Tour";
  if (p.svc === 4) return "Longa distância";
  if (p.svc === 0) return p.dir === 0 ? "Chegada aeroporto" : p.dir === 1 ? "Partida aeroporto" : "Transfer";
  return "Transfer";
}

const MAIL: Record<string, { subj: string; hi: string; body: string; rows: string[]; cancel: string; contact: string }> = {
  pt: { subj: "Reserva confirmada", hi: "Olá", body: "O pagamento foi recebido e a sua reserva está confirmada.", rows: ["Serviço", "Data e hora", "Recolha", "Destino", "Viatura", "Passageiros", "Voo", "Pago"], cancel: "Cancelamento sem penalização até 24 h antes (48 h em longa distância, eventos e serviços à disposição). Custos de processamento do pagamento (3 %) não reembolsáveis em caso de cancelamento.", contact: "Para alterar ou cancelar, responda a este email ou fale connosco por WhatsApp: +351 932 666 254." },
  en: { subj: "Booking confirmed", hi: "Hello", body: "Your payment has been received and your booking is confirmed.", rows: ["Service", "Date and time", "Pick-up", "Destination", "Vehicle", "Passengers", "Flight", "Paid"], cancel: "Cancellation without penalty up to 24 h before (48 h for long distance, events and chauffeur at disposal). Payment processing costs (3%) are not refundable if you cancel.", contact: "To change or cancel, reply to this email or message us on WhatsApp: +351 932 666 254." },
  es: { subj: "Reserva confirmada", hi: "Hola", body: "Hemos recibido el pago y su reserva está confirmada.", rows: ["Servicio", "Fecha y hora", "Recogida", "Destino", "Vehículo", "Pasajeros", "Vuelo", "Pagado"], cancel: "Cancelación sin penalización hasta 24 h antes (48 h en larga distancia, eventos y servicios a disposición). Gastos de procesamiento del pago (3 %) no reembolsables en caso de cancelación.", contact: "Para cambiar o cancelar, responda a este email o escríbanos por WhatsApp: +351 932 666 254." },
  fr: { subj: "Réservation confirmée", hi: "Bonjour", body: "Votre paiement a bien été reçu et votre réservation est confirmée.", rows: ["Service", "Date et heure", "Prise en charge", "Destination", "Véhicule", "Passagers", "Vol", "Payé"], cancel: "Annulation sans pénalité jusqu'à 24 h avant (48 h pour la longue distance, les événements et les services à disposition). Frais de traitement du paiement (3 %) non remboursables en cas d'annulation.", contact: "Pour modifier ou annuler, répondez à cet email ou écrivez-nous sur WhatsApp : +351 932 666 254." },
};
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));

async function sendMail(to: string, p: Record<string, any>, cents: number, test: boolean): Promise<string | null> {
  const key = Deno.env.get("RESEND_API_KEY");
  if (!key) return "sem RESEND_API_KEY";
  const m = MAIL[p.lang] || MAIL.en;
  const [y, mo, d] = String(p.date).split("-");
  const vals = [p.label, `${d}/${mo}/${y} ${p.time}`, p.pickup || "—", p.dropoff || p.to || "—", p.carName, String(p.pax), p.flight || "", eurTxt(cents)];
  const rows = m.rows.map((r, i) => vals[i] ? `<tr><td style="padding:6px 14px 6px 0;color:#777">${r}</td><td style="padding:6px 0">${esc(vals[i])}</td></tr>` : "").join("");
  const html = `<div style="font-family:Georgia,serif;max-width:560px;color:#111">${test ? '<p style="color:#b00">[TESTE — modo de teste da Stripe, nenhum pagamento real]</p>' : ""}<h2 style="font-weight:400">Dark Diamond Luxury</h2><p>${m.hi}${p.name ? " " + esc(String(p.name).split(" ")[0]) : ""},</p><p>${m.body}</p><table style="border-collapse:collapse;font-size:15px">${rows}</table><p style="font-size:13px;color:#555;margin-top:18px">${m.cancel}</p><p>${m.contact}</p></div>`;
  const copy = Deno.env.get("EMAIL_COPY");
  const r = await fetch("https://api.resend.com/emails", { method: "POST", headers: { authorization: `Bearer ${key}`, "content-type": "application/json" }, body: JSON.stringify({
    from: (Deno.env.get("EMAIL_FROM") || "").includes("@darkdiamondluxury.pt") ? Deno.env.get("EMAIL_FROM") : "Dark Diamond Luxury <reservas@darkdiamondluxury.pt>", to: [to], ...(copy ? { bcc: [copy] } : {}),
    reply_to: "geral@darkdiamondluxury.pt", subject: `${test ? "[TESTE] " : ""}${m.subj} · Dark Diamond Luxury`, html }) });
  return r.ok ? null : `resend ${r.status}: ${(await r.text()).slice(0, 300)}`;
}

async function companyFor(live: boolean): Promise<string | null> {
  const q = live ? "companies?select=id&settings->>site_bookings=eq.true&order=created_at&limit=1" : "companies?select=id&settings->>site_test_bookings=eq.true&limit=1";
  let rows = await (await db(q)).json();
  if (live && !rows.length) rows = await (await db("companies?select=id&order=created_at&limit=1")).json();
  return rows[0]?.id || null;
}

async function paid(session: Record<string, any>) {
  const rows = await (await db(`site_checkouts?select=*&stripe_session_id=eq.${session.id}`)).json();
  const row = rows[0];
  if (!row) { console.error("sessão desconhecida", session.id); return; }
  if (row.status === "pago" && row.service_id) return; // já tratado (a Stripe pode repetir avisos)
  const p = row.payload, cents = session.amount_total ?? row.amount_cents, live = !!session.livemode;
  const co = await companyFor(live);
  if (!co) { console.error("sem empresa para", live ? "real" : "teste"); return; }
  const cd = session.customer_details || {};
  const email = p.email || cd.email || null, phone = p.phone || cd.phone || null;
  const extras: string[] = p.extras || [];
  const req = [`Viatura pedida: ${p.carName}`, ...extras].join(" · ");
  const svc = {
    company_id: co, date: p.date, time: p.time, service_type: serviceType(p), vehicle_type: VEH[p.car] ?? null,
    pickup: p.pickup || null, dropoff: p.dropoff || p.to || null, flight: p.flight || null,
    client_name: p.name || cd.name || null, client_phone: phone, client_email: email, pax: p.pax, checked_bags: p.bags, cabin_bags: p.cabin,
    notes: [p.svc === 2 ? `Tour: ${p.label}` : "", p.svc === 5 ? "Cruzeiro" : "", p.notes].filter(Boolean).join(" · ") || null,
    requirements: req.slice(0, 1000), channel: "Site", source: "site", origin: "direct",
    internal_notes: `${live ? "" : "TESTE · "}Pago online pela Stripe: ${eurTxt(cents)} · ${session.payment_intent || session.id}`,
    seat_child: extras.some((x) => SEAT.includes(x)) ? 1 : 0, seat_booster: extras.some((x) => BOOST.includes(x)) ? 1 : 0,
  };
  const ins = await db("services", { method: "POST", body: JSON.stringify(svc) });
  if (!ins.ok) { console.error("serviço", await ins.text()); throw new Error("serviço"); }
  const sid = (await ins.json())[0].id;
  await db("service_money", { method: "POST", headers: { prefer: "resolution=merge-duplicates,return=minimal" }, body: JSON.stringify({ service_id: sid, company_id: co, price: cents / 100, price_vat_mode: "com", vat_rate: 6 }) });
  await db("payments", { method: "POST", body: JSON.stringify({ company_id: co, service_id: sid, direction: "in", date: new Date().toISOString().slice(0, 10), amount: cents / 100, method: "Stripe", reference: session.payment_intent || session.id }) });
  await db("service_events", { method: "POST", body: JSON.stringify({ company_id: co, service_id: sid, kind: "criado", note: `Reserva paga no site (${eurTxt(cents)})`, money: true }) });
  await db(`site_checkouts?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify({ status: "pago", paid_at: new Date().toISOString(), service_id: sid, company_id: co, payment_intent: session.payment_intent || null, livemode: live }) });
  const to = email;
  const err = to ? await sendMail(to, p, cents, !live) : "sem email do cliente";
  await db(`site_checkouts?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify(err ? { email_error: err } : { email_sent_at: new Date().toISOString(), email_error: null }) });
}

async function refunded(charge: Record<string, any>) {
  const pi = charge.payment_intent; if (!pi) return;
  const rows = await (await db(`site_checkouts?select=*&payment_intent=eq.${pi}`)).json();
  const row = rows[0]; if (!row) return;
  const ref = charge.amount_refunded || 0, full = ref >= (charge.amount || row.amount_cents);
  await db(`site_checkouts?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify({ refunded_cents: ref, status: full ? "reembolsado" : "reembolso_parcial" }) });
  if (!row.service_id) return;
  const note = `Reembolso na Stripe: ${eurTxt(ref)} de ${eurTxt(charge.amount || row.amount_cents)}`;
  await db(`services?id=eq.${row.service_id}&status=neq.cancelado`, { method: "PATCH", body: JSON.stringify({ status: "cancelado", cancel_reason: note }) });
  await db("service_events", { method: "POST", body: JSON.stringify({ company_id: row.company_id, service_id: row.service_id, kind: "cancelado", note, money: true }) });
  // o que fica com a empresa (penalização + 3 % de processamento) passa a taxa de cancelamento do serviço
  await db(`service_money?service_id=eq.${row.service_id}`, { method: "PATCH", body: JSON.stringify({ cancel_fee: Math.max(0, (charge.amount || row.amount_cents) - ref) / 100 }) });
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("método", { status: 405 });
  const raw = await req.text();
  const secret = Deno.env.get("STRIPE_WEBHOOK_SECRET") || "";
  if (!secret || !(await verify(raw, req.headers.get("stripe-signature") || "", secret))) return new Response("assinatura inválida", { status: 400 });
  const ev = JSON.parse(raw), o = ev.data?.object || {};
  try {
    switch (ev.type) {
      case "checkout.session.completed":
        if (o.payment_status === "paid") await paid(o);
        break;
      case "checkout.session.async_payment_succeeded":
        await paid(o); break;
      case "checkout.session.async_payment_failed":
        await db(`site_checkouts?stripe_session_id=eq.${o.id}&status=eq.aberto`, { method: "PATCH", body: JSON.stringify({ status: "falhou" }) }); break;
      case "checkout.session.expired":
        await db(`site_checkouts?stripe_session_id=eq.${o.id}&status=eq.aberto`, { method: "PATCH", body: JSON.stringify({ status: "expirado" }) }); break;
      case "charge.refunded":
        await refunded(o); break;
    }
  } catch (e) {
    console.error(ev.type, String(e));
    return new Response("erro", { status: 500 }); // a Stripe volta a tentar
  }
  return ok();
});
