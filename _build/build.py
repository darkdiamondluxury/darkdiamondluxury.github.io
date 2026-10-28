#!/usr/bin/env python3
"""
Gera o site a partir de:
  config.py     dados da empresa, endereços das páginas
  home.html     modelo da página inicial (com marcadores {{...}})
  home_i18n.py  textos da página inicial em PT / EN / ES
  content.py    textos das páginas interiores em PT / EN / ES
Uso:  python3 _build/build.py    (corre a partir da raiz do repositório)
"""
import html
import hashlib as _h, os as _o
CSSV=_h.md5(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'..','assets','page.css'),'rb').read()).hexdigest()[:8]
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from chrome import GOAT, L, SVG_DEFS, dest_name, footer, head, nav, org_ld, tel, url  # noqa: E402
from config import BOOKINGS_KEY, BOOKINGS_URL, DESTS, EMAIL, IMG, LANGS, PHONES, REDIRECTS, SITE, SLUGS, WHATSAPP  # noqa: E402
import content  # noqa: E402
from home_i18n import MSG, MSG_FLIGHT, MSG_NOTES, PLACES, T  # noqa: E402

E = html.escape
written = []


def out_path(slug):
    p = slug.strip('/')
    return os.path.join(ROOT, p, 'index.html') if p else os.path.join(ROOT, 'index.html')


def write(slug_or_file, text):
    path = out_path(slug_or_file) if slug_or_file.endswith('/') else os.path.join(ROOT, slug_or_file.lstrip('/'))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    written.append(os.path.relpath(path, ROOT))


# ---------------------------------------------------------------- página inicial
def build_home(lang):
    t = T[lang]
    tpl = open(os.path.join(HERE, 'home.html'), encoding='utf-8').read()
    links = (f'<a href="#destinos">{t["nav_dest"]}</a><a href="#servicos">{t["nav_svc"]}</a>'
             f'<a href="#frota">{t["nav_fleet"]}</a><a href="#parceiros">{t["nav_ag"]}</a>')
    dlinks = f'<span>{L[lang]["dests"]}:</span> ' + ' '.join(f'<a href="{url(d, lang)}">{dest_name(d, lang)}</a>' for d in DESTS)
    js_t = {k: v for k, v in t.items() if k not in ('title', 'desc')}
    rep = {
        '{{LANG}}': lang,
        '{{HEAD}}': head('home', lang, t['title'], t['desc'], org_ld(lang)),
        '{{NAV}}': nav('home', lang, links, '#reservar'),
        '{{FOOTER}}': footer(lang),
        '{{T_JSON}}': json.dumps(js_t, ensure_ascii=False),
        '{{MSG_JSON}}': json.dumps({'tpl': MSG[lang], 'flight': MSG_FLIGHT[lang], 'notes': MSG_NOTES[lang]}, ensure_ascii=False),
        '{{PLACES_JSON}}': json.dumps([[n[lang] if isinstance(n, dict) else n, m] for n, m, _ in PLACES], ensure_ascii=False),
        '{{DLINKS}}': dlinks,
        '{{AIRPORT_URL}}': url('airport', lang),
        '{{CRUISE_URL}}': url('cruise', lang),
        '{{AG_URL}}': url('agencies', lang),
        '{{WHATSAPP}}': WHATSAPP,
        '{{BK_URL}}': BOOKINGS_URL,
        '{{BK_KEY}}': BOOKINGS_KEY,
        '{{GOAT}}': GOAT,
    }
    for k, v in rep.items():
        tpl = tpl.replace(k, v)

    # Texto "cozido" no HTML de cada língua: o Google lê a página já na língua certa.
    def fill(m):
        key = m.group(3)
        v = t.get(key)
        return m.group(1) + (E(v) if isinstance(v, str) else m.group(4)) + m.group(5)
    tpl = re.sub(r'(<(\w+)\b[^>]*\bdata-i18n="(\w+)"[^>]*>)(.*?)(</\2>)', fill, tpl, flags=re.S)
    tpl = re.sub(r'(data-i18n-ph="(\w+)"\s+placeholder=")[^"]*(")', lambda m: m.group(1) + E(t[m.group(2)]) + m.group(3), tpl)
    assert '{{' not in tpl, re.findall(r'\{\{\w+\}\}', tpl)
    write(url('home', lang), tpl)


