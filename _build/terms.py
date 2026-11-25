# Termos e condições (B5). Cada decisão do Bruno é um valor em TERMS.
# None = ainda por decidir → a página é gerada mas fica escondida (sem link, noindex, fora do mapa do site).
# Quando todos os valores estiverem preenchidos e 'live' passar a True, a página aparece no rodapé.
# Rascunho com as propostas: doc do projeto claude/termos-e-condicoes-rascunho.md
from config import EMAIL, LEGAL, PAY_MODE
from prices_page import EXTRAS_H, extras_items

TERMS = {
    'live': True,
    'updated': {'pt': 'novembro de 2026', 'en': 'November 2026', 'es': 'noviembre de 2026', 'fr': 'novembre 2026'},
    'change_free_h': 24,        # alterações sem custo até 24 h antes (25/11)
    'vat_included': True,       # preços com IVA incluído (tabela de 25/11/2026)
    'night': 'extras',          # suplemento noturno e restantes extras: secção Extras (prices.py, 25/11/2026)
    'payment': 'full',          # pagamento total na reserva (reunião de 22/11/2026)
    'deposit_pct': None,        # só se payment = 'deposit' (proposta 30)
    'cash': False,              # sem numerário (25/11)
    'wait_air': 120,            # min grátis no aeroporto, a contar da aterragem (Bruno, 22/11)
    'wait_other': 30,           # min grátis nas outras recolhas (Bruno, 22/11)
    'wait_extra_eur': 'extras', # por viatura, na secção Extras (prices.py)
    'cancel_free_h': 24,        # cancelamento grátis até 24 h antes (Bruno, 22/11)
    'cancel_half_h': 3,         # 50 % entre 24 h e 3 h antes (Bruno, 22/11)
    'cancel_long_h': 48,        # longa distância, eventos e à disposição (reunião de 22/11)
    'refund_days': 5,           # dias úteis (25/11)
    'fee_pct': 3,               # custos bancários e de processamento, não reembolsáveis (25/11)
    'child_seat_eur': 0,        # grátis, pedidas na reserva (25/11)
    'pets': 'request_carrier',  # a pedido, em transportadora; cães de assistência sempre (25/11)
    'alcohol': 'no',            # proibido em todos os serviços (25/11)
    'cleaning_eur': 'cost',     # ao custo real, com comprovativo (25/11)
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
    # Frase da reserva: com o pagamento online ativo (PAY_MODE = 'live'), a reserva no site fica confirmada com o pagamento.
    BOOK = {
        'pt': 'No site, a reserva fica confirmada com o pagamento. Pedidos feitos por WhatsApp, telefone ou email só ficam reservados depois da nossa confirmação escrita, com o preço, e pagam-se por link de pagamento ou transferência.',
        'en': 'On the website, your booking is confirmed when you pay. Requests made by WhatsApp, phone or email are only booked once we confirm them in writing, with the price, and are paid by payment link or bank transfer.',
        'es': 'En la web, la reserva queda confirmada con el pago. Las solicitudes hechas por WhatsApp, teléfono o email solo quedan reservadas tras nuestra confirmación por escrito, con el precio, y se pagan por enlace de pago o transferencia.',
        'fr': "Sur le site, la réservation est confirmée par le paiement. Les demandes faites par WhatsApp, téléphone ou email ne sont réservées qu'après notre confirmation écrite, avec le prix, et se paient par lien de paiement ou virement.",
    }
    OLD = {
        'pt': 'Um pedido feito pelo site, WhatsApp, telefone ou email só fica reservado depois de o confirmarmos por escrito, com o preço.',
        'en': 'A request made through the website, WhatsApp, phone or email is only booked once we confirm it in writing, with the price.',
        'es': 'Una solicitud hecha por la web, WhatsApp, teléfono o email solo queda reservada cuando la confirmamos por escrito, con el precio.',
        'fr': "Une demande faite par le site, WhatsApp, téléphone ou email n'est réservée qu'après notre confirmation écrite, avec le prix.",
    }
    booking = BOOK[lang] if PAY_MODE == 'live' else OLD[lang]
    ex = f'<h2>{EXTRAS_H[lang]}</h2><ul>' + ''.join(f'<li>{x}</li>' for x in extras_items(lang)) + '</ul>'
    if lang == 'pt':
        pay = {'full': 'O pagamento total é feito na reserva.', 'deposit': f'Na reserva paga-se um sinal de {_v("deposit_pct")} % do preço; o restante no fim do serviço.',
               'after': 'O pagamento é feito no fim do serviço; pode também pagar antecipadamente.', None: '<mark>[a confirmar]</mark>'}[t['payment']]
        nightp = ('<mark>[a confirmar: suplemento noturno]</mark>' if night is None else '' if night in (False, 'extras') else
                  f'<p>Serviços entre as {night["start"]} e as {night["end"]} têm um suplemento de {night["pct"]} %.</p>')
        pets = {'request_carrier': 'Animais de estimação são aceites a pedido, em transportadora, se indicados na reserva. Cães de assistência são sempre aceites.', 'carrier': 'Animais de estimação são aceites em transportadora, se indicados na reserva.', 'request': 'Animais de estimação são aceites a pedido, se indicados na reserva.',
                'no': 'Não transportamos animais de estimação, exceto cães de assistência.', None: '<mark>[a confirmar: animais]</mark>'}[t['pets']]
        alc = {'no': 'Não é permitido consumir bebidas alcoólicas a bordo, em nenhum serviço.', 'moderate': 'Bebidas alcoólicas a bordo só com moderação.',
               'events': 'Bebidas alcoólicas a bordo só em serviços de eventos e com moderação.', None: '<mark>[a confirmar: álcool]</mark>'}[t['alcohol']]
        seat = 'sem custo' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'por {x} € cada')
        return f'''<p>Última atualização: {t["updated"]["pt"]}. Estes termos aplicam-se aos serviços da Dark Diamond Luxury, nome comercial de {co}.</p>
<h2>Reserva e confirmação</h2>
<p>{booking} Confirme que a data, a hora, o voo, as moradas, os passageiros e as malas estão corretos. Alterações sem custo até {_v("change_free_h")} h antes, sujeitas a disponibilidade.</p>
<h2>Preço</h2>
<p>O preço confirmado inclui viatura, motorista, combustível, portagens, estacionamento no aeroporto e o tempo de espera indicado abaixo{", com IVA incluído" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[IVA: a confirmar]</mark>"}. Não inclui espera extra, paragens não previstas, desvios pedidos durante a viagem nem horas extra em serviços à disposição.</p>
{ex}
<h2>Pagamento</h2>
<p>{pay} Aceitamos cartão, MB WAY e transferência{", e numerário" if t["cash"] else "" if t["cash"] is False else " <mark>[numerário: a confirmar]</mark>"}. Empresas e parceiros podem ter faturação mensal, conforme acordado.</p>
<h2>Tempo de espera</h2>
<ul><li>Chegadas ao aeroporto: {_v("wait_air")} minutos sem custo, a contar da hora real de aterragem. Acompanhamos o voo, por isso um atraso não lhe custa nada.</li>
<li>Outras recolhas: {_v("wait_other")} minutos sem custo.</li>
<li>Espera extra: por viatura, conforme os extras acima.</li></ul>
<p>Se o passageiro não aparecer nem responder depois do tempo de espera, o serviço conta como não comparência.</p>
<h2>Cancelamento</h2>
<p>Cancelamento sem penalização até {_v("cancel_free_h")} h antes ({_v("cancel_long_h")} h em longa distância, eventos e serviços à disposição). Os custos bancários e de processamento do pagamento ({_v("fee_pct")} %) não são reembolsáveis. O reembolso é feito pelo mesmo meio de pagamento, em até {_v("refund_days")} dias úteis. Se o cancelamento for da nossa parte, o reembolso é total.</p>
<ul><li>Entre {_v("cancel_free_h")} h e {_v("cancel_half_h")} h antes: 50 % do preço.</li>
<li>Com menos de {_v("cancel_half_h")} h ou não comparência: 100 % do preço.</li></ul>
<h2>Passageiros, bagagem e crianças</h2>
<p>O número de passageiros e malas indicado define a viatura. Se não couberem com segurança mais pessoas ou malas do que as indicadas, pode ser necessária outra viatura, com custo adicional. Cadeiras de criança e assentos elevatórios são obrigatórios por lei e fornecidos {seat}, se pedidos na reserva. Bagagem especial (golfe, ski, bicicletas, carrinhos de bebé) deve ser indicada na reserva. {pets}</p>
<h2>Conduta a bordo</h2>
<p>Não é permitido fumar, incluindo cigarros eletrónicos. {alc} Limpeza extraordinária ou danos causados pelos passageiros são cobrados ao custo real, com comprovativo. O motorista pode recusar ou interromper o serviço se a segurança estiver em causa.</p>
<h2>Atrasos e força maior</h2>
<p>Não somos responsáveis por atrasos causados por trânsito anormal, acidentes, condições meteorológicas, greves, encerramento de estradas ou outras causas fora do nosso controlo. Recomendamos margem suficiente para voos e comboios.</p>
<h2>Objetos esquecidos</h2>
<p>Guardamos os objetos encontrados nas viaturas durante {_v("lost_days")} dias. A devolução pode ter custo de envio ou deslocação.</p>
<h2>Seguros, dados e reclamações</h2>
<p>Viaturas e passageiros estão cobertos por seguros de responsabilidade civil e de acidentes pessoais. Os dados pessoais são tratados conforme a <a href="/pt/privacidade/">política de privacidade</a>. Pode reclamar no <a href="https://www.livroreclamacoes.pt" rel="noopener">Livro de Reclamações Eletrónico</a> ou recorrer ao <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Centro de Arbitragem de Conflitos de Consumo de Lisboa</a>. Aplica-se a lei portuguesa. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
    if lang == 'es':
        pay = {'full': 'El pago total se realiza al reservar.', 'deposit': f'Al reservar se paga una señal del {_v("deposit_pct")} % del precio; el resto al final del servicio.',
               'after': 'El pago se realiza al final del servicio; también puede pagar por adelantado.', None: '<mark>[a confirmar]</mark>'}[t['payment']]
        nightp = ('<mark>[a confirmar]</mark>' if night is None else '' if night in (False, 'extras') else
                  f'<p>Los servicios entre las {night["start"]} y las {night["end"]} tienen un suplemento del {night["pct"]} %.</p>')
        pets = {'request_carrier': 'Se aceptan mascotas bajo petición, en transportín, si se indican al reservar. Los perros de asistencia siempre son bienvenidos.', 'carrier': 'Se aceptan mascotas en transportín, si se indican al reservar.', 'request': 'Se aceptan mascotas bajo petición, si se indican al reservar.',
                'no': 'No transportamos mascotas, salvo perros de asistencia.', None: '<mark>[a confirmar]</mark>'}[t['pets']]
        alc = {'no': 'No se permite consumir bebidas alcohólicas a bordo, en ningún servicio.', 'moderate': 'Bebidas alcohólicas a bordo solo con moderación.',
               'events': 'Bebidas alcohólicas a bordo solo en servicios de eventos y con moderación.', None: '<mark>[a confirmar]</mark>'}[t['alcohol']]
        seat = 'sin coste' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'por {x} € cada una')
        return f'''<p>Última actualización: {t["updated"]["es"]}. Estos términos se aplican a los servicios de Dark Diamond Luxury, nombre comercial de {co}.</p>
