// pagar-reserva: cria a sessão de pagamento da Stripe (Checkout) para uma reserva do site.
// O preço é sempre calculado aqui, a partir da tabela (prices.json, gerado de _build/prices.py): nunca se confia no valor do browser.
// Nada entra na app nesta fase: a reserva só passa a serviço quando a Stripe confirma o pagamento (função stripe-webhook).
// Também responde a GET ?estado=<id da sessão> para a página de regresso saber se o pagamento já foi confirmado.
// Segredos: STRIPE_SECRET_KEY (chave secreta de TESTE, sk_test_...). SUPABASE_URL e SUPABASE_SERVICE_ROLE_KEY vêm do Supabase.
import Pj from "./prices.json" with { type: "json" };
// deno-lint-ignore no-explicit-any
const P = Pj as any;

const SITE = "https://darkdiamondluxury.github.io";
const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "content-type, apikey, authorization", "Access-Control-Allow-Methods": "POST, GET, OPTIONS" };
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...CORS, "content-type": "application/json" } });
const SB = Deno.env.get("SUPABASE_URL")!, SR = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const db = (path: string, init: RequestInit = {}) => fetch(`${SB}/rest/v1/${path}`, { ...init, headers: { apikey: SR, authorization: `Bearer ${SR}`, "content-type": "application/json", prefer: "return=representation", ...(init.headers || {}) } });

const CARS = ["E", "V", "T", "S", "P", "M"];
const TXT: Record<string, { err: string; full: string; past: string; quote: string; soon: string; svc: string[]; pax: (n: number) => string }> = {
  pt: { err: "Não foi possível iniciar o pagamento. Tente de novo ou fale connosco por WhatsApp.", full: "Demasiados pedidos seguidos. Tente daqui a pouco.", past: "A data e a hora já passaram.", quote: "Este serviço tem preço sob orçamento.", soon: "Para reservas com menos de 24 h (48 h em Sprinter e minibus), fale connosco por WhatsApp: +351 932 666 254.", svc: ["Transfer aeroporto", "À disposição", "Tour", "Evento", "Longa distância", "Cruzeiro"], pax: (n) => n === 1 ? "1 passageiro" : `${n} passageiros` },
  en: { err: "We could not start the payment. Please try again or message us on WhatsApp.", full: "Too many requests in a row. Please try again shortly.", past: "That date and time have already passed.", quote: "This service is priced on request.", soon: "For bookings less than 24 h ahead (48 h for Sprinter and minibus), please message us on WhatsApp: +351 932 666 254.", svc: ["Airport transfer", "At your disposal", "Tour", "Event", "Long distance", "Cruise"], pax: (n) => n === 1 ? "1 passenger" : `${n} passengers` },
  es: { err: "No se pudo iniciar el pago. Inténtelo de nuevo o escríbanos por WhatsApp.", full: "Demasiadas solicitudes seguidas. Inténtelo dentro de un momento.", past: "La fecha y la hora ya han pasado.", quote: "Este servicio tiene precio bajo presupuesto.", soon: "Para reservas con menos de 24 h de antelación (48 h en Sprinter y minibús), escríbanos por WhatsApp: +351 932 666 254.", svc: ["Traslado aeropuerto", "A disposición", "Tour", "Evento", "Larga distancia", "Crucero"], pax: (n) => n === 1 ? "1 pasajero" : `${n} pasajeros` },
  fr: { err: "Impossible de lancer le paiement. Réessayez ou écrivez-nous sur WhatsApp.", full: "Trop de demandes à la suite. Réessayez dans un instant.", past: "La date et l'heure sont déjà passées.", quote: "Ce service est sur devis.", soon: "Pour les réservations à moins de 24 h (48 h en Sprinter et minibus), écrivez-nous sur WhatsApp : +351 932 666 254.", svc: ["Transfert aéroport", "À disposition", "Tour", "Événement", "Longue distance", "Croisière"], pax: (n) => n === 1 ? "1 passager" : `${n} passagers` },
};