# ---------------------------------------------------------------- páginas interiores
PAGE_JS = '''<script>
const nav=document.getElementById('nav');
const solid=()=>nav.classList.toggle('solid', scrollY>40);
addEventListener('scroll',solid,{passive:true}); solid();
document.getElementById('toTop').addEventListener('click',()=>scrollTo({top:0,behavior:'instant'}));
document.getElementById('yr').textContent=new Date().getFullYear();
</script>'''


def cta_buttons(lang, ctas, ctx):
    l = L[lang]
    out = []
    for i, (kind, label) in enumerate(ctas):
        cls = 'btn' if i == 0 else 'btn ghost'
        if ctx.get('on_gold'):
            cls = 'btn dark' if i == 0 else 'btn ghost'
        if kind == 'book':
            to = ctx.get('to')
            href = url('home', lang) + (f'?to={to}' if to else '') + '#reservar'
        elif kind == 'wa':
            href = f'https://wa.me/{WHATSAPP}' if WHATSAPP else url('home', lang) + '#reservar'
        elif kind == 'mail':
            href = f'mailto:{EMAIL}?subject={E(ctx.get("subject", "Dark Diamond Luxury"))}'
        elif kind == 'tel':
            href = tel(PHONES[0])
        elif kind == 'agencies':
            href = url('agencies', lang)
        else:
            href = kind
        out.append(f'<a class="{cls}" href="{href}">{E(label)}</a>')
    return '<div class="actions">' + ''.join(out) + '</div>'


def block_html(b, lang, ctx):
    k = b['type']
    cls = {'bone': ' bone', 'alt': ' alt'}.get(b.get('bg', ''), '')
    if k == 'split':
        body = ''.join(f'<p>{p}</p>' for p in b.get('p', []))
        if b.get('ticks'):
            body += '<ul class="ticks">' + ''.join(f'<li>{x}</li>' for x in b['ticks']) + '</ul>'
        if b.get('steps'):
            body += '<ol class="steps">' + ''.join(f'<li><div><b>{a}</b>{d}</div></li>' for a, d in b['steps']) + '</ol>'
        if b.get('rows'):
            body += '<dl class="rows">' + ''.join(f'<div><dt>{a}</dt><dd>{d}</dd></div>' for a, d in b['rows']) + '</dl>'
        if b.get('after'):
            body += ''.join(f'<p class="muted">{p}</p>' for p in b['after'])
        if b.get('related'):
            body += '<div class="related">' + ' '.join(f'<a href="{url(d, lang)}">{dest_name(d, lang)}</a>' for d in b['related']) + '</div>'
        return f'<section class="sec{cls}"><div class="wrap split"><h2 class="display">{b["h"]}</h2><div class="body">{body}</div></div></section>'
    if k == 'cta':
        return (f'<section class="ctab"><div class="wrap"><div><h2 class="display">{b["h"]}</h2>'
                f'{"<p>" + b["p"] + "</p>" if b.get("p") else ""}</div>{cta_buttons(lang, b["ctas"], {**ctx, "on_gold": True})}</div></section>')
    if k == 'prose':
        return f'<section class="sec"><div class="wrap prose">{b["html"]}</div></section>'
    raise ValueError(k)


