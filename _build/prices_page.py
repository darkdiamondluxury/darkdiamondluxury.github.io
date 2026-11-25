# Página de preços (PT/EN/ES/FR). Os valores vêm de prices.py; aqui só os textos e a montagem.
from urllib.parse import quote
from prices import VEH, VEH_NAME, TRANSFERS, TOURS, NIGHT_EUR, NIGHT_FROM, NIGHT_TO, EXTRA_15MIN, ROUND_TRIP_PCT, CAPACITY

TXT = {
    'pt': dict(title='Preços · Dark Diamond Luxury', desc='Preços finais de transfers e tours privados em Lisboa, Portugal e Espanha, por viatura, com IVA incluído.',
               crumb='Preços', h1='Preços', lead='Preço final por viatura, com IVA incluído. Escolha a viatura e toque no destino para reservar.',
               veh='Viatura', tr_h='Transfers', tr_p='Preço por trajeto, só ida, a partir do aeroporto ou de Lisboa. IVA e portagens incluídos.',
               dest='Destino', troia='¹ Inclui a travessia de ferry da viatura e dos passageiros.',
               to_h='Tours', to_p='Preço por viatura, com IVA incluído. Portagens incluídas. Bilhetes de entrada em monumentos não incluídos.',
               tour='Tour', quote='Pedir orçamento', book='Reservar',
               q_h='Sob orçamento', q_p='Motorista à disposição, tours à medida, eventos, grupos de mais de 21 pessoas e destinos que não estão na tabela. Diga-nos o que precisa e respondemos com o preço.',
               q=['Motorista à disposição', 'Tour à medida', 'Eventos e casamentos', 'Outro destino']),
    'en': dict(title='Prices · Dark Diamond Luxury', desc='Final prices for private transfers and tours in Lisbon, Portugal and Spain, per vehicle, VAT included.',
               crumb='Prices', h1='Prices', lead='Final price per vehicle, VAT included. Choose the vehicle and tap the destination to book.',
               veh='Vehicle', tr_h='Transfers', tr_p='Price per journey, one way, from the airport or Lisbon. VAT and tolls included.',
               dest='Destination', troia='¹ Includes the ferry crossing for the vehicle and passengers.',
               to_h='Tours', to_p='Price per vehicle, VAT included. Tolls included. Monument entrance tickets not included.',
               tour='Tour', quote='Request a quote', book='Book',
               q_h='On request', q_p='Chauffeur at disposal, tailor-made tours, events, groups of more than 21 people and destinations not in the table. Tell us what you need and we reply with the price.',
               q=['Chauffeur at disposal', 'Tailor-made tour', 'Events and weddings', 'Another destination']),
    'es': dict(title='Precios · Dark Diamond Luxury', desc='Precios finales de traslados y tours privados en Lisboa, Portugal y España, por vehículo, IVA incluido.',
               crumb='Precios', h1='Precios', lead='Precio final por vehículo, IVA incluido. Elija el vehículo y toque el destino para reservar.',
               veh='Vehículo', tr_h='Traslados', tr_p='Precio por trayecto, solo ida, desde el aeropuerto o Lisboa. IVA y peajes incluidos.',
               dest='Destino', troia='¹ Incluye el ferry del vehículo y de los pasajeros.',
               to_h='Tours', to_p='Precio por vehículo, IVA incluido. Peajes incluidos. Entradas a monumentos no incluidas.',
               tour='Tour', quote='Pedir presupuesto', book='Reservar',
               q_h='Bajo presupuesto', q_p='Chófer a disposición, tours a medida, eventos, grupos de más de 21 personas y destinos que no están en la tabla. Díganos qué necesita y le respondemos con el precio.',
               q=['Chófer a disposición', 'Tour a medida', 'Eventos y bodas', 'Otro destino']),
    'fr': dict(title='Tarifs · Dark Diamond Luxury', desc='Prix finaux des transferts et tours privés à Lisbonne, au Portugal et en Espagne, par véhicule, TVA incluse.',
               crumb='Tarifs', h1='Tarifs', lead='Prix final par véhicule, TVA incluse. Choisissez le véhicule et touchez la destination pour réserver.',
               veh='Véhicule', tr_h='Transferts', tr_p="Prix par trajet, aller simple, depuis l'aéroport ou Lisbonne. TVA et péages inclus.",
               dest='Destination', troia='¹ Comprend la traversée en ferry du véhicule et des passagers.',
               to_h='Tours', to_p="Prix par véhicule, TVA incluse. Péages inclus. Billets d'entrée des monuments non inclus.",
               tour='Tour', quote='Demander un devis', book='Réserver',
               q_h='Sur devis', q_p="Chauffeur à disposition, tours sur mesure, événements, groupes de plus de 21 personnes et destinations hors tableau. Dites-nous ce qu'il vous faut et nous répondons avec le prix.",
               q=['Chauffeur à disposition', 'Tour sur mesure', 'Événements et mariages', 'Autre destination']),
}


def money(v, lang):
    if lang == 'en':
        return f'€{v:,}'
    s = f'{v:,}'.replace(',', '\u00a0') if v >= 1000 and lang != 'es' else str(v)
    return f'{s} €'


