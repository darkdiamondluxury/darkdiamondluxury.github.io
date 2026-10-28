# Peças comuns a todas as páginas: <head>, navegação, troca de língua e rodapé.
import html
import json

from config import (BRAND, COVERAGE, DESTS, EMAIL, INSTAGRAM, LANG_NAME, LANGS, LEGAL, LOCALE, PHONES, SITE, SLUGS,
                    WHATSAPP, WHATSAPP_ALL)

E = html.escape

L = {
 'pt': dict(nav_label='Principal', lang_label='Língua', contact='Contacto', company='Empresa', info='Informação', services='Serviços',
            airport='Transfer aeroporto', cruise='Terminal de cruzeiros', agencies='Agências e parceiros', dests='Destinos',
            privacy='Privacidade', legal='Informação legal', support='Suporte da app', complaints='Livro de Reclamações',
            top='Voltar ao início', book='Reservar', rnaat='Registo RNAAT n.º', nipc='NIPC', brand_of='é uma marca de',
            credits='Fotografias ilustrativas, Unsplash License:', home='Início', coverage='Cobertura'),
 'en': dict(nav_label='Main', lang_label='Language', contact='Contact', company='Company', info='Information', services='Services',
            airport='Airport transfer', cruise='Cruise terminal', agencies='Agencies and partners', dests='Destinations',
            privacy='Privacy', legal='Legal information', support='App support', complaints='Complaints Book (Livro de Reclamações)',
            top='Back to top', book='Book', rnaat='RNAAT registration no.', nipc='VAT no. (NIPC)', brand_of='is a brand of',
            credits='Illustrative photographs, Unsplash License:', home='Home', coverage='Coverage'),
 'es': dict(nav_label='Principal', lang_label='Idioma', contact='Contacto', company='Empresa', info='Información', services='Servicios',
            airport='Traslado aeropuerto', cruise='Terminal de cruceros', agencies='Agencias y partners', dests='Destinos',
            privacy='Privacidad', legal='Aviso legal', support='Soporte de la app', complaints='Libro de Reclamaciones (Livro de Reclamações)',
            top='Volver arriba', book='Reservar', rnaat='Registro RNAAT n.º', nipc='NIF (NIPC)', brand_of='es una marca de',
            credits='Fotografías ilustrativas, Unsplash License:', home='Inicio', coverage='Cobertura'),
}
DEST_NAME = {'d-sintra': 'Sintra', 'd-cascais': 'Cascais', 'd-comporta': 'Comporta', 'd-evora': 'Évora', 'd-fatima': 'Fátima',
             'd-algarve': 'Algarve', 'd-porto': {'pt': 'Porto', 'en': 'Porto', 'es': 'Oporto'}}


def dest_name(k, lang):
    n = DEST_NAME[k]
    return n[lang] if isinstance(n, dict) else n


def url(page, lang):
    return SLUGS[page][lang]


