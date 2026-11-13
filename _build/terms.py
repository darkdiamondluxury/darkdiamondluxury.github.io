# Termos e condições (B5). Cada decisão do Bruno é um valor em TERMS.
# None = ainda por decidir → a página é gerada mas fica escondida (sem link, noindex, fora do mapa do site).
# Quando todos os valores estiverem preenchidos e 'live' passar a True, a página aparece no rodapé.
# Rascunho com as propostas: doc do projeto claude/termos-e-condicoes-rascunho.md
from config import EMAIL, LEGAL

TERMS = {
    'live': False,
    'updated': {'pt': 'novembro de 2026', 'en': 'November 2026', 'es': 'noviembre de 2026'},
    'change_free_h': None,      # alterações sem custo até X h antes (proposta 24)
    'vat_included': None,       # True / False (proposta True)
    'night': None,              # False = não há; ou dict(start='00:00', end='06:00', pct=20)
    'payment': None,            # 'full' (tudo na reserva) · 'deposit' (sinal) · 'after' (no fim)
    'deposit_pct': None,        # só se payment = 'deposit' (proposta 30)
    'cash': None,               # True / False: aceitam numerário?
    'wait_air': None,           # min grátis no aeroporto, a contar da aterragem (proposta 60)
    'wait_other': None,         # min grátis nas outras recolhas (proposta 15)
    'wait_extra_eur': None,     # € por cada 15 min de espera extra
    'cancel_free_h': None,      # cancelamento grátis até X h antes (proposta 24)
    'cancel_half_h': None,      # 50 % entre cancel_free_h e X h antes (proposta 6)
    'cancel_long_h': None,      # à disposição, eventos e longa distância: grátis até X h (proposta 48)
    'refund_days': None,        # reembolso em até X dias (proposta 14)
    'child_seat_eur': None,     # 0 = grátis; ou preço em €
    'pets': None,               # 'carrier' (em transportadora) · 'request' (a pedido) · 'no'
    'alcohol': None,            # 'no' · 'moderate' · 'events'
    'cleaning_eur': None,       # taxa de limpeza extraordinária em €
    'lost_days': 30,            # dias que se guardam objetos esquecidos
}


def missing():
    return [k for k, v in TERMS.items() if v is None and not (k == 'deposit_pct' and TERMS['payment'] != 'deposit')]


def _v(k, fmt=str):
    v = TERMS[k]
    return '<mark>[a confirmar]</mark>' if v is None else fmt(v)