<h2>Reserva y confirmación</h2>
<p>{booking} Compruebe que la fecha, la hora, el vuelo, las direcciones, los pasajeros y las maletas son correctos. Cambios sin coste hasta {_v("change_free_h")} h antes, según disponibilidad.</p>
<h2>Precio</h2>
<p>El precio confirmado incluye vehículo, chófer, combustible, peajes, aparcamiento en el aeropuerto y el tiempo de espera indicado abajo{", IVA incluido" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[IVA: a confirmar]</mark>"}. No incluye espera adicional, paradas no previstas, desvíos pedidos durante el viaje ni horas extra en servicios a disposición.</p>
{ex}
<h2>Pago</h2>
<p>{pay} Aceptamos tarjeta, MB WAY y transferencia{", y efectivo" if t["cash"] else "" if t["cash"] is False else " <mark>[efectivo: a confirmar]</mark>"}. Empresas y colaboradores pueden tener facturación mensual, según lo acordado.</p>
<h2>Tiempo de espera</h2>
<ul><li>Llegadas al aeropuerto: {_v("wait_air")} minutos sin coste, desde la hora real de aterrizaje. Seguimos el vuelo, así que un retraso no le cuesta nada.</li>
<li>Otras recogidas: {_v("wait_other")} minutos sin coste.</li>
<li>Espera adicional: por vehículo, según los extras indicados arriba.</li></ul>
<p>Si el pasajero no aparece ni responde tras el tiempo de espera, el servicio cuenta como no presentado.</p>
<h2>Cancelación</h2>
<p>Cancelación sin penalización hasta {_v("cancel_free_h")} h antes ({_v("cancel_long_h")} h en larga distancia, eventos y servicios a disposición). Los gastos bancarios y de procesamiento del pago ({_v("fee_pct")} %) no son reembolsables. El reembolso se hace por el mismo medio de pago, en un máximo de {_v("refund_days")} días hábiles. Si la cancelación es nuestra, el reembolso es total.</p>
<ul><li>Entre {_v("cancel_free_h")} h y {_v("cancel_half_h")} h antes: 50 % del precio.</li>
<li>Con menos de {_v("cancel_half_h")} h o no presentado: 100 % del precio.</li></ul>
<h2>Pasajeros, equipaje y niños</h2>
<p>El número de pasajeros y maletas indicado define el vehículo. Si no caben con seguridad más personas o maletas de las indicadas, puede ser necesario otro vehículo, con coste adicional. Las sillas infantiles y los elevadores son obligatorios por ley y se facilitan {seat}, si se piden al reservar. El equipaje especial (golf, esquí, bicicletas, cochecitos) debe indicarse al reservar. {pets}</p>
<h2>Conducta a bordo</h2>
<p>No se permite fumar, tampoco cigarrillos electrónicos. {alc} La limpieza extraordinaria o los daños causados por los pasajeros se cobran al coste real, con justificante. El chófer puede rechazar o interrumpir el servicio si la seguridad está en juego.</p>
<h2>Retrasos y fuerza mayor</h2>
<p>No somos responsables de retrasos causados por tráfico anormal, accidentes, meteorología, huelgas, cierres de carreteras u otras causas ajenas a nuestro control. Recomendamos margen suficiente para vuelos y trenes.</p>
<h2>Objetos olvidados</h2>
<p>Guardamos los objetos encontrados en los vehículos durante {_v("lost_days")} días. La devolución puede tener coste de envío o desplazamiento.</p>
<h2>Seguros, datos y reclamaciones</h2>
<p>Vehículos y pasajeros están cubiertos por seguros de responsabilidad civil y de accidentes personales. Los datos personales se tratan según la <a href="/es/privacidad/">política de privacidad</a>. Puede reclamar en el <a href="https://www.livroreclamacoes.pt" rel="noopener">Libro de Reclamaciones Electrónico</a> o acudir al <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Centro de Arbitraje de Conflictos de Consumo de Lisboa</a>. Se aplica la ley portuguesa. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
    if lang == 'fr':
        pay = {'full': 'Le paiement intégral se fait à la réservation.', 'deposit': f'À la réservation, un acompte de {_v("deposit_pct")} % du prix est demandé ; le solde à la fin du service.',
               'after': "Le paiement se fait à la fin du service ; vous pouvez aussi payer à l'avance.", None: '<mark>[à confirmer]</mark>'}[t['payment']]
        nightp = ('<mark>[à confirmer]</mark>' if night is None else '' if night in (False, 'extras') else
                  f"<p>Les services entre {night['start']} et {night['end']} comportent un supplément de {night['pct']} %.</p>")
        pets = {'request_carrier': "Les animaux sont acceptés sur demande, en caisse de transport, s'ils sont indiqués à la réservation. Les chiens d'assistance sont toujours acceptés.", 'carrier': "Les animaux sont acceptés en caisse de transport, s'ils sont indiqués à la réservation.", 'request': "Les animaux sont acceptés sur demande, s'ils sont indiqués à la réservation.",
                'no': "Nous ne transportons pas d'animaux, à l'exception des chiens d'assistance.", None: '<mark>[à confirmer]</mark>'}[t['pets']]
        alc = {'no': "La consommation d'alcool à bord n'est autorisée dans aucun service.", 'moderate': 'Alcool à bord avec modération uniquement.',
               'events': 'Alcool à bord uniquement pour les services événementiels, avec modération.', None: '<mark>[à confirmer]</mark>'}[t['alcohol']]
        seat = 'sans frais' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'à {x} € pièce')
        return f"""<p>Dernière mise à jour : {t["updated"]["fr"]}. Ces conditions s'appliquent aux services de Dark Diamond Luxury, nom commercial de {co}.</p>
<h2>Réservation et confirmation</h2>
<p>{booking} Vérifiez que la date, l'heure, le vol, les adresses, les passagers et les bagages sont corrects. Modifications sans frais jusqu'à {_v("change_free_h")} h avant, selon disponibilité.</p>
<h2>Prix</h2>
<p>Le prix confirmé comprend le véhicule, le chauffeur, le carburant, les péages, le parking à l'aéroport et le temps d'attente indiqué ci-dessous{", TVA comprise" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[TVA : à confirmer]</mark>"}. Il ne comprend pas l'attente supplémentaire, les arrêts non prévus, les détours demandés en cours de route ni les heures supplémentaires des services à disposition.</p>
{ex}
<h2>Paiement</h2>
<p>{pay} Nous acceptons la carte, MB WAY et le virement{", et les espèces" if t["cash"] else "" if t["cash"] is False else " <mark>[espèces : à confirmer]</mark>"}. Les entreprises et partenaires peuvent être facturés mensuellement, selon accord.</p>
<h2>Temps d'attente</h2>
<ul><li>Arrivées à l'aéroport : {_v("wait_air")} minutes sans frais, à compter de l'heure réelle d'atterrissage. Nous suivons votre vol : un retard ne vous coûte rien.</li>
<li>Autres prises en charge : {_v("wait_other")} minutes sans frais.</li>
<li>Attente supplémentaire : par véhicule, selon les extras ci-dessus.</li></ul>
<p>Si le passager ne se présente pas et ne répond pas après le temps d'attente, le service compte comme une non-présentation.</p>
<h2>Annulation</h2>
<p>Annulation sans pénalité jusqu'à {_v("cancel_free_h")} h avant ({_v("cancel_long_h")} h pour la longue distance, les événements et les services à disposition). Les frais bancaires et de traitement du paiement ({_v("fee_pct")} %) ne sont pas remboursables. Le remboursement se fait par le moyen de paiement d'origine, sous {_v("refund_days")} jours ouvrés. Si l'annulation vient de nous, le remboursement est intégral.</p>
<ul><li>Entre {_v("cancel_free_h")} h et {_v("cancel_half_h")} h avant : 50 % du prix.</li>
<li>Moins de {_v("cancel_half_h")} h avant, ou non-présentation : 100 % du prix.</li></ul>
<h2>Passagers, bagages et enfants</h2>
<p>Le nombre de passagers et de valises indiqué détermine le véhicule. Si plus de personnes ou de valises que prévu ne tiennent pas en sécurité, un autre véhicule peut être nécessaire, avec un coût supplémentaire. Les sièges enfants et rehausseurs sont obligatoires par la loi et fournis {seat}, s'ils sont demandés à la réservation. Les bagages spéciaux (golf, ski, vélos, poussettes) doivent être signalés à la réservation. {pets}</p>
<h2>Conduite à bord</h2>
<p>Interdiction de fumer, cigarettes électroniques comprises. {alc} Le nettoyage extraordinaire ou les dégâts causés par les passagers sont facturés au coût réel, sur justificatif. Le chauffeur peut refuser ou interrompre le service si la sécurité est en jeu.</p>
<h2>Retards et force majeure</h2>
<p>Nous ne sommes pas responsables des retards dus à un trafic anormal, des accidents, la météo, des grèves, des routes fermées ou d'autres causes hors de notre contrôle. Prévoyez une marge suffisante pour les vols et les trains.</p>
<h2>Objets oubliés</h2>
<p>Les objets trouvés dans nos véhicules sont conservés {_v("lost_days")} jours. Leur restitution peut entraîner des frais d'envoi ou de déplacement.</p>
<h2>Assurances, données et réclamations</h2>
<p>Véhicules et passagers sont couverts par des assurances de responsabilité civile et d'accidents personnels. Les données personnelles sont traitées selon la <a href="/fr/confidentialite/">politique de confidentialité</a>. Vous pouvez déposer une réclamation sur le <a href="https://www.livroreclamacoes.pt" rel="noopener">Livre de réclamations électronique</a> ou saisir le <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Centre d'arbitrage des conflits de consommation de Lisbonne</a>. Le droit portugais s'applique. Contact : <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""
    pay = {'full': 'Full payment is made when you book.', 'deposit': f'A deposit of {_v("deposit_pct")}% is paid when you book; the balance at the end of the service.',
           'after': 'Payment is made at the end of the service; you can also pay in advance.', None: '<mark>[to confirm]</mark>'}[t['payment']]
    nightp = ('<mark>[to confirm]</mark>' if night is None else '' if night in (False, 'extras') else
              f'<p>Services between {night["start"]} and {night["end"]} carry a {night["pct"]}% surcharge.</p>')
    pets = {'request_carrier': 'Pets are accepted on request, in a carrier, if mentioned when booking. Assistance dogs are always welcome.', 'carrier': 'Pets are welcome in a carrier, if mentioned when booking.', 'request': 'Pets are accepted on request, if mentioned when booking.',
            'no': 'We do not carry pets, except assistance dogs.', None: '<mark>[to confirm]</mark>'}[t['pets']]
    alc = {'no': 'Alcohol may not be consumed on board, on any service.', 'moderate': 'Alcohol on board in moderation only.',
           'events': 'Alcohol on board only on event services, in moderation.', None: '<mark>[to confirm]</mark>'}[t['alcohol']]
    seat = 'free of charge' if t['child_seat_eur'] == 0 else _v('child_seat_eur', lambda x: f'at €{x} each')
    return f'''<p>Last updated: {t["updated"]["en"]}. These terms apply to services provided by Dark Diamond Luxury, the trading name of {co}.</p>
<h2>Booking and confirmation</h2>
<p>{booking} Please check that the date, time, flight, addresses, passengers and luggage are correct. Changes are free up to {_v("change_free_h")} h before, subject to availability.</p>
<h2>Price</h2>
<p>The confirmed price includes vehicle, driver, fuel, tolls, airport parking and the waiting time below{", VAT included" if t["vat_included"] else "" if t["vat_included"] is False else " <mark>[VAT: to confirm]</mark>"}. It does not include extra waiting, unplanned stops, detours requested during the journey or extra hours on chauffeur-at-disposal services.</p>
{ex}
<h2>Payment</h2>
<p>{pay} We accept card, MB WAY and bank transfer{", and cash" if t["cash"] else "" if t["cash"] is False else " <mark>[cash: to confirm]</mark>"}. Companies and partners may be invoiced monthly, as agreed.</p>
<h2>Waiting time</h2>
<ul><li>Airport arrivals: {_v("wait_air")} minutes free, from the actual landing time. We track your flight, so a delay costs you nothing.</li>
<li>Other pick-ups: {_v("wait_other")} minutes free.</li>
<li>Extra waiting: per vehicle, as set out in Extras above.</li></ul>
<p>If the passenger does not appear or respond after the waiting time, the service counts as a no-show.</p>
<h2>Cancellation</h2>
<p>Cancellation without penalty up to {_v("cancel_free_h")} h before ({_v("cancel_long_h")} h for long distance, events and chauffeur-at-disposal services). Bank and payment processing costs ({_v("fee_pct")}%) are not refundable. Refunds are made to the original payment method within {_v("refund_days")} working days. If we cancel, the refund is in full.</p>
<ul><li>Between {_v("cancel_free_h")} h and {_v("cancel_half_h")} h before: 50% of the price.</li>
<li>Less than {_v("cancel_half_h")} h before, or no-show: 100% of the price.</li></ul>
<h2>Passengers, luggage and children</h2>
<p>The number of passengers and bags you give sets the vehicle. If more people or bags turn up than booked and they do not fit safely, another vehicle may be needed at extra cost. Child seats and boosters are required by law and provided {seat} when requested at booking. Special luggage (golf, ski, bicycles, pushchairs) should be mentioned when booking. {pets}</p>
<h2>Conduct on board</h2>
<p>No smoking, including e-cigarettes. {alc} Extraordinary cleaning or damage caused by passengers is charged at actual cost, with proof. The driver may refuse or stop the service if safety is at risk.</p>
<h2>Delays and force majeure</h2>
<p>We are not liable for delays caused by abnormal traffic, accidents, weather, strikes, road closures or other causes beyond our control. Please allow enough time for flights and trains.</p>
<h2>Lost property</h2>
<p>Items found in our vehicles are kept for {_v("lost_days")} days. Returning them may involve delivery or travel costs.</p>
<h2>Insurance, data and complaints</h2>
<p>Vehicles and passengers are covered by third-party liability and personal accident insurance. Personal data is handled under our <a href="/privacy/">privacy policy</a>. You can file a complaint in the <a href="https://www.livroreclamacoes.pt" rel="noopener">Electronic Complaints Book</a> or refer to the <a href="https://www.centroarbitragemlisboa.pt" rel="noopener">Lisbon Consumer Arbitration Centre</a>. Portuguese law applies. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