def head(page, lang, title, desc, extra_ld=None):
    """<meta>, canonical, hreflang (versões noutras línguas) e Open Graph."""
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{url(page, l)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE}{url(page, LANGS[0])}">'
    ld = ''
    if extra_ld:
        ld = f'<script type="application/ld+json">{json.dumps(extra_ld, ensure_ascii=False)}</script>'
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#050505">
<link rel="canonical" href="{SITE}{url(page, lang)}">
{alts}
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{url(page, lang)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="google-site-verification" content="7xoDgQRwv990JpySxhvBizAM3TBYI5-SQdsn1q0e9Ig">
{ld}'''


def org_ld(lang):
    """Dados estruturados para o Google (quem somos, onde, contactos)."""
    return {
        '@context': 'https://schema.org', '@type': 'LocalBusiness', 'name': BRAND, 'legalName': LEGAL['name'],
        'url': SITE + '/', 'image': SITE + '/assets/og.png', 'logo': SITE + '/assets/icon-512.png',
        'telephone': PHONES[0], 'email': EMAIL, 'vatID': 'PT' + LEGAL['nipc'],
        'address': {'@type': 'PostalAddress', 'streetAddress': LEGAL['street'], 'postalCode': LEGAL['postcode'],
                    'addressLocality': LEGAL['city'], 'addressCountry': 'PT'},
        'areaServed': [{'@type': 'Country', 'name': n} for n in ('Portugal', 'Spain', 'France')],
        'description': {'pt': 'Transfers privados, tours e motorista à disposição em Lisboa, Portugal, Espanha e França.',
                        'en': 'Private transfers, tours and chauffeur services in Lisbon, Portugal, Spain and France.',
                        'es': 'Traslados privados, tours y chófer a disposición en Lisboa, Portugal, España y Francia.'}[lang],
    }


def lang_switch(page, lang):
    l = L[lang]
    cur = ' aria-current="true"'
    items = ''.join(
        f'<a href="{url(page, x)}" hreflang="{x}" lang="{x}"{cur if x == lang else ""}>{LANG_NAME[x]}</a>'
        for x in ['pt', 'en', 'es'])
    return f'<nav class="lang" aria-label="{l["lang_label"]}">{items}</nav>'


def nav(page, lang, links_html, cta_href):
    l = L[lang]
    return f'''<header class="nav" id="nav">
  <a class="brand" href="{url('home', lang)}" aria-label="{BRAND}"><img src="/assets/logo.png" alt="" width="40" height="40"><span class="dk">Dark</span> <span class="dm">Diamond</span> <span class="lux">Luxury</span></a>
  <nav class="links" aria-label="{l['nav_label']}">{links_html}</nav>
  {lang_switch(page, lang)}
  <a class="btn" href="{cta_href}">{l['book']}</a>
</header>'''


SVG_DEFS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="dd" viewBox="0 0 24 24"><path d="M6 3h12l4 6-10 12L2 9z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M2 9h20M9 3l3 18 3-18" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round" opacity=".7"/></symbol>
</svg>'''


def tel(p):
    return 'tel:' + p.replace(' ', '')


def footer(lang):
    l = L[lang]
    wa = ''
    ig = f'<a href="{INSTAGRAM}">Instagram</a>' if INSTAGRAM else ''
    phones = ''.join(
        f'<span class="ph"><a href="{tel(p)}">{p}</a>'
        + (f' · <a href="https://wa.me/{p.replace("+", "").replace(" ", "")}">WhatsApp</a>' if p.replace('+', '').replace(' ', '') in WHATSAPP_ALL else '')
        + '</span>' for p in PHONES)
    dests = ' '.join(f'<a href="{url(d, lang)}">{dest_name(d, lang)}</a>' for d in DESTS)  # espaços = pontos onde a linha pode quebrar
    return f'''<footer>
  <div class="foot-top">
    <div class="word"><img src="/assets/logo.png" alt="" width="200" height="200"><span class="dk">Dark</span> <span class="dm">Diamond</span><br><em>Luxury</em></div>
    <button class="btn totop" type="button" id="toTop"><span>{l['top']}</span><span aria-hidden="true">↑</span></button>
  </div>
  <div class="cols">
    <div><b>{l['contact']}</b>{phones}<a href="mailto:{EMAIL}">{EMAIL}</a>{wa}{ig}
      <p class="cov"><b>{l['coverage']}</b>{COVERAGE[lang]}</p></div>
    <div><b>{l['services']}</b><a href="{url('airport', lang)}">{l['airport']}</a><a href="{url('cruise', lang)}">{l['cruise']}</a>
      <b class="sub">{l['dests']}</b><span class="inline">{dests}</span></div>
    <div><b>{l['info']}</b><a href="{url('agencies', lang)}">{l['agencies']}</a><a href="{url('legal', lang)}">{l['legal']}</a><a href="{url('privacy', lang)}">{l['privacy']}</a><a href="https://www.livroreclamacoes.pt" rel="noopener">{l['complaints']}</a><a href="{url('support', lang)}">{l['support']}</a></div>
  </div>
  <p class="legalline">{BRAND} {l['brand_of']} {LEGAL['name']} · {l['nipc']} {LEGAL['nipc']} · {LEGAL['street']}, {LEGAL['postcode']} {LEGAL['city']} · {l['rnaat']} {LEGAL['rnaat']}</p>
  <p class="credits"><span>{l['credits']}</span>
    <a href="https://unsplash.com/photos/jHw55im3a8Q">Marc Najera</a>,
    <a href="https://unsplash.com/photos/JlnS8Zl9RcQ">Dani and Juan</a>,
    <a href="https://unsplash.com/photos/yydI2Op7ILs">Iler Stoe</a>,
    <a href="https://unsplash.com/photos/oe4QHK9EwS8">Luis Quintero</a>,
    <a href="https://unsplash.com/photos/gOLCAOuc7iA">Svetlana Gumerova</a>,
    <a href="https://unsplash.com/photos/airplane-on-sky-during-golden-hour-M0AWNxnLaMw">Tom Barrett</a>,
    <a href="https://unsplash.com/photos/a-city-street-at-night-with-a-clock-tower-in-the-background-uyCK9mfsLfw">Clovis Wood</a>,
    <a href="https://unsplash.com/photos/a-castle-like-building-with-a-yellow-roof-LhYFlcgQQJA">Hasmik Ghazaryan Olson</a>,
    <a href="https://unsplash.com/photos/landscape-photography-of-white-canopy-tent-dcb2pog89fQ">Photos by Lanty</a>,
    <a href="https://unsplash.com/photos/an-aerial-view-of-a-highway-in-the-mountains-lu3gOnEVFZw">Marlon Santizo</a>,
    <a href="https://unsplash.com/photos/cruise-ship-sails-through-dramatic-sunset-clouds-over-the-ocean-bO3cow4Ezq4">zhao chen</a>,
    <a href="https://unsplash.com/photos/yellow-tram-in-historic-lisbon-street-ljhCEaHYWJ8">Aayush Gupta</a>,
    <a href="https://unsplash.com/s/photos/cascais">Calin Stan</a>,
    <a href="https://unsplash.com/photos/an-aerial-view-of-a-beach-and-ocean-MZ187oc9b9M">Diogo Monteiro</a>,
    <a href="https://unsplash.com/photos/a-group-of-stone-pillars-sitting-next-to-each-other-PP2SUFjOoCE">Beatriz Queiroz</a>,
    <a href="https://unsplash.com/photos/jagged-coastal-cliffs-with-arches-and-ocean-waves--eeaFLsJDbY">Jeffrey Eisen</a>,
    <a href="https://unsplash.com/photos/boats-on-douro-river-in-porto-Prb-sjOUBFs">Nick Karvounis</a>,
    <a href="https://unsplash.com/photos/metropolis-building-and-gran-via-madrid-WBGjg0DsO_g">Florian Wehde</a>,
    <a href="https://unsplash.com/photos/plaza-de-espana-architecture-in-seville-a96wj8idE_I">Tânia Mousinho</a>,
    <a href="https://unsplash.com/photos/many-boats-docked-in-a-marina-with-white-buildings-SmVxCpaziJg">ionut dobre</a>,
    <a href="https://unsplash.com/photos/a-view-of-a-golf-course-with-the-ocean-in-the-background-Alo3lgdV2CU">Frederik Rosar</a>,
    <a href="https://www.pexels.com/photo/aerial-view-of-fatima-sanctuary-in-portugal-30443719/">magr S (Pexels)</a>,
    <a href="https://www.pexels.com/photo/sunny-praia-da-rocha-beach-in-algarve-portugal-33887497/">Carel Voorhorst (Pexels)</a>,
    <a href="https://unsplash.com/photos/c1iZp1LoIpM">Pascal Bernardon</a>,
    <a href="https://www.pexels.com/photo/aerial-view-of-luxury-marina-in-marbella-spain-28428861/">David Pickup (Pexels)</a>,
    <a href="https://unsplash.com/photos/a-commercial-airplane-flying-through-fluffy-clouds-7gJyHcCStT0">Hieu</a>,
    <a href="https://unsplash.com/photos/interior-view-of-a-cars-steering-wheel-and-dashboard-Oqq4isWzHsU">William G</a>,
    <a href="https://unsplash.com/photos/couple-walks-towards-a-mediterranean-style-building-XL09jDIzg3Y">Fotógrafo Samuel Cruz</a>,
    <a href="https://unsplash.com/photos/a-scenic-view-of-a-valley-with-a-river-running-through-it-n0IVV6m5hfI">Thomas Gabernig</a>,
    <a href="https://unsplash.com/photos/white-cruise-ship-on-sea-during-daytime-xEJoSsDCnR8">Georgy Trofimov</a>,
    <a href="https://unsplash.com/photos/dark-car-interior-with-starry-headliner-9hD5_2LrU3g">Rana Singh</a>.
    © <span id="yr">2026</span> {BRAND}.</p>
</footer>'''

GOAT = '<script data-goatcounter="https://darkdiamondluxury.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'