def terms_html(lang):
    t = TERMS
    co = f'{LEGAL["name"]}, NIPC {LEGAL["nipc"]}, RNAAT {LEGAL["rnaat"]}'
    night = t['night']
    if lang == 'pt':
        pay = {'full': 'O pagamento total é feito na reserva.', 'deposit': f'Na reserva paga-se um sinal de {_v("deposit_pct")} % do preço; o restante no fim do serviço.',
               'after': 'O pagamento é feito no fim do serviço; pode também pagar antecipadamente.', None: '<mark>[a confirmar]</mark>'}[t['payment']]
        nightp = ('<mark>[a confirmar: suplemento noturno]</mark>' if night is None else '' if night is False else
                  f'<p>Serviços entre as {night["start"]} e as {night["end"]} têm um suplemento de {night["pct"]} %.</p>')
        pets = {'carrier': 'Animais de estimação são aceites em transportadora, se indicados na reserva.', 'request': 'Animais de estimação são aceites a pedido, se indicados na reserva.',
                'no': 'Não transportamos animais de estimação, exceto cães de assistência.', None: '<mark>[a confirmar: animais]</mark>'}[t['pets']]
        alc = {'no': 'Não é permitido consumir bebidas alcoólicas a bordo.', 'moderate': 'Bebidas alcoólicas a bordo só com moderação.',
               'events': 'Bebidas alcoólicas a bordo só em serviços de eventos e com moderação.', None: '<mark>[a confirmar: álcool]</mark>'}[t['alcohol']]
        seat = 'sem custo' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'por {x} € cada')
        return f'''<p>Última atualização: {t["updated"]["pt"]}. Estes termos aplicam-se aos serviços da Dark Diamond Luxury, nome comercial de {co}.</p>
<h2>Reserva e confirmação</h2>
<p>Um pedido feito pelo site, WhatsApp, telefone ou email só fica reservado depois de o confirmarmos por escrito, com o preço. Confirme que a data, a hora, o voo, as moradas, os passageiros e as malas estão corretos. Alterações sem custo até {_v("change_free_h")} h antes, sujeitas a disponibilidade.</p>
<h2>Preço</h2>
<p>O preço confirmado inclui viatura, motorista, combustível, portagens, estacionamento no aeroporto e o tempo de espera indicado abaixo{", com IVA incluído" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[IVA: a confirmar]</mark>"}. Não inclui espera extra, paragens não previstas, desvios pedidos durante a viagem nem horas extra em serviços à disposição.</p>
{nightp}
<h2>Pagamento</h2>
<p>{pay} Aceitamos cartão, MB WAY e transferência{", e numerário" if t["cash"] else "" if t["cash"] is False else " <mark>[numerário: a confirmar]</mark>"}. Empresas e parceiros podem ter faturação mensal, conforme acordado.</p>
<h2>Tempo de espera</h2>
<ul><li>Chegadas ao aeroporto: {_v("wait_air")} minutos sem custo, a contar da hora real de aterragem. Acompanhamos o voo, por isso um atraso não lhe custa nada.</li>
<li>Outras recolhas: {_v("wait_other")} minutos sem custo.</li>
<li>Espera extra: {_v("wait_extra_eur")} € por cada 15 minutos.</li></ul>
<p>Se o passageiro não aparecer nem responder depois do tempo de espera, o serviço conta como não comparência.</p>
<h2>Cancelamento</h2>
<ul><li>Até {_v("cancel_free_h")} h antes: sem custo, com reembolso total.</li>
<li>Entre {_v("cancel_free_h")} h e {_v("cancel_half_h")} h antes: 50 % do preço.</li>
<li>Com menos de {_v("cancel_half_h")} h ou não comparência: 100 % do preço.</li>
<li>Motorista à disposição, eventos, casamentos e longa distância: sem custo até {_v("cancel_long_h")} h antes.</li></ul>
<p>Os reembolsos são feitos pelo mesmo meio de pagamento, em até {_v("refund_days")} dias. Se formos nós a cancelar, devolvemos o valor total ou enviamos uma viatura equivalente, à sua escolha.</p>
<h2>Passageiros, bagagem e crianças</h2>
<p>O número de passageiros e malas indicado define a viatura. Se não couberem com segurança mais pessoas ou malas do que as indicadas, pode ser necessária outra viatura, com custo adicional. Cadeiras de criança e assentos elevatórios são obrigatórios por lei e fornecidos {seat}, se pedidos na reserva. Bagagem especial (golfe, ski, bicicletas, carrinhos de bebé) deve ser indicada na reserva. {pets}</p>
<h2>Conduta a bordo</h2>
<p>Não é permitido fumar, incluindo cigarros eletrónicos. {alc} Danos ou limpeza extraordinária causados por passageiros são cobrados: {_v("cleaning_eur")} € de limpeza, ou o custo real da reparação. O motorista pode recusar ou interromper o serviço se a segurança estiver em causa.</p>
<h2>Atrasos e força maior</h2>
<p>Não somos responsáveis por atrasos causados por trânsito anormal, acidentes, condições meteorológicas, greves, encerramento de estradas ou outras causas fora do nosso controlo. Recomendamos margem suficiente para voos e comboios.</p>
<h2>Objetos esquecidos</h2>
<p>Guardamos os objetos encontrados nas viaturas durante {_v("lost_days")} dias. A devolução pode ter custo de envio ou deslocação.</p>
<h2>Seguros, dados e reclamações</h2>
<p>Viaturas e passageiros estão cobertos por seguros de responsabilidade civil e de acidentes pessoais. Os dados pessoais são tratados conforme a <a href="/pt/privacidade/">política de privacidade</a>. Pode reclamar no <a href="https://www.livroreclamacoes.pt" rel="noopener">Livro de Reclamações Eletrónico</a> ou recorrer ao <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Centro de Arbitragem de Conflitos de Consumo de Lisboa</a>. Aplica-se a lei portuguesa. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
    if lang == 'es':
        pay = {'full': 'El pago total se realiza al reservar.', 'deposit': f'Al reservar se paga una señal del {_v("deposit_pct")} % del precio; el resto al final del servicio.',
               'after': 'El pago se realiza al final del servicio; también puede pagar por adelantado.', None: '<mark>[a confirmar]</mark>'}[t['payment']]
        nightp = ('<mark>[a confirmar]</mark>' if night is None else '' if night is False else
                  f'<p>Los servicios entre las {night["start"]} y las {night["end"]} tienen un suplemento del {night["pct"]} %.</p>')
        pets = {'carrier': 'Se aceptan mascotas en transportín, si se indican al reservar.', 'request': 'Se aceptan mascotas bajo petición, si se indican al reservar.',
                'no': 'No transportamos mascotas, salvo perros de asistencia.', None: '<mark>[a confirmar]</mark>'}[t['pets']]
        alc = {'no': 'No se permite consumir bebidas alcohólicas a bordo.', 'moderate': 'Bebidas alcohólicas a bordo solo con moderación.',
               'events': 'Bebidas alcohólicas a bordo solo en servicios de eventos y con moderación.', None: '<mark>[a confirmar]</mark>'}[t['alcohol']]
        seat = 'sin coste' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'por {x} € cada una')
        return f'''<p>Última actualización: {t["updated"]["es"]}. Estos términos se aplican a los servicios de Dark Diamond Luxury, nombre comercial de {co}.</p>
