// stripe-webhook: recebe os avisos da Stripe. Só aqui uma reserva paga passa a serviço na app.
// - checkout.session.completed / async_payment_succeeded (pago) → serviço novo na app + preço + pagamento recebido + email de confirmação
// - checkout.session.expired / async_payment_failed → fica registado, nada entra na app
// - charge.refunded → o serviço fica "cancelado" na app, com o valor reembolsado (os reembolsos fazem-se no painel da Stripe)
// Modo de teste → empresa demo (settings.site_test_bookings); modo real → empresa com settings.site_bookings (ou a primeira).
// Emails (Resend, a partir de reservas@): confirmação ao cliente + aviso à equipa (geral@) quando paga; cancelamento ao cliente + aviso à equipa no 1.º reembolso.
// Segredos: STRIPE_WEBHOOK_SECRET (whsec_...), RESEND_API_KEY (opcional; sem ela não sai email), EMAIL_FROM (opcional).
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

// Email de confirmação ao cliente. Estética do orçamento da Colorama (documento limpo: títulos serifados, etiquetas a negrito, destaque com barra à esquerda).
// Os clientes de email só mostram letras instaladas no aparelho: Georgia nos títulos, Helvetica/Arial no texto.
type Txt = { subj: string; title: string; booking: string; of: string; to: string; service: string; paid: string; vat: string; confirmed: string;
  hService: string; hDay: string; hCond: string; hContact: string; rows: string[]; bags: (a: number, b: number) => string; pax: (n: number) => string;
  svc: (p: Record<string, any>) => string; meet: string[]; wait: string; other: string; cond: string[]; wa: string; cal: string; locale: string; test: string };