// O mesmo cálculo do formulário do site (home.html → spPrice), feito no servidor.
function price(svc: number, to: string, car: string, hour: number, min: number): { eur: number; label: string } | null {
  const k = to.trim().toLowerCase(), i = CARS.indexOf(car);
  if (i < 0 || !k) return null;
  const tr = svc === 0 || svc === 4 || svc === 5;
  let p: number[] | null = null, tour = svc === 2, label = to.trim();
  if (tour) { p = P.tour[k] || (P.aliasTour[k] || [])[1] || null; if (!P.tour[k] && P.aliasTour[k]) label = P.aliasTour[k][0]; }
  else if (tr) { p = P.tr[k] || null; if (!p && P.aliasTour[k]) { p = P.aliasTour[k][1]; label = P.aliasTour[k][0]; tour = true; } }
  let v = p && p[i]; if (!v) return null;
  if (tour && (hour >= 20 || hour < 7 || (hour === 7 && min < 30)) && !P.night.includes(k)) v += P.nightEur;
  return { eur: v, label };
}

// Hora de Lisboa → instante real (trata a hora de verão)
function lisbonEpoch(date: string, hour: number, min: number): number {
  const [y, m, d] = date.split("-").map(Number);
  const guess = Date.UTC(y, m - 1, d, hour, min);
  const parts = Object.fromEntries(new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Lisbon", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).formatToParts(new Date(guess)).map((x) => [x.type, x.value]));
  const asUtc = Date.UTC(+parts.year, +parts.month - 1, +parts.day, +parts.hour, +parts.minute);
  return guess - (asUtc - guess);
}
// Antecedência mínima para pagar online: 24 h; 48 h em Sprinter e minibus (decisão de 25/11/2026)
const LEAD_H: Record<string, number> = { P: 48, M: 48 };

async function sha(s: string) { const h = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s)); return [...new Uint8Array(h)].map((b) => b.toString(16).padStart(2, "0")).join("").slice(0, 32); }