def _book(home, svc, to, car='E'):
    return f'{home}?svc={svc}&amp;car={car}&amp;to={quote(to)}#reservar'


def prices_html(lang, home):
    t = TXT[lang]
    names = VEH_NAME[lang]
    codes = [c for c, _ in VEH]
    chips = ''.join(f'<button type="button" data-car="{c}" aria-pressed="{str(c == "E").lower()}">{n}</button>' for c, n in zip(codes, names))
    head = lambda first: '<thead><tr><th scope="col">' + first + '</th>' + ''.join(  # noqa: E731
        f'<th scope="col" class="c c-{c}">{n}</th>' for c, n in zip(codes, names)) + '</tr></thead>'

    def cells(p, link_to, svc):
        out = []
        for c, v in zip(codes, p):
            if v is None:
                out.append(f'<td class="c c-{c} q"><a href="{_book(home, svc, link_to, c)}" data-l>{t["quote"]}</a></td>')
            else:
                out.append(f'<td class="c c-{c}"><a href="{_book(home, svc, link_to, c)}" data-l aria-label="{t["book"]}: {link_to}, {names[codes.index(c)]}, {money(v, lang)}">{money(v, lang)}</a></td>')
        return ''.join(out)

    tr_body = ''
    for g, rows in TRANSFERS:
        tr_body += f'<tbody><tr class="grp"><th colspan="7" scope="rowgroup">{g[lang]}</th></tr>'
        for n, km, p in rows:
            name = n[lang]
            clean = name.replace(' ¹', '')
            svc = 4 if km >= 190 else 0
            tr_body += f'<tr><th scope="row"><a href="{_book(home, svc, clean)}" data-l>{name}</a></th>{cells(p, clean, svc)}</tr>'
        tr_body += '</tbody>'
    to_body = '<tbody>' + ''.join(
        f'<tr><th scope="row"><a href="{_book(home, 2, n[lang])}" data-l>{n[lang]}</a></th>{cells(p, n[lang], 2)}</tr>' for n, p in TOURS) + '</tbody>'

    qbtn = ''.join(f'<a class="btn{"" if i == 0 else " ghost"}" href="{home}?svc={s}#reservar">{lbl}</a>' for i, (s, lbl) in enumerate(zip((1, 2, 3, 4), t['q'])))
    return f'''<section class="sec prices"><div class="wrap">
<div class="pr-veh" role="group" aria-label="{t['veh']}"><span class="pr-vl">{t['veh']}</span>{chips}</div>
<div class="pr-block" id="transfers"><h2 class="display">{t['tr_h']}</h2><p class="pr-note">{t['tr_p']}</p>
<table class="pt" data-car="E">{head(t['dest'])}{tr_body}</table>
<p class="pr-foot">{t['troia']}</p></div>
<div class="pr-block" id="tours"><h2 class="display">{t['to_h']}</h2><p class="pr-note">{t['to_p']}</p>
<table class="pt" data-car="E">{head(t['tour'])}{to_body}</table></div>
</div></section>
<section class="sec alt" id="condicoes"><div class="wrap"><h2 class="display pr-exh">{EXTRAS_H[lang]}</h2><ul class="pr-ex">{''.join(f'<li>{x}</li>' for x in extras_items(lang))}</ul></div></section>
<section class="ctab" id="orcamento"><div class="wrap"><div><h2 class="display">{t['q_h']}</h2><p>{t['q_p']}</p></div><div class="actions">{qbtn}</div></div></section>
<script>
(()=>{{const bar=document.querySelector('.pr-veh'),tabs=document.querySelectorAll('.pt');let car='E';
try{{const s=localStorage.getItem('ddl-preco-viatura');if(s&&bar.querySelector('[data-car="'+s+'"]'))car=s;}}catch(e){{}}
function set(c){{car=c;bar.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.car===c));tabs.forEach(t=>t.dataset.car=c);
  document.querySelectorAll('th[scope=row] a[data-l]').forEach(a=>{{a.href=a.href.replace(/car=[A-Z]/,'car='+c);}});
  try{{localStorage.setItem('ddl-preco-viatura',c);}}catch(e){{}}}}
bar.addEventListener('click',e=>{{const b=e.target.closest('button');if(!b)return;set(b.dataset.car);if(window.gcEv)gcEv('precos-viatura/'+b.dataset.car,location.pathname);}});
document.querySelectorAll('.pt a[data-l]').forEach(a=>a.addEventListener('click',()=>{{if(window.gcEv)gcEv('precos-reservar',location.pathname);}}));
set(car);}})();
</script>'''


# Extras e condições: usados na página de preços (#condicoes) e nos termos.
EXTRAS_H = {'pt': 'Extras e condições', 'en': 'Extras and conditions', 'es': 'Extras y condiciones', 'fr': 'Extras et conditions'}


