# Formulário "Seja nosso parceiro" (página de agências). Só toques; envia por WhatsApp ou email.
import json

PT = {
    'h': 'Vamos trabalhar juntos.',
    'p': 'Diga-nos quem é e o que precisa. Respondemos com uma tabela de preços para o seu negócio.',
    'type_q': 'O seu negócio', 'types': ['Agência de viagens', 'Operador ou DMC', 'Hotel ou alojamento', 'Linha de cruzeiros', 'Empresa', 'Empresa de transportes ou motorista', 'Outro'],
    'vol_q': 'Serviços por mês, mais ou menos', 'vols': ['Até 10', '10 a 50', 'Mais de 50', 'Ainda não sei'],
    'svc_q': 'O que lhe interessa', 'svcs': ['Aeroporto', 'Cruzeiros', 'Motorista à disposição', 'Tours', 'Eventos', 'Longa distância'],
    'name': 'O seu nome', 'company': 'Empresa', 'contact': 'Email ou telefone',
    'send': 'Enviar no WhatsApp', 'mail': 'Prefiro email',
    'err': 'Escolha o tipo de negócio e escreva o seu nome.',
    'msg_h': 'Pedido de parceria', 'l_type': 'Tipo', 'l_vol': 'Volume mensal', 'l_svc': 'Serviços', 'l_name': 'Nome', 'l_company': 'Empresa', 'l_contact': 'Contacto',
}
EN = {
    'h': 'Let\'s work together.',
    'p': 'Tell us who you are and what you need. We reply with a rate sheet for your business.',
    'type_q': 'Your business', 'types': ['Travel agency', 'Tour operator or DMC', 'Hotel or rental', 'Cruise line', 'Company', 'Transport company or driver', 'Other'],
    'vol_q': 'Services per month, roughly', 'vols': ['Up to 10', '10 to 50', 'More than 50', 'Not sure yet'],
    'svc_q': 'What you need', 'svcs': ['Airport', 'Cruises', 'Chauffeur at disposal', 'Tours', 'Events', 'Long distance'],
    'name': 'Your name', 'company': 'Company', 'contact': 'Email or phone',
    'send': 'Send on WhatsApp', 'mail': 'I prefer email',
    'err': 'Choose your type of business and write your name.',
    'msg_h': 'Partnership request', 'l_type': 'Type', 'l_vol': 'Monthly volume', 'l_svc': 'Services', 'l_name': 'Name', 'l_company': 'Company', 'l_contact': 'Contact',
}
ES = {
    'h': 'Trabajemos juntos.',
    'p': 'Díganos quién es y qué necesita. Le respondemos con una tabla de tarifas para su negocio.',
    'type_q': 'Su negocio', 'types': ['Agencia de viajes', 'Operador o DMC', 'Hotel o alojamiento', 'Naviera', 'Empresa', 'Empresa de transporte o chófer', 'Otro'],
    'vol_q': 'Servicios al mes, más o menos', 'vols': ['Hasta 10', '10 a 50', 'Más de 50', 'Aún no lo sé'],
    'svc_q': 'Qué le interesa', 'svcs': ['Aeropuerto', 'Cruceros', 'Chófer a disposición', 'Tours', 'Eventos', 'Larga distancia'],
    'name': 'Su nombre', 'company': 'Empresa', 'contact': 'Email o teléfono',
    'send': 'Enviar por WhatsApp', 'mail': 'Prefiero email',
    'err': 'Elija el tipo de negocio y escriba su nombre.',
    'msg_h': 'Solicitud de colaboración', 'l_type': 'Tipo', 'l_vol': 'Volumen mensual', 'l_svc': 'Servicios', 'l_name': 'Nombre', 'l_company': 'Empresa', 'l_contact': 'Contacto',
}
T = {'pt': PT, 'en': EN, 'es': ES}


def partner_html(lang, whatsapp, email, esc):
    t = T[lang]
    chips = lambda name, opts, multi=False: ''.join(  # noqa: E731
        f'<button type="button" data-g="{name}"{" data-multi" if multi else ""} aria-pressed="false">{esc(o)}</button>' for o in opts)
    return f'''<section class="ctab pf-sec" id="parceria"><div class="wrap pf-wrap">
<div><h2 class="display">{t['h']}</h2><p>{t['p']}</p></div>
<form class="pf" id="pf" novalidate>
  <p class="pf-q" id="pfq1">{t['type_q']}</p><div class="pf-chips" role="group" aria-labelledby="pfq1">{chips('type', t['types'])}</div>
  <p class="pf-q" id="pfq2">{t['vol_q']}</p><div class="pf-chips" role="group" aria-labelledby="pfq2">{chips('vol', t['vols'])}</div>
  <p class="pf-q" id="pfq3">{t['svc_q']}</p><div class="pf-chips multi" role="group" aria-labelledby="pfq3">{chips('svc', t['svcs'], True)}</div>
  <div class="pf-fields">
    <label><span>{t['name']}</span><input id="pfName" autocomplete="name" required></label>
    <label><span>{t['company']}</span><input id="pfCo" autocomplete="organization"></label>
    <label class="wide"><span>{t['contact']}</span><input id="pfContact" autocomplete="email" inputmode="email"></label>
  </div>
  <p class="pf-err" id="pfErr" role="alert"></p>
  <div class="actions"><button class="btn dark" type="submit">{t['send']}</button><button class="btn ghost" type="button" id="pfMail">{t['mail']}</button></div>
</form>
</div></section>
<script>
(()=>{{const T={json.dumps({k: t[k] for k in ('err', 'msg_h', 'l_type', 'l_vol', 'l_svc', 'l_name', 'l_company', 'l_contact')}, ensure_ascii=False)};
const f=document.getElementById('pf'),err=document.getElementById('pfErr'),v=id=>document.getElementById(id).value.trim();
f.addEventListener('click',e=>{{const b=e.target.closest('[data-g]');if(!b)return;
  if(b.hasAttribute('data-multi'))b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!=='true');
  else f.querySelectorAll(`[data-g="${{b.dataset.g}}"]`).forEach(x=>x.setAttribute('aria-pressed',x===b));
  err.textContent='';}});
const pick=g=>[...f.querySelectorAll(`[data-g="${{g}}"][aria-pressed="true"]`)].map(x=>x.textContent).join(', ');
const msg=()=>{{if(!pick('type')||!v('pfName')){{err.textContent=T.err;(pick('type')?document.getElementById('pfName'):f.querySelector('[data-g]')).focus();return null;}}
  const L=[[T.l_type,pick('type')],[T.l_vol,pick('vol')],[T.l_svc,pick('svc')],[T.l_name,v('pfName')],[T.l_company,v('pfCo')],[T.l_contact,v('pfContact')]];
  try{{window.goatcounter&&goatcounter.count({{path:'parceria-pedido',event:true}})}}catch(e){{}}
  return T.msg_h+' · Dark Diamond Luxury\\n\\n'+L.filter(x=>x[1]).map(x=>x[0]+': '+x[1]).join('\\n');}};
f.addEventListener('submit',e=>{{e.preventDefault();const m=msg();if(m)window.open('https://wa.me/{whatsapp}?text='+encodeURIComponent(m),'_blank','noopener');}});
document.getElementById('pfMail').addEventListener('click',()=>{{const m=msg();if(m)location.href='mailto:{email}?subject='+encodeURIComponent(T.msg_h)+'&body='+encodeURIComponent(m);}});
}})();
</script>'''