async function stripe(path: string, form: URLSearchParams | null, method = "POST") {
  const r = await fetch(`https://api.stripe.com/v1/${path}`, { method, headers: { authorization: `Bearer ${Deno.env.get("STRIPE_SECRET_KEY")}`, "content-type": "application/x-www-form-urlencoded", "Stripe-Version": "2025-10-29.clover" }, body: form ? form.toString() : undefined });
  return { ok: r.ok, body: await r.json() };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const key = Deno.env.get("STRIPE_SECRET_KEY") || "";
  // Proteção: só chaves de teste até a conta ser ativada (decisão de 25/11/2026).
  if (!key.startsWith("sk_test_") && Deno.env.get("STRIPE_LIVE_ALLOWED") !== "sim") return json({ error: "Pagamentos indisponíveis." }, 503);

  if (req.method === "GET") {
    const id = new URL(req.url).searchParams.get("estado") || "";
    if (!/^cs_[A-Za-z0-9_]{10,200}$/.test(id)) return json({ status: "desconhecido" });
    const r = await db(`site_checkouts?select=status&stripe_session_id=eq.${id}`);
    const rows = await r.json();
    return json({ status: rows[0]?.status || "desconhecido" });
  }
  if (req.method !== "POST") return json({ error: "método" }, 405);

  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return json({ error: "pedido" }, 400); }
  const lang = ["pt", "en", "es", "fr"].includes(String(b.lang)) ? String(b.lang) : "en";
  const t = TXT[lang];
  if (String(b.website || "") !== "") return json({ error: t.err }, 400); // campo-armadilha preenchido: robô

  const s = (k: string, n: number) => String(b[k] ?? "").trim().slice(0, n);
  const svc = Number(b.svc), car = s("car", 2), to = s("to", 200), date = s("date", 10);
  const hour = Number(b.hour), min = Number(b.min), pax = Number(b.pax), bags = Number(b.bags) || 0, cabin = Number(b.cabin) || 0;
  if (![0, 2, 4, 5].includes(svc) || !/^\d{4}-\d{2}-\d{2}$/.test(date) || !(hour >= 0 && hour < 24) || !(min >= 0 && min < 60) || !(pax >= 1 && pax <= P.cap[CARS.indexOf(car)])) return json({ error: t.quote }, 400);
  const when = lisbonEpoch(date, hour, min);
  if (isNaN(when) || when < Date.now()) return json({ error: t.past }, 400);
  if (when - Date.now() < (LEAD_H[car] || 24) * 3600e3) return json({ error: t.soon, soon: true }, 400);
  const pr = price(svc, to, car, hour, min);
  if (!pr) return json({ error: t.quote }, 400);

  // limite de pedidos: 10 por hora por endereço
  const ip = await sha((req.headers.get("x-forwarded-for") || "").split(",")[0] + "|ddl");
  const since = new Date(Date.now() - 3600e3).toISOString();
  const cnt = await (await db(`site_checkouts?select=id&ip_hash=eq.${ip}&created_at=gt.${since}`)).json();
  if (Array.isArray(cnt) && cnt.length >= 10) return json({ error: t.full }, 429);

  const extras = Array.isArray(b.extras) ? (b.extras as unknown[]).map((x) => String(x).slice(0, 60)).slice(0, 12) : [];
  const payload = {
    lang, svc, dir: Number(b.dir) || 0, to, car, carName: P.carNames[lang][CARS.indexOf(car)], date, time: `${String(hour).padStart(2, "0")}:${String(min).padStart(2, "0")}`,
    pax, bags, cabin, flight: s("flight", 20).toUpperCase(), name: s("name", 120), phone: s("phone", 40), email: s("email", 160),
    pickup: s("pickup", 200), dropoff: s("dropoff", 200), notes: s("notes", 1200), extras, label: pr.label, eur: pr.eur,
  };
  const ins = await db("site_checkouts", { method: "POST", body: JSON.stringify({ lang, amount_cents: pr.eur * 100, payload, ip_hash: ip }) });
  if (!ins.ok) return json({ error: t.err }, 500);
  const row = (await ins.json())[0];

  const [y, m, d] = date.split("-");
  const desc = `${d}/${m}/${y} ${payload.time} · ${payload.carName} · ${t.pax(pax)}`;
  const back = /^https:\/\/(darkdiamondluxury\.github\.io|(www\.)?darkdiamondluxury\.pt)\//.test(String(b.back || "")) ? String(b.back).split("?")[0].split("#")[0] : `${SITE}/`;
  const f = new URLSearchParams({
    mode: "payment", locale: lang,
    "line_items[0][quantity]": "1", "line_items[0][price_data][currency]": "eur", "line_items[0][price_data][unit_amount]": String(pr.eur * 100),
    "line_items[0][price_data][product_data][name]": `${t.svc[svc]} · ${pr.label}`, "line_items[0][price_data][product_data][description]": desc,
    success_url: `${back}?pago={CHECKOUT_SESSION_ID}#reservar`, cancel_url: `${back}?cancelado=1#reservar`,
    client_reference_id: row.id, "metadata[checkout_id]": row.id, "payment_intent_data[metadata][checkout_id]": row.id,
    "payment_intent_data[description]": `Dark Diamond Luxury · ${t.svc[svc]} · ${pr.label} · ${desc}`,
    expires_at: String(Math.floor(Date.now() / 1000) + 31 * 60),
    "payment_method_types[0]": "card", "payment_method_types[1]": "mb_way",
  });
  if (/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(payload.email)) f.set("customer_email", payload.email);
  let r = await stripe("checkout/sessions", f);
  if (!r.ok && JSON.stringify(r.body).includes("mb_way")) { f.delete("payment_method_types[1]"); r = await stripe("checkout/sessions", f); } // MB WAY ainda não ativo na conta
  if (!r.ok) { console.error("stripe", JSON.stringify(r.body?.error || r.body)); await db(`site_checkouts?id=eq.${row.id}`, { method: "DELETE" }); return json({ error: t.err }, 502); }
  await db(`site_checkouts?id=eq.${row.id}`, { method: "PATCH", body: JSON.stringify({ stripe_session_id: r.body.id, livemode: !!r.body.livemode }) });
  return json({ url: r.body.url, eur: pr.eur });
});