const PAX = { pt: (n: number) => n === 1 ? "1 passageiro" : `${n} passageiros`, en: (n: number) => n === 1 ? "1 passenger" : `${n} passengers`, es: (n: number) => n === 1 ? "1 pasajero" : `${n} pasajeros`, fr: (n: number) => n === 1 ? "1 passager" : `${n} passagers` };
const svcName = (names: string[], dirs: string[]) => (p: Record<string, any>) => p.svc === 0 ? `${names[0]} · ${dirs[p.dir === 1 ? 1 : 0]}` : names[p.svc] || names[0];
const MAIL: Record<string, Txt> = {
  pt: { subj: "Reserva confirmada", title: "Reserva confirmada", booking: "Reserva", of: "de", to: "Para", service: "Serviço", paid: "Pagamento recebido", vat: "IVA incluído", confirmed: "A sua reserva está confirmada.",
    hService: "O seu serviço", hDay: "No dia", hCond: "Condições", hContact: "Contacto",
    rows: ["Data e hora", "Recolha", "Destino", "Voo", "Viatura", "Passageiros e malas", "O seu pedido", "Contacto"],
    bags: (a, b) => `${a} de porão · ${b} de mão`, pax: PAX.pt,
    svc: svcName(["Transfer aeroporto", "À disposição", "Tour privado", "Evento", "Longa distância", "Cruzeiro"], ["chegada", "partida"]),
    meet: ["Onde nos encontra", "o motorista espera nas chegadas com uma placa com o seu nome.", "Se o voo atrasar", "acompanhamos o voo e esperamos por si. A espera está incluída até 120 minutos depois da aterragem."],
    wait: "Espera incluída", other: "o motorista chega à hora marcada ao local de recolha. Estão incluídos 30 minutos de espera.",
    cond: ["Cancelamento", "sem penalização até 24 h antes (48 h em longa distância, eventos e serviços à disposição).", "Custos de processamento", "3 % do pagamento, não reembolsáveis em caso de cancelamento.", "Alterar ou cancelar", "responda a este email ou fale connosco por WhatsApp."],
    wa: "Falar connosco no WhatsApp", cal: "Adicionar ao calendário", locale: "pt-PT", test: "TESTE — modo de teste da Stripe, nenhum pagamento real" },
  en: { subj: "Booking confirmed", title: "Booking confirmed", booking: "Booking", of: "of", to: "For", service: "Service", paid: "Payment received", vat: "VAT included", confirmed: "Your booking is confirmed.",
    hService: "Your service", hDay: "On the day", hCond: "Terms", hContact: "Contact",
    rows: ["Date and time", "Pick-up", "Destination", "Flight", "Vehicle", "Passengers and luggage", "Your request", "Phone"],
    bags: (a, b) => `${a} checked · ${b} cabin`, pax: PAX.en,
    svc: svcName(["Airport transfer", "Chauffeur at disposal", "Private tour", "Event", "Long distance", "Cruise"], ["arrival", "departure"]),
    meet: ["Where to find us", "your driver waits in the arrivals hall with a sign bearing your name.", "If your flight is delayed", "we track your flight and wait for you. Waiting is included up to 120 minutes after landing."],
    wait: "Waiting included", other: "your driver arrives at the pick-up point at the agreed time. 30 minutes of waiting are included.",
    cond: ["Cancellation", "free of charge up to 24 h before (48 h for long distance, events and chauffeur at disposal).", "Processing costs", "3% of the payment, not refundable if you cancel.", "To change or cancel", "reply to this email or message us on WhatsApp."],
    wa: "Message us on WhatsApp", cal: "Add to calendar", locale: "en-GB", test: "TEST — Stripe test mode, no real payment" },
  es: { subj: "Reserva confirmada", title: "Reserva confirmada", booking: "Reserva", of: "del", to: "Para", service: "Servicio", paid: "Pago recibido", vat: "IVA incluido", confirmed: "Su reserva está confirmada.",
    hService: "Su servicio", hDay: "El día del servicio", hCond: "Condiciones", hContact: "Contacto",
    rows: ["Fecha y hora", "Recogida", "Destino", "Vuelo", "Vehículo", "Pasajeros y maletas", "Su petición", "Teléfono"],
    bags: (a, b) => `${a} facturadas · ${b} de mano`, pax: PAX.es,
    svc: svcName(["Traslado aeropuerto", "A disposición", "Tour privado", "Evento", "Larga distancia", "Crucero"], ["llegada", "salida"]),
    meet: ["Dónde encontrarnos", "el conductor le espera en llegadas con un cartel con su nombre.", "Si el vuelo se retrasa", "seguimos el vuelo y le esperamos. La espera está incluida hasta 120 minutos después del aterrizaje."],
    wait: "Espera incluida", other: "el conductor llega a la hora acordada al punto de recogida. Se incluyen 30 minutos de espera.",
    cond: ["Cancelación", "sin penalización hasta 24 h antes (48 h en larga distancia, eventos y servicios a disposición).", "Gastos de procesamiento", "3 % del pago, no reembolsables en caso de cancelación.", "Cambiar o cancelar", "responda a este email o escríbanos por WhatsApp."],
    wa: "Escríbanos por WhatsApp", cal: "Añadir al calendario", locale: "es-ES", test: "PRUEBA — modo de prueba de Stripe, ningún pago real" },
  fr: { subj: "Réservation confirmée", title: "Réservation confirmée", booking: "Réservation", of: "du", to: "Pour", service: "Service", paid: "Paiement reçu", vat: "TVA incluse", confirmed: "Votre réservation est confirmée.",
    hService: "Votre service", hDay: "Le jour J", hCond: "Conditions", hContact: "Contact",
    rows: ["Date et heure", "Prise en charge", "Destination", "Vol", "Véhicule", "Passagers et bagages", "Votre demande", "Téléphone"],
    bags: (a, b) => `${a} en soute · ${b} en cabine`, pax: PAX.fr,
    svc: svcName(["Transfert aéroport", "Chauffeur à disposition", "Tour privé", "Événement", "Longue distance", "Croisière"], ["arrivée", "départ"]),
    meet: ["Où nous trouver", "votre chauffeur vous attend aux arrivées avec une pancarte à votre nom.", "Si votre vol est retardé", "nous suivons votre vol et vous attendons. L'attente est incluse jusqu'à 120 minutes après l'atterrissage."],
    wait: "Attente incluse", other: "votre chauffeur arrive au point de prise en charge à l'heure convenue. 30 minutes d'attente sont incluses.",
    cond: ["Annulation", "sans pénalité jusqu'à 24 h avant (48 h pour la longue distance, les événements et les services à disposition).", "Frais de traitement", "3 % du paiement, non remboursables en cas d'annulation.", "Modifier ou annuler", "répondez à cet email ou écrivez-nous sur WhatsApp."],
    wa: "Écrivez-nous sur WhatsApp", cal: "Ajouter au calendrier", locale: "fr-FR", test: "TEST — mode test de Stripe, aucun paiement réel" },
};
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));
export const bookingRef = (id: string) => "DDL-" + String(id).replace(/-/g, "").slice(0, 6).toUpperCase();
const LOGO = "https://darkdiamondluxury.pt/assets/email-logo.png";
const SERIF = "Georgia,'Times New Roman',serif", SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif";
const li = (k: string, v: string) => `<li style="margin:0 0 4px"><b>${esc(k)}:</b> ${esc(v)}</li>`;
const ul = (items: string) => `<ul style="margin:0;padding:0 0 0 22px;font-family:${SANS};font-size:15px;line-height:1.6;color:#1a1a1a">${items}</ul>`;
const h2 = (t: string) => `<h2 style="margin:28px 0 10px;font-family:${SERIF};font-weight:normal;font-size:22px;line-height:1.3;color:#1a1a1a">${esc(t)}</h2>`;
const pl = (k: string, v: string) => `<p style="margin:4px 0 0;font-family:${SANS};font-size:15px;line-height:1.6;color:#1a1a1a"><b>${esc(k)}:</b> ${esc(v)}</p>`;
const note = (html: string) => `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:20px 0 0"><tr><td style="border-left:3px solid #d9d6d0;padding:6px 0 6px 18px;font-family:${SANS};font-size:15px;line-height:1.6;color:#1a1a1a">${html}</td></tr></table>`;
const waBtn = (t: string) => `<a href="https://wa.me/351932666254" style="display:inline-block;background:#1a1a1a;color:#ffffff;text-decoration:none;font-family:${SANS};font-size:14px;font-weight:bold;padding:11px 20px;border-radius:6px">${esc(t)}</a>`;
const SIGN = `<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:${SANS};color:#1a1a1a"><tr>
<td style="padding:0 16px 0 0;vertical-align:middle"><a href="https://darkdiamondluxury.pt" style="text-decoration:none"><img src="${LOGO}" width="72" height="72" alt="Dark Diamond Luxury" style="display:block;width:72px;height:72px;border:0"></a></td>
<td style="padding:0 0 0 16px;vertical-align:middle;border-left:2px solid #b08a3a">
<div style="font-size:16px;font-weight:bold;letter-spacing:0.5px">Dark Diamond Luxury</div>
<div style="font-size:13px;color:#8a6a24;padding:2px 0 8px">Luxury Transport &amp; Transfers · Lisboa</div>
<div style="font-size:13px;color:#333;line-height:1.6"><a href="tel:+351932666254" style="color:#333;text-decoration:none">+351 932 666 254</a> · <a href="mailto:geral@darkdiamondluxury.pt" style="color:#333;text-decoration:none">geral@darkdiamondluxury.pt</a><br>
<a href="https://wa.me/351932666254" style="color:#333;text-decoration:none">WhatsApp 24/7</a> · <a href="https://darkdiamondluxury.pt" style="color:#8a6a24;text-decoration:none;font-weight:bold">darkdiamondluxury.pt</a></div>
</td></tr></table>`;
const shell = (inner: string, testLine = "") => `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"></head>
<body style="margin:0;padding:0;background:#ffffff">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff"><tr><td align="center" style="padding:0">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%"><tr><td style="padding:32px 24px 40px;color:#1a1a1a">
${testLine ? `<p style="margin:0 0 16px;font-family:${SANS};font-size:13px;color:#b00020">${testLine}</p>` : ""}
${inner}
</td></tr></table></td></tr></table></body></html>`;