def build_page(page, lang, d):
    l = L[lang]
    img = d.get('img')
    bg = f'<div class="bg"><img src="{IMG[img]}" alt="" fetchpriority="high" onerror="this.style.display=\'none\'"></div>' if img else ''
    crumbs = f'<p class="crumbs"><a href="{url("home", lang)}">{l["home"]}</a> / {E(d.get("crumb", d["h1"]))}</p>'
    ctx = {'to': d.get('to'), 'subject': d.get('subject')}
    hero = (f'<section class="phero{"" if img else " plain"}">{bg}<div class="in">{crumbs}'
            f'<h1 class="display">{d["h1"]}</h1><p class="lead">{d["lead"]}</p>'
            f'{cta_buttons(lang, d.get("ctas", []), ctx) if d.get("ctas") else ""}</div></section>')
    blocks = ''.join(block_html(b, lang, ctx) for b in d.get('blocks', []))
    t = T[lang]
    h = url('home', lang)
    links = (f'<a href="{h}#destinos">{t["nav_dest"]}</a><a href="{h}#servicos">{t["nav_svc"]}</a>'
             f'<a href="{h}#frota">{t["nav_fleet"]}</a>'
             f'<a href="{url("agencies", lang)}"{" aria-current=" + chr(34) + "page" + chr(34) if page == "agencies" else ""}>{t["nav_ag"]}</a>')
    ld = org_ld(lang) if page in ('agencies',) else None
    doc = f'''<!doctype html>
<html lang="{lang}">
<head>
{head(page, lang, d['title'], d['desc'], ld)}
<link rel="preload" href="/assets/jost-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/page.css?v={CSSV}">
</head>
<body class="pg-{page}{' gp' if page in ('agencies','airport') or page.startswith('d-') else ''}">
{SVG_DEFS}
{nav(page, lang, links, url('home', lang) + '#reservar')}
<main>
{hero}
{blocks}
</main>
{footer(lang)}
{PAGE_JS}
{GOAT}
</body>
</html>
'''
    write(url(page, lang), doc)


def build_redirects():
    for old, new in REDIRECTS.items():
        write(old, f'<!doctype html><html lang="pt"><head><meta charset="utf-8"><title>Dark Diamond Luxury</title>'
                   f'<meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{SITE}{new}">'
                   f'<script>location.replace("{new}")</script></head><body><a href="{new}">{SITE}{new}</a></body></html>')


def build_sitemap():
    rows = []
    for page in SLUGS:
        for lang in LANGS:
            alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{url(page, l)}"/>' for l in LANGS)
            pri = '1.0' if page == 'home' else '0.4' if page in ('privacy', 'legal', 'support') else '0.8'
            rows.append(f'  <url><loc>{SITE}{url(page, lang)}</loc>{alts}<priority>{pri}</priority></url>')
    write('/sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')
    write('/robots.txt', f'# O site público pode ser indexado; a app interna (/Despacho/) e o gerador (/_build/) não.\n'
          f'User-agent: *\nDisallow: /Despacho/\nDisallow: /_build/\n\nSitemap: {SITE}/sitemap.xml\n')


def build_404():
    """Página 404 de todo o domínio. Endereços da app interna (/Despacho/app/...) voltam à entrada da app,
    porque a app trata da navegação sozinha; o resto vê uma página simples com ligações."""
    write('/404.html', '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found · Dark Diamond Luxury</title><meta name="robots" content="noindex">
<script>if(location.pathname.indexOf('/Despacho/app')===0){location.replace('/Despacho/app/');}</script>
<link rel="stylesheet" href="/assets/page.css?v=@@V@@"></head><body>
<section class="phero plain"><div class="in"><h1 class="display">Page not found.</h1>
<p class="lead">Página não encontrada · Página no encontrada</p>
<div class="actions"><a class="btn" href="/">Dark Diamond Luxury</a><a class="btn ghost" href="/pt/">Português</a><a class="btn ghost" href="/es/">Español</a></div></div></section>
</body></html>'''.replace('@@V@@',CSSV))


if __name__ == '__main__':
    for lang in LANGS:
        build_home(lang)
        for page, data in content.PAGES.items():
            build_page(page, lang, data[lang])
    build_redirects()
    build_404()
    build_sitemap()
    print(f'{len(written)} ficheiros gerados')