<h2>Reserva y confirmación</h2>
<p>Una solicitud hecha por la web, WhatsApp, teléfono o email solo queda reservada cuando la confirmamos por escrito, con el precio. Compruebe que la fecha, la hora, el vuelo, las direcciones, los pasajeros y las maletas son correctos. Cambios sin coste hasta {_v("change_free_h")} h antes, según disponibilidad.</p>
<h2>Precio</h2>
<p>El precio confirmado incluye vehículo, chófer, combustible, peajes, aparcamiento en el aeropuerto y el tiempo de espera indicado abajo{", IVA incluido" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[IVA: a confirmar]</mark>"}. No incluye espera adicional, paradas no previstas, desvíos pedidos durante el viaje ni horas extra en servicios a disposición.</p>
{nightp}
<h2>Pago</h2>
<p>{pay} Aceptamos tarjeta, MB WAY y transferencia{", y efectivo" if t["cash"] else "" if t["cash"] is False else " <mark>[efectivo: a confirmar]</mark>"}. Empresas y colaboradores pueden tener facturación mensual, según lo acordado.</p>
<h2>Tiempo de espera</h2>
<ul><li>Llegadas al aeropuerto: {_v("wait_air")} minutos sin coste, desde la hora real de aterrizaje. Seguimos el vuelo, así que un retraso no le cuesta nada.</li>
<li>Otras recogidas: {_v("wait_other")} minutos sin coste.</li>
<li>Espera adicional: {_v("wait_extra_eur")} € por cada 15 minutos.</li></ul>
<p>Si el pasajero no aparece ni responde tras el tiempo de espera, el servicio cuenta como no presentado.</p>
<h2>Cancelación</h2>
<ul><li>Hasta {_v("cancel_free_h")} h antes: sin coste, con reembolso total.</li>
<li>Entre {_v("cancel_free_h")} h y {_v("cancel_half_h")} h antes: 50 % del precio.</li>
<li>Con menos de {_v("cancel_half_h")} h o no presentado: 100 % del precio.</li>
<li>Chófer a disposición, eventos, bodas y larga distancia: sin coste hasta {_v("cancel_long_h")} h antes.</li></ul>
<p>Los reembolsos se hacen por el mismo medio de pago, en un máximo de {_v("refund_days")} días. Si cancelamos nosotros, devolvemos el importe total o enviamos un vehículo equivalente, a su elección.</p>
<h2>Pasajeros, equipaje y niños</h2>
<p>El número de pasajeros y maletas indicado define el vehículo. Si no caben con seguridad más personas o maletas de las indicadas, puede ser necesario otro vehículo, con coste adicional. Las sillas infantiles y los elevadores son obligatorios por ley y se facilitan {seat}, si se piden al reservar. El equipaje especial (golf, esquí, bicicletas, cochecitos) debe indicarse al reservar. {pets}</p>
<h2>Conducta a bordo</h2>
<p>No se permite fumar, tampoco cigarrillos electrónicos. {alc} Los daños o la limpieza extraordinaria causados por pasajeros se cobran: {_v("cleaning_eur")} € de limpieza, o el coste real de la reparación. El chófer puede rechazar o interrumpir el servicio si la seguridad está en juego.</p>
<h2>Retrasos y fuerza mayor</h2>
<p>No somos responsables de retrasos causados por tráfico anormal, accidentes, meteorología, huelgas, cierres de carreteras u otras causas ajenas a nuestro control. Recomendamos margen suficiente para vuelos y trenes.</p>
<h2>Objetos olvidados</h2>
<p>Guardamos los objetos encontrados en los vehículos durante {_v("lost_days")} días. La devolución puede tener coste de envío o desplazamiento.</p>
<h2>Seguros, datos y reclamaciones</h2>
<p>Vehículos y pasajeros están cubiertos por seguros de responsabilidad civil y de accidentes personales. Los datos personales se tratan según la <a href="/es/privacidad/">política de privacidad</a>. Puede reclamar en el <a href="https://www.livroreclamacoes.pt" rel="noopener">Libro de Reclamaciones Electrónico</a> o acudir al <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Centro de Arbitraje de Conflictos de Consumo de Lisboa</a>. Se aplica la ley portuguesa. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
    pay = {'full': 'Full payment is made when you book.', 'deposit': f'A deposit of {_v("deposit_pct")}% is paid when you book; the balance at the end of the service.',
           'after': 'Payment is made at the end of the service; you can also pay in advance.', None: '<mark>[to confirm]</mark>'}[t['payment']]
    nightp = ('<mark>[to confirm]</mark>' if night is None else '' if night is False else
              f'<p>Services between {night["start"]} and {night["end"]} carry a {night["pct"]}% surcharge.</p>')
    pets = {'carrier': 'Pets are welcome in a carrier, if mentioned when booking.', 'request': 'Pets are accepted on request, if mentioned when booking.',
            'no': 'We do not carry pets, except assistance dogs.', None: '<mark>[to confirm]</mark>'}[t['pets']]
    alc = {'no': 'Alcohol may not be consumed on board.', 'moderate': 'Alcohol on board in moderation only.',
           'events': 'Alcohol on board only on event services, in moderation.', None: '<mark>[to confirm]</mark>'}[t['alcohol']]
    seat = 'free of charge' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'at €{x} each')
    return f'''<p>Last updated: {t["updated"]["en"]}. These terms apply to services provided by Dark Diamond Luxury, the trading name of {co}.</p>
<h2>Booking and confirmation</h2>
<p>A request made through the website, WhatsApp, phone or email is only booked once we confirm it in writing, with the price. Please check that the date, time, flight, addresses, passengers and luggage are correct. Changes are free up to {_v("change_free_h")} h before, subject to availability.</p>
<h2>Price</h2>
<p>The confirmed price includes vehicle, driver, fuel, tolls, airport parking and the waiting time below{", VAT included" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[VAT: to confirm]</mark>"}. It does not include extra waiting, unplanned stops, detours requested during the journey or extra hours on chauffeur-at-disposal services.</p>
{nightp}
<h2>Payment</h2>
<p>{pay} We accept card, MB WAY and bank transfer{", and cash" if t["cash"] else "" if t["cash"] is False else " <mark>[cash: to confirm]</mark>"}. Companies and partners may be invoiced monthly, as agreed.</p>
<h2>Waiting time</h2>
<ul><li>Airport arrivals: {_v("wait_air")} minutes free, from the actual landing time. We track your flight, so a delay costs you nothing.</li>
<li>Other pick-ups: {_v("wait_other")} minutes free.</li>
<li>Extra waiting: €{_v("wait_extra_eur")} per 15 minutes.</li></ul>
<p>If the passenger does not appear or respond after the waiting time, the service counts as a no-show.</p>
<h2>Cancellation</h2>
<ul><li>Up to {_v("cancel_free_h")} h before: free, full refund.</li>
<li>Between {_v("cancel_free_h")} h and {_v("cancel_half_h")} h before: 50% of the price.</li>
<li>Less than {_v("cancel_half_h")} h before, or no-show: 100% of the price.</li>
<li>Chauffeur at disposal, events, weddings and long distance: free up to {_v("cancel_long_h")} h before.</li></ul>
<p>Refunds are made to the original payment method within {_v("refund_days")} days. If we cancel, we refund in full or send an equivalent vehicle, as you prefer.</p>
<h2>Passengers, luggage and children</h2>
<p>The number of passengers and bags you give sets the vehicle. If more people or bags turn up than booked and they do not fit safely, another vehicle may be needed at extra cost. Child seats and boosters are required by law and provided {seat} when requested at booking. Special luggage (golf, ski, bicycles, pushchairs) should be mentioned when booking. {pets}</p>
<h2>Conduct on board</h2>
<p>No smoking, including e-cigarettes. {alc} Damage or extraordinary cleaning caused by passengers is charged: €{_v("cleaning_eur")} for cleaning, or the actual cost of repair. The driver may refuse or stop the service if safety is at risk.</p>
<h2>Delays and force majeure</h2>
<p>We are not liable for delays caused by abnormal traffic, accidents, weather, strikes, road closures or other causes beyond our control. Please allow enough time for flights and trains.</p>
<h2>Lost property</h2>
<p>Items found in our vehicles are kept for {_v("lost_days")} days. Returning them may involve delivery or travel costs.</p>
<h2>Insurance, data and complaints</h2>
<p>Vehicles and passengers are covered by third-party liability and personal accident insurance. Personal data is handled under our <a href="/privacy/">privacy policy</a>. You can file a complaint in the <a href="https://www.livroreclamacoes.pt" rel="noopener">Electronic Complaints Book</a> or refer to the <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Lisbon Consumer Arbitration Centre</a>. Portuguese law applies. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