export function mailHtml(p: Record<string, any>, cents: number, test: boolean, ref: string): { subject: string; html: string } {
  const m = MAIL[p.lang] || MAIL.en;
  const [y, mo, d] = String(p.date).split("-").map(Number);
  const day = (dt: Date) => dt.toLocaleDateString(m.locale, { weekday: "long", day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
  const today = new Date().toLocaleDateString(m.locale, { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Lisbon" });
  const when = `${day(new Date(Date.UTC(y, mo - 1, d)))} · ${p.time}`;
  const arrival = p.svc === 0 && p.dir !== 1;
  const phone = [p.cc, p.phone].filter(Boolean).join(" ");
  const vals = [when, p.pickup || "", p.svc === 2 ? p.label : (p.dropoff || p.label || p.to || ""), p.flight || "", p.carName ? `Mercedes ${p.carName}` : "",
    `${m.pax(Number(p.pax) || 1)} · ${m.bags(Number(p.bags) || 0, Number(p.cabin) || 0)}`, p.notes || "", phone];
  const service = m.svc(p);
  const pad = (n: number) => String(n).padStart(2, "0");
  const [hh, mm] = String(p.time).split(":").map(Number);
  const end = new Date(Date.UTC(y, mo - 1, d, hh + 1, mm));
  const cal = "https://calendar.google.com/calendar/render?" + new URLSearchParams({ action: "TEMPLATE", text: `Dark Diamond Luxury · ${service}`,
    dates: `${y}${pad(mo)}${pad(d)}T${pad(hh)}${pad(mm)}00/${end.getUTCFullYear()}${pad(end.getUTCMonth() + 1)}${pad(end.getUTCDate())}T${pad(end.getUTCHours())}${pad(end.getUTCMinutes())}00`,
    ctz: "Europe/Lisbon", details: `${m.booking} ${ref} · WhatsApp +351 932 666 254`, location: p.pickup || "" }).toString();
  const inner = `<h1 style="margin:0;font-family:${SERIF};font-weight:normal;font-size:32px;line-height:1.2;color:#1a1a1a">${m.title}</h1>
<p style="margin:12px 0 0;font-family:${SANS};font-size:15px;line-height:1.6;color:#1a1a1a"><b>Dark Diamond Luxury</b> · ${m.booking} ${ref} ${m.of} ${esc(today)}</p>
${p.name ? pl(m.to, String(p.name)) : ""}${pl(m.service, service)}
${note(`<b>${m.paid}:</b> ${eurTxt(cents)} (${m.vat}). ${m.confirmed}`)}
${h2(m.hService)}${ul(m.rows.map((r, i) => vals[i] ? li(r, vals[i]) : "").join(""))}
${h2(m.hDay)}${ul(arrival ? li(m.meet[0], m.meet[1]) + li(m.meet[2], m.meet[3]) : li(m.wait, m.other))}
<p style="margin:18px 0 0;font-family:${SANS}">${waBtn(m.wa)}&nbsp;&nbsp;<a href="${esc(cal)}" style="display:inline-block;color:#1a1a1a;text-decoration:underline;font-size:14px;padding:11px 4px">${m.cal}</a></p>
${h2(m.hCond)}${ul(li(m.cond[0], m.cond[1]) + li(m.cond[2], m.cond[3]) + li(m.cond[4], m.cond[5]))}
${h2(m.hContact)}${SIGN}`;
  const html = shell(inner, test ? m.test : "");
  return { subject: `${test ? "[TESTE] " : ""}${m.subj} ${ref} · Dark Diamond Luxury`, html };
}

// Email de cancelamento ao cliente (sai quando o pagamento é reembolsado na Stripe).
const CANCEL: Record<string, { subj: string; title: string; lead: (r: string) => string; rows: string[]; kept: string; bye: string }> = {
  pt: { subj: "Reserva cancelada", title: "Reserva cancelada", lead: (r) => `<b>Reembolso:</b> ${r} para o cartão usado no pagamento. Pode demorar 5 a 10 dias úteis a aparecer na sua conta.`,
    rows: ["Data e hora", "Pago", "Reembolsado", "Retido"], kept: "O valor retido corresponde aos custos de processamento do pagamento (3 %) e, quando se aplica, à penalização de cancelamento prevista nas condições.", bye: "Esperamos voltar a recebê-lo em breve. Se precisar de alguma coisa, estamos no WhatsApp." },
  en: { subj: "Booking cancelled", title: "Booking cancelled", lead: (r) => `<b>Refund:</b> ${r} to the card used for payment. It may take 5 to 10 business days to appear in your account.`,
    rows: ["Date and time", "Paid", "Refunded", "Retained"], kept: "The retained amount covers payment processing costs (3%) and, where applicable, the cancellation penalty set out in our terms.", bye: "We hope to welcome you again soon. If you need anything, we are on WhatsApp." },
  es: { subj: "Reserva cancelada", title: "Reserva cancelada", lead: (r) => `<b>Reembolso:</b> ${r} a la tarjeta usada en el pago. Puede tardar de 5 a 10 días hábiles en aparecer en su cuenta.`,
    rows: ["Fecha y hora", "Pagado", "Reembolsado", "Retenido"], kept: "El importe retenido corresponde a los gastos de procesamiento del pago (3 %) y, cuando procede, a la penalización de cancelación prevista en las condiciones.", bye: "Esperamos volver a recibirle pronto. Si necesita algo, estamos en WhatsApp." },
  fr: { subj: "Réservation annulée", title: "Réservation annulée", lead: (r) => `<b>Remboursement :</b> ${r} sur la carte utilisée pour le paiement. Le montant peut mettre 5 à 10 jours ouvrés à apparaître sur votre compte.`,
    rows: ["Date et heure", "Payé", "Remboursé", "Retenu"], kept: "Le montant retenu correspond aux frais de traitement du paiement (3 %) et, le cas échéant, à la pénalité d'annulation prévue dans nos conditions.", bye: "Nous espérons vous accueillir de nouveau bientôt. Pour toute question, nous sommes sur WhatsApp." },
};

export function cancelHtml(p: Record<string, any>, paidC: number, refC: number, test: boolean, ref: string): { subject: string; html: string } {
  const m = MAIL[p.lang] || MAIL.en, c = CANCEL[p.lang] || CANCEL.en;
  const [y, mo, d] = String(p.date).split("-").map(Number);
  const when = `${new Date(Date.UTC(y, mo - 1, d)).toLocaleDateString(m.locale, { weekday: "long", day: "numeric", month: "long", year: "numeric", timeZone: "UTC" })} · ${p.time}`;
  const kept = Math.max(0, paidC - refC);
  const inner = `<h1 style="margin:0;font-family:${SERIF};font-weight:normal;font-size:32px;line-height:1.2;color:#1a1a1a">${c.title}</h1>
<p style="margin:12px 0 0;font-family:${SANS};font-size:15px;line-height:1.6;color:#1a1a1a"><b>Dark Diamond Luxury</b> · ${m.booking} ${ref}</p>
${p.name ? pl(m.to, String(p.name)) : ""}${pl(m.service, m.svc(p))}
${note(c.lead(eurTxt(refC)))}
${h2(m.hService)}${ul(li(c.rows[0], when) + li(c.rows[1], eurTxt(paidC)) + li(c.rows[2], eurTxt(refC)) + (kept ? li(c.rows[3], eurTxt(kept)) : ""))}
${kept ? `<p style="margin:12px 0 0;font-family:${SANS};font-size:14px;line-height:1.6;color:#555">${c.kept}</p>` : ""}
<p style="margin:20px 0 0;font-family:${SANS};font-size:15px;line-height:1.6;color:#1a1a1a">${c.bye}</p>
<p style="margin:16px 0 0">${waBtn(m.wa)}</p>
${h2(m.hContact)}${SIGN}`;
  return { subject: `${test ? "[TESTE] " : ""}${c.subj} ${ref} · Dark Diamond Luxury`, html: shell(inner, test ? m.test : "") };
}

// Aviso curto à equipa (geral@, que reencaminha para o Gmail da empresa), em cada reserva paga e em cada reembolso.
export function teamHtml(kind: "nova" | "cancelada", p: Record<string, any>, ref: string, paidC: number, refC: number, test: boolean): { subject: string; html: string } {
  const [y, mo, d] = String(p.date).split("-");
  const when = `${d}/${mo}/${y} ${p.time}`;
  const svc = MAIL.pt.svc(p);
  const head = kind === "nova" ? `Nova reserva paga no site · ${ref}` : `Reserva cancelada e reembolsada · ${ref}`;
  const rows = [["Serviço", svc], ["Data e hora", when], ["Recolha", p.pickup], ["Destino", p.svc === 2 ? p.label : (p.dropoff || p.label)], ["Voo", p.flight],
    ["Viatura", p.carName], ["Passageiros", `${p.pax} · malas ${p.bags || 0} + ${p.cabin || 0}`], ["Cliente", p.name], ["Telefone", p.phone], ["Email", p.email],
    ["Pedido do cliente", p.notes], ["Extras", (p.extras || []).join(", ")], ["Língua", String(p.lang || "").toUpperCase()], ["Pago", eurTxt(paidC)],
    ...(kind === "cancelada" ? [["Reembolsado", eurTxt(refC)], ["Fica com a empresa", eurTxt(Math.max(0, paidC - refC))]] : [])].filter((r) => r[1]);
  const inner = `<h1 style="margin:0;font-family:${SERIF};font-weight:normal;font-size:26px;line-height:1.2;color:#1a1a1a">${esc(head)}</h1>
${note(kind === "nova" ? "O serviço já está na app, com o pagamento registado. Falta atribuir motorista." : "O serviço já passou a cancelado na app. O cliente recebeu o email de cancelamento.")}
${h2("Detalhes")}${ul(rows.map(([k, v]) => li(String(k), String(v))).join(""))}`;
  return { subject: `${test ? "[TESTE] " : ""}${kind === "nova" ? "Nova reserva" : "Cancelada"} ${ref} · ${when} · ${p.carName} · ${eurTxt(kind === "nova" ? paidC : refC)}`, html: shell(inner, test ? "TESTE — modo de teste da Stripe" : "") };
}

const TEAM = "geral@darkdiamondluxury.pt";
async function send(to: string, mail: { subject: string; html: string }, replyTo = "geral@darkdiamondluxury.pt"): Promise<string | null> {
  const key = Deno.env.get("RESEND_API_KEY");
  if (!key) return "sem RESEND_API_KEY";
  const r = await fetch("https://api.resend.com/emails", { method: "POST", headers: { authorization: `Bearer ${key}`, "content-type": "application/json" }, body: JSON.stringify({
    from: (Deno.env.get("EMAIL_FROM") || "").includes("@darkdiamondluxury.pt") ? Deno.env.get("EMAIL_FROM") : "Dark Diamond Luxury <reservas@darkdiamondluxury.pt>", to: [to],
    reply_to: replyTo, subject: mail.subject, html: mail.html }) });
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
    internal_notes: `${live ? "" : "TESTE · "}${bookingRef(row.id)} · Pago online pela Stripe: ${eurTxt(cents)} · ${session.payment_intent || session.id}`,
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
  const ref = bookingRef(row.id);
  const err = to ? await send(to, mailHtml(p, cents, !live, ref)) : "sem email do cliente";
  const tErr = await send(TEAM, teamHtml("nova", p, ref, cents, 0, !live), to || TEAM);
  if (tErr) console.error("aviso equipa", tErr);
  await db(`site_checkouts?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify(err ? { email_error: err } : { email_sent_at: new Date().toISOString(), email_error: null }) });
}

async function refunded(charge: Record<string, any>) {
  const pi = charge.payment_intent; if (!pi) return;
  const rows = await (await db(`site_checkouts?select=*&payment_intent=eq.${pi}`)).json();
  const row = rows[0]; if (!row) return;
  const ref = charge.amount_refunded || 0, full = ref >= (charge.amount || row.amount_cents);
  const first = row.status === "pago"; // os emails só saem no primeiro reembolso (a Stripe repete o aviso em cada reembolso parcial)
  await db(`site_checkouts?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify({ refunded_cents: ref, status: full ? "reembolsado" : "reembolso_parcial" }) });
  if (first) {
    const p = row.payload, paidC = charge.amount || row.amount_cents, live = !!charge.livemode, bref = bookingRef(row.id), to = p.email || charge.billing_details?.email;
    const e1 = to ? await send(to, cancelHtml(p, paidC, ref, !live, bref)) : "sem email do cliente";
    if (e1) console.error("email cancelamento", e1);
    const e2 = await send(TEAM, teamHtml("cancelada", p, bref, paidC, ref, !live), to || TEAM);
    if (e2) console.error("aviso equipa", e2);
  }
  if (!row.service_id) return;
  const why = `Reembolso na Stripe: ${eurTxt(ref)} de ${eurTxt(charge.amount || row.amount_cents)}`;
  await db(`services?id=eq.${row.service_id}&status=neq.cancelado`, { method: "PATCH", body: JSON.stringify({ status: "cancelado", cancel_reason: why }) });
  await db("service_events", { method: "POST", body: JSON.stringify({ company_id: row.company_id, service_id: row.service_id, kind: "cancelado", note: why, money: true }) });
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