def extras_items(lang):
    n = VEH_NAME[lang]
    per = ', '.join(f'{n[i]} {money(v, lang)}' for i, v in enumerate(EXTRA_15MIN))
    cap = ', '.join(f'{n[i]} {c}' for i, c in enumerate(CAPACITY))
    ne = money(NIGHT_EUR, lang)
    return {
        'pt': [f'<b>Suplemento noturno:</b> {ne} em tours e serviços à disposição entre as {NIGHT_FROM} e as {NIGHT_TO}. Os transfers custam o mesmo a qualquer hora, e as tours noturnas da tabela já o incluem.',
               f'<b>Espera extra e paragens extra</b> (paragens só se combinadas na reserva), por cada 15 minutos: {per}. A espera incluída é de 120 minutos no aeroporto, a contar da aterragem, e de 30 minutos nos outros locais.',
               '<b>Cadeiras de criança:</b> grátis, pedidas na reserva.',
               '<b>Golfe ou bicicletas:</b> sem custo, avisando na reserva. Obrigam a Classe V ou superior.',
               f'<b>Ida e volta:</b> {ROUND_TRIP_PCT} % de desconto no regresso, só em reservas diretas no site. Não se aplica a reservas feitas através de parceiros.',
               '<b>Cancelamento</b> sem penalização até 24 h antes (48 h em longa distância, eventos e serviços à disposição). Custos de processamento do pagamento (3 %) não reembolsáveis em caso de cancelamento.',
               f'<b>Lotação</b> (passageiros): {cap}. Para mais de 21 pessoas, enviamos orçamento.'],
        'en': [f'<b>Night supplement:</b> {ne} on tours and chauffeur-at-disposal services between {NIGHT_FROM.replace("h", ":")} and {NIGHT_TO.replace("h", ":")}. Transfers cost the same at any time, and the night tours in the table already include it.',
               f'<b>Extra waiting and extra stops</b> (stops only if agreed when booking), per 15 minutes: {per}. Waiting included: 120 minutes at the airport, from landing, and 30 minutes elsewhere.',
               '<b>Child seats:</b> free, requested when booking.',
               '<b>Golf bags or bicycles:</b> no charge, if mentioned when booking. They require a V-Class or larger.',
               f'<b>Return trip:</b> {ROUND_TRIP_PCT}% off the return journey, only on direct bookings through the site. It does not apply to bookings made through partners.',
               '<b>Cancellation</b> without penalty up to 24 h before (48 h for long distance, events and chauffeur-at-disposal services). Payment processing costs (3%) are not refundable if you cancel.',
               f'<b>Capacity</b> (passengers): {cap}. For more than 21 people, we send a quote.'],
        'es': [f'<b>Suplemento nocturno:</b> {ne} en tours y servicios a disposición entre las {NIGHT_FROM.replace("h", ":")} y las {NIGHT_TO.replace("h", ":")}. Los traslados cuestan lo mismo a cualquier hora, y los tours nocturnos de la tabla ya lo incluyen.',
               f'<b>Espera adicional y paradas adicionales</b> (paradas solo si se acuerdan al reservar), por cada 15 minutos: {per}. Espera incluida: 120 minutos en el aeropuerto, desde el aterrizaje, y 30 minutos en otros lugares.',
               '<b>Sillas infantiles:</b> gratis, pedidas al reservar.',
               '<b>Golf o bicicletas:</b> sin coste, avisando al reservar. Requieren Clase V o superior.',
               f'<b>Ida y vuelta:</b> {ROUND_TRIP_PCT} % de descuento en la vuelta, solo en reservas directas en la web. No se aplica a reservas hechas a través de colaboradores.',
               '<b>Cancelación</b> sin penalización hasta 24 h antes (48 h en larga distancia, eventos y servicios a disposición). Gastos de procesamiento del pago (3 %) no reembolsables en caso de cancelación.',
               f'<b>Capacidad</b> (pasajeros): {cap}. Para más de 21 personas, le enviamos presupuesto.'],
        'fr': [f'<b>Supplément de nuit :</b> {ne} sur les tours et les services à disposition entre {NIGHT_FROM} et {NIGHT_TO}. Les transferts coûtent le même prix à toute heure, et les tours de nuit du tableau l\'incluent déjà.',
               f'<b>Attente et arrêts supplémentaires</b> (arrêts uniquement s\'ils sont convenus à la réservation), par tranche de 15 minutes : {per}. Attente incluse : 120 minutes à l\'aéroport, à partir de l\'atterrissage, et 30 minutes ailleurs.',
               '<b>Sièges enfants :</b> gratuits, demandés à la réservation.',
               '<b>Golf ou vélos :</b> sans frais, en le signalant à la réservation. Ils exigent une Classe V ou supérieure.',
               f'<b>Aller-retour :</b> {ROUND_TRIP_PCT} % de réduction sur le retour, uniquement pour les réservations directes sur le site. Ne s\'applique pas aux réservations faites via des partenaires.',
               '<b>Annulation</b> sans pénalité jusqu\'à 24 h avant (48 h pour la longue distance, les événements et les services à disposition). Frais de traitement du paiement (3 %) non remboursables en cas d\'annulation.',
               f'<b>Capacité</b> (passagers) : {cap}. Au-delà de 21 personnes, nous envoyons un devis.'],
    }[lang]
