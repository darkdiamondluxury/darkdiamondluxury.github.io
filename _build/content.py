# Textos das páginas interiores, em EN / PT / ES.
# Onde falta um dado da empresa aparece <span class="todo">[…]</span> (a dourado) para ser fácil de encontrar.
from config import COVERAGE, DESTS, EMAIL, LEGAL, PHONES

TODO = lambda s: f'<span class="todo">[{s}]</span>'  # noqa: E731
PH = ' · '.join(PHONES)
ADDR = f"{LEGAL['street']}, {LEGAL['postcode']} {LEGAL['city']}"

PAGES = {}

# =====================================================================================
# AGÊNCIAS E PARCEIROS
# =====================================================================================
PAGES['agencies'] = {
 'en': dict(
  title='Ground transportation partner in Portugal for travel agencies · Dark Diamond Luxury',
  desc='Private transfers, tours and chauffeur services for travel agencies, tour operators, DMCs and cruise lines in Portugal, Spain and France. Registered with Turismo de Portugal, RNAAT 682/2022.',
  crumb='Agencies and partners', h1='Your ground partner in Portugal.',
  lead='Private transfers, tours and chauffeured services for travel agencies, tour operators, DMCs and cruise lines. Portugal, Spain and France.',
  subject='Partnership request / rates', ctas=[('mail', 'Request our rates'), ('tel', 'Call us')],
  blocks=[
   dict(type='split', h='Why agencies work with us', ticks=[
     '<b>Registered with Turismo de Portugal.</b> Licensed tourism activity operator, RNAAT no. 682/2022.',
     '<b>Insured.</b> Civil liability and personal accident insurance in force.',
     '<b>Flight tracking, meet and greet.</b> Your client is met at arrivals with a name sign, whatever time the flight lands.',
     '<b>A direct line.</b> You speak to the people who plan and dispatch the service, not a call centre.',
     '<b>Written confirmation.</b> Every booking is confirmed in writing, and the driver\'s details are sent before the service.']),
   dict(type='split', bg='bone', h='Where we operate', p=['Based in Lisbon, with regular services across Portugal and long-distance transfers to Spain and France.'], ticks=[
     'Lisbon airport (LIS), city hotels and the cruise terminals', 'Sintra, Cascais and the Estoril coast', 'Comporta and the Alentejo coast',
     'Évora and the Alentejo', 'Fátima, Óbidos, Nazaré and Batalha', 'Porto and the Douro valley', 'The Algarve', 'Spain and France, on request']),
   dict(type='split', h='How it works', steps=[
     ('Send the booking', 'By email or WhatsApp: passenger name, date, flight or pick-up time, number of passengers and luggage.'),
     ('We confirm', f'Availability and price confirmed in writing {TODO("response time, e.g. within 2 hours")}.'),
     ('Before the service', 'You receive the driver\'s name, phone number and vehicle.'),
     ('On the day', 'Meet and greet, flight tracking and direct contact with the driver. If anything changes, we tell you straight away.'),
     ('Invoicing', f'{TODO("invoicing terms, e.g. monthly invoice, bank transfer")} Invoices issued by {LEGAL["name"]}, VAT PT{LEGAL["nipc"]}.')]),
   dict(type='split', bg='alt', h='Services', ticks=[
     'Airport and cruise port transfers', 'Chauffeur at disposal, by the hour or by the day', 'Private tours and day trips',
     'Events, weddings and groups', 'Long distance within Portugal and to Spain and France']),
   dict(type='split', h='Company details', rows=[
     ('Trading name', 'Dark Diamond Luxury'), ('Legal name', LEGAL['name']), ('VAT number (NIPC)', LEGAL['nipc']),
     ('Registered office', ADDR), ('Tourism registration', f'RNAAT {LEGAL["rnaat"]}'),
     ('Insurance', 'Civil liability · Personal accident'), ('Coverage', COVERAGE['en']), ('Contact', f'{EMAIL}<br>{PH}')]),
   dict(type='cta', h='Let\'s work together.', p='Send us your usual routes and volumes and we will prepare a rate sheet for your agency.',
        ctas=[('mail', 'Request our rates'), ('tel', 'Call us')]),
  ]),
 'pt': dict(
  title='Parceiro de transporte em Portugal para agências de viagens · Dark Diamond Luxury',
  desc='Transfers privados, tours e motorista para agências de viagens, operadores turísticos, DMCs e linhas de cruzeiro em Portugal, Espanha e França. Registada no Turismo de Portugal, RNAAT 682/2022.',
  crumb='Agências e parceiros', h1='O seu parceiro em terra, em Portugal.',
  lead='Transfers privados, tours e serviços com motorista para agências de viagens, operadores turísticos, DMCs e linhas de cruzeiro. Portugal, Espanha e França.',
  subject='Pedido de parceria / tabela de preços', ctas=[('mail', 'Pedir tabela de preços'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Porque trabalham connosco', ticks=[
     '<b>Registados no Turismo de Portugal.</b> Agente de animação turística, RNAAT n.º 682/2022.',
     '<b>Com seguro.</b> Seguros de responsabilidade civil e de acidentes pessoais em vigor.',
     '<b>Seguimento de voos e receção com placa.</b> O seu cliente é recebido nas chegadas com o nome, à hora a que o voo aterrar.',
     '<b>Contacto direto.</b> Fala com quem planeia e despacha o serviço, não com um call center.',
     '<b>Confirmação por escrito.</b> Cada reserva é confirmada por escrito e os dados do motorista seguem antes do serviço.']),
   dict(type='split', bg='bone', h='Onde trabalhamos', p=['Com base em Lisboa, serviços regulares em todo o país e transfers de longa distância para Espanha e França.'], ticks=[
     'Aeroporto de Lisboa, hotéis da cidade e terminais de cruzeiros', 'Sintra, Cascais e a linha do Estoril', 'Comporta e o litoral alentejano',
     'Évora e o Alentejo', 'Fátima, Óbidos, Nazaré e Batalha', 'Porto e o vale do Douro', 'Algarve', 'Espanha e França, por pedido']),
   dict(type='split', h='Como funciona', steps=[
     ('Envie a reserva', 'Por email ou WhatsApp: nome do passageiro, data, voo ou hora de recolha, número de passageiros e malas.'),
     ('Confirmamos', f'Disponibilidade e preço confirmados por escrito {TODO("tempo de resposta, ex.: em menos de 2 horas")}.'),
     ('Antes do serviço', 'Recebe o nome e o telefone do motorista e o veículo.'),
     ('No dia', 'Receção com placa, seguimento do voo e contacto direto com o motorista. Se algo mudar, avisamos de imediato.'),
     ('Faturação', f'{TODO("condições de faturação, ex.: fatura mensal, transferência")} Faturas emitidas por {LEGAL["name"]}, NIPC {LEGAL["nipc"]}.')]),
   dict(type='split', bg='alt', h='Serviços', ticks=[
     'Transfers de aeroporto e de porto de cruzeiros', 'Motorista à disposição, à hora ou ao dia', 'Tours privados e passeios de um dia',
     'Eventos, casamentos e grupos', 'Longa distância em Portugal e para Espanha e França']),
   dict(type='split', h='Dados da empresa', rows=[
     ('Nome comercial', 'Dark Diamond Luxury'), ('Firma', LEGAL['name']), ('NIPC', LEGAL['nipc']),
     ('Sede', ADDR), ('Registo de turismo', f'RNAAT {LEGAL["rnaat"]}'),
     ('Seguros', 'Responsabilidade civil · Acidentes pessoais'), ('Cobertura', COVERAGE['pt']), ('Contacto', f'{EMAIL}<br>{PH}')]),
   dict(type='cta', h='Vamos trabalhar juntos.', p='Envie-nos as rotas e volumes habituais e preparamos uma tabela de preços para a sua agência.',
        ctas=[('mail', 'Pedir tabela de preços'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Partner de transporte en Portugal para agencias de viajes · Dark Diamond Luxury',
  desc='Traslados privados, tours y chófer para agencias de viajes, turoperadores, DMCs y navieras en Portugal, España y Francia. Registrada en Turismo de Portugal, RNAAT 682/2022.',
  crumb='Agencias y partners', h1='Su partner en tierra, en Portugal.',
  lead='Traslados privados, tours y servicios con chófer para agencias de viajes, turoperadores, DMCs y navieras. Portugal, España y Francia.',
  subject='Solicitud de colaboración / tarifas', ctas=[('mail', 'Solicitar tarifas'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='Por qué trabajan con nosotros', ticks=[
     '<b>Registrados en Turismo de Portugal.</b> Agente de animación turística, RNAAT n.º 682/2022.',
     '<b>Asegurados.</b> Seguros de responsabilidad civil y de accidentes personales en vigor.',
     '<b>Seguimiento de vuelos y recepción con cartel.</b> Su cliente es recibido en llegadas con su nombre, a la hora a la que aterrice el vuelo.',
     '<b>Contacto directo.</b> Habla con quien planifica y asigna el servicio, no con un call center.',
     '<b>Confirmación por escrito.</b> Cada reserva se confirma por escrito y los datos del chófer se envían antes del servicio.']),
   dict(type='split', bg='bone', h='Dónde trabajamos', p=['Con base en Lisboa, servicios regulares en todo Portugal y traslados de larga distancia a España y Francia.'], ticks=[
     'Aeropuerto de Lisboa, hoteles de la ciudad y terminales de cruceros', 'Sintra, Cascais y la costa de Estoril', 'Comporta y la costa del Alentejo',
     'Évora y el Alentejo', 'Fátima, Óbidos, Nazaré y Batalha', 'Oporto y el valle del Duero', 'El Algarve', 'España y Francia, bajo petición']),
   dict(type='split', h='Cómo funciona', steps=[
     ('Envíe la reserva', 'Por email o WhatsApp: nombre del pasajero, fecha, vuelo u hora de recogida, número de pasajeros y maletas.'),
     ('Confirmamos', f'Disponibilidad y precio confirmados por escrito {TODO("tiempo de respuesta, p. ej. en menos de 2 horas")}.'),
     ('Antes del servicio', 'Recibe el nombre y el teléfono del chófer y el vehículo.'),
     ('El día del servicio', 'Recepción con cartel, seguimiento del vuelo y contacto directo con el chófer. Si algo cambia, le avisamos de inmediato.'),
     ('Facturación', f'{TODO("condiciones de facturación, p. ej. factura mensual, transferencia")} Facturas emitidas por {LEGAL["name"]}, NIF PT{LEGAL["nipc"]}.')]),
   dict(type='split', bg='alt', h='Servicios', ticks=[
     'Traslados de aeropuerto y de puerto de cruceros', 'Chófer a disposición, por horas o por días', 'Tours privados y excursiones de un día',
     'Eventos, bodas y grupos', 'Larga distancia en Portugal y a España y Francia']),
   dict(type='split', h='Datos de la empresa', rows=[
     ('Nombre comercial', 'Dark Diamond Luxury'), ('Razón social', LEGAL['name']), ('NIF (NIPC)', LEGAL['nipc']),
     ('Domicilio social', ADDR), ('Registro de turismo', f'RNAAT {LEGAL["rnaat"]}'),
     ('Seguros', 'Responsabilidad civil · Accidentes personales'), ('Cobertura', COVERAGE['es']), ('Contacto', f'{EMAIL}<br>{PH}')]),
   dict(type='cta', h='Trabajemos juntos.', p='Envíenos sus rutas y volúmenes habituales y preparamos una tabla de tarifas para su agencia.',
        ctas=[('mail', 'Solicitar tarifas'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# AEROPORTO
# =====================================================================================
TIMES = [('Baixa · Chiado', '20 min'), ('Belém', '25 min'), ('Parque das Nações', '10 min'), ('Cascais', '35 min'), ('Sintra', '35 min'),
         ('Comporta', '1h15'), ('Évora', '1h30'), ('Fátima', '1h30'), ('Algarve', '2h45'), ('Porto', '3h')]
PAGES['airport'] = {
 'en': dict(
  title='Lisbon Airport Transfer · Private meet and greet · Dark Diamond Luxury',
  desc='Private transfer from Lisbon Airport (LIS) to your hotel or anywhere in Portugal. Flight tracking, meet and greet at arrivals with your name, price confirmed before you book.',
  crumb='Lisbon airport transfer', h1='Lisbon airport transfers, met by name.', img='plane',
  lead='Private transfer from Lisbon Humberto Delgado Airport (LIS) to your hotel, home or anywhere in Portugal. Your driver tracks the flight and waits at arrivals with your name.',
  ctas=[('book', 'Book airport transfer'), ('tel', 'Call us')],
  blocks=[
   dict(type='split', h='How it works', steps=[
     ('Book', 'Send us your flight number, destination and number of passengers and bags. We reply with confirmation and price.'),
     ('We track your flight', 'If the flight lands early or late, your driver adjusts to the real landing time.'),
     ('Meet at arrivals', 'Your driver waits in the arrivals hall of Terminal 1 or 2, holding a sign with your name.'),
     ('Straight to your door', 'Help with luggage and a direct ride, with no shared stops.')]),
   dict(type='split', bg='bone', h='Journey times from the airport', rows=TIMES, after=['Indicative times without traffic.']),
   dict(type='split', h='Good to know', ticks=[
     'A private vehicle just for your group: no shared shuttles.', 'Child seats on request: tell us the children\'s ages when booking.',
     'Departures too: pick-up at your hotel at the time you choose.', 'Price confirmed in writing before you book.'], related=DESTS),
   dict(type='cta', h='Landing soon?', p='Send us your flight and destination. We reply with confirmation and price.', ctas=[('book', 'Book airport transfer'), ('tel', 'Call us')]),
  ]),
 'pt': dict(
  title='Transfer do Aeroporto de Lisboa · Receção com placa · Dark Diamond Luxury',
  desc='Transfer privado do aeroporto de Lisboa para o seu hotel ou para qualquer ponto do país. Seguimento do voo, receção nas chegadas com o seu nome, preço confirmado antes de reservar.',
  crumb='Transfer aeroporto de Lisboa', h1='Transfers do aeroporto de Lisboa, recebido pelo nome.', img='plane',
  lead='Transfer privado do Aeroporto Humberto Delgado (LIS) para o seu hotel, casa ou qualquer ponto do país. O motorista acompanha o voo e espera nas chegadas com o seu nome.',
  ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Como funciona', steps=[
     ('Reserve', 'Envie-nos o número do voo, o destino e o número de passageiros e malas. Respondemos com a confirmação e o preço.'),
     ('Acompanhamos o voo', 'Se o voo chegar mais cedo ou mais tarde, o motorista ajusta-se à hora real de aterragem.'),
     ('Receção nas chegadas', 'O motorista espera na zona de chegadas do Terminal 1 ou 2, com uma placa com o seu nome.'),
     ('Direto à porta', 'Ajuda com as malas e viagem direta, sem paragens partilhadas.')]),
   dict(type='split', bg='bone', h='Tempos de viagem a partir do aeroporto', rows=TIMES, after=['Tempos indicativos, sem trânsito.']),
   dict(type='split', h='Bom saber', ticks=[
     'Veículo privado só para o seu grupo: sem shuttles partilhados.', 'Cadeiras de criança por pedido: indique a idade das crianças ao reservar.',
     'Também para partidas: recolha no hotel à hora que escolher.', 'Preço confirmado por escrito antes de reservar.'], related=DESTS),
   dict(type='cta', h='Vai aterrar em breve?', p='Envie-nos o voo e o destino. Respondemos com a confirmação e o preço.', ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Traslado Aeropuerto de Lisboa · Recepción con cartel · Dark Diamond Luxury',
  desc='Traslado privado desde el aeropuerto de Lisboa a su hotel o a cualquier punto de Portugal. Seguimiento del vuelo, recepción en llegadas con su nombre y precio confirmado antes de reservar.',
  crumb='Traslado aeropuerto de Lisboa', h1='Traslados desde el aeropuerto de Lisboa, con su nombre.', img='plane',
  lead='Traslado privado desde el Aeropuerto Humberto Delgado (LIS) a su hotel, su casa o cualquier punto de Portugal. El chófer sigue el vuelo y le espera en llegadas con su nombre.',
  ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='Cómo funciona', steps=[
     ('Reserve', 'Envíenos el número de vuelo, el destino y el número de pasajeros y maletas. Le respondemos con la confirmación y el precio.'),
     ('Seguimos su vuelo', 'Si el vuelo llega antes o después, el chófer se ajusta a la hora real de aterrizaje.'),
     ('Recepción en llegadas', 'El chófer le espera en la zona de llegadas de la Terminal 1 o 2, con un cartel con su nombre.'),
     ('Directo a su puerta', 'Ayuda con las maletas y viaje directo, sin paradas compartidas.')]),
   dict(type='split', bg='bone', h='Tiempos de viaje desde el aeropuerto', rows=TIMES, after=['Tiempos orientativos, sin tráfico.']),
   dict(type='split', h='Conviene saber', ticks=[
     'Vehículo privado solo para su grupo: sin shuttles compartidos.', 'Sillas infantiles bajo petición: indíquenos la edad de los niños al reservar.',
     'También para salidas: recogida en su hotel a la hora que elija.', 'Precio confirmado por escrito antes de reservar.'], related=DESTS),
   dict(type='cta', h='¿Aterriza pronto?', p='Envíenos el vuelo y el destino. Le respondemos con la confirmación y el precio.', ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# CRUZEIROS
# =====================================================================================
PAGES['cruise'] = {
 'en': dict(
  title='Lisbon Cruise Port Transfers and Private Shore Excursions · Dark Diamond Luxury',
  desc='Private transfers between the Lisbon cruise terminals, the airport and hotels, plus private shore excursions to Sintra, Cascais and Lisbon, planned around your all-aboard time.',
  crumb='Lisbon cruise terminal', h1='Lisbon cruise port transfers and shore excursions.', img='bridge',
  lead='From the ship to the airport, your hotel or a private tour, timed around your port call. For passengers, agencies and cruise lines.',
  ctas=[('book', 'Book a port transfer'), ('agencies', 'For agencies and cruise lines')],
  blocks=[
   dict(type='split', h='What we do at the port', ticks=[
     '<b>Port and airport.</b> Transfers on embarkation and disembarkation day.', '<b>Port and hotel.</b> For stays before or after the cruise.',
     '<b>Private shore excursions.</b> Lisbon, Sintra, Cascais or Fátima, with a driver who plans the return around the all-aboard time.',
     '<b>Groups.</b> Vans for families and small groups, with room for luggage.']),
   dict(type='split', bg='bone', h='Lisbon\'s cruise terminals', p=[
     'Most ships dock at the Lisbon Cruise Terminal, next to Santa Apolónia and Alfama, close to the city centre and around 20 minutes from the airport.',
     'Some ships use the Alcântara or Rocha Conde de Óbidos terminals, further west. Tell us the ship\'s name and we will meet you at the right place.']),
   dict(type='split', h='Back on board on time', p=[
     'On shore excursions we plan the day backwards from the all-aboard time, with a margin for traffic. You keep the driver\'s number and the driver keeps yours.']),
   dict(type='cta', h='Docking in Lisbon?', p='Tell us the ship, the date and what you would like to do. We reply with a plan and a price.', ctas=[('book', 'Book a port transfer'), ('tel', 'Call us')]),
  ]),
 'pt': dict(
  title='Transfers no Terminal de Cruzeiros de Lisboa e excursões privadas · Dark Diamond Luxury',
  desc='Transfers privados entre os terminais de cruzeiros de Lisboa, o aeroporto e os hotéis, e excursões privadas a Sintra, Cascais e Lisboa, planeadas em função da hora de regresso ao navio.',
  crumb='Terminal de cruzeiros de Lisboa', h1='Transfers no porto de cruzeiros de Lisboa e excursões em terra.', img='bridge',
  lead='Do navio para o aeroporto, para o hotel ou para um tour privado, ao ritmo da escala. Para passageiros, agências e linhas de cruzeiro.',
  ctas=[('book', 'Reservar transfer'), ('agencies', 'Para agências e linhas de cruzeiro')],
  blocks=[
   dict(type='split', h='O que fazemos no porto', ticks=[
     '<b>Porto e aeroporto.</b> Transfers no dia de embarque e de desembarque.', '<b>Porto e hotel.</b> Para estadias antes ou depois do cruzeiro.',
     '<b>Excursões privadas em terra.</b> Lisboa, Sintra, Cascais ou Fátima, com um motorista que planeia o regresso em função da hora de embarque.',
     '<b>Grupos.</b> Carrinhas para famílias e pequenos grupos, com espaço para as malas.']),
   dict(type='split', bg='bone', h='Os terminais de cruzeiros de Lisboa', p=[
     'A maioria dos navios atraca no Terminal de Cruzeiros de Lisboa, junto a Santa Apolónia e Alfama, perto do centro e a cerca de 20 minutos do aeroporto.',
     'Alguns navios usam os terminais de Alcântara ou da Rocha Conde de Óbidos, mais a oeste. Diga-nos o nome do navio e esperamos no sítio certo.']),
   dict(type='split', h='De volta ao navio a horas', p=[
     'Nas excursões em terra planeamos o dia a partir da hora de regresso a bordo, com margem para o trânsito. Fica com o número do motorista e ele com o seu.']),
   dict(type='cta', h='Vai fazer escala em Lisboa?', p='Diga-nos o navio, a data e o que gostaria de fazer. Respondemos com um plano e um preço.', ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Traslados en la Terminal de Cruceros de Lisboa y excursiones privadas · Dark Diamond Luxury',
  desc='Traslados privados entre las terminales de cruceros de Lisboa, el aeropuerto y los hoteles, y excursiones privadas a Sintra, Cascais y Lisboa, planificadas según la hora de regreso al barco.',
  crumb='Terminal de cruceros de Lisboa', h1='Traslados en el puerto de cruceros de Lisboa y excursiones en tierra.', img='bridge',
  lead='Del barco al aeropuerto, al hotel o a un tour privado, al ritmo de la escala. Para pasajeros, agencias y navieras.',
  ctas=[('book', 'Reservar traslado'), ('agencies', 'Para agencias y navieras')],
  blocks=[
   dict(type='split', h='Qué hacemos en el puerto', ticks=[
     '<b>Puerto y aeropuerto.</b> Traslados el día de embarque y de desembarque.', '<b>Puerto y hotel.</b> Para estancias antes o después del crucero.',
     '<b>Excursiones privadas en tierra.</b> Lisboa, Sintra, Cascais o Fátima, con un chófer que planifica el regreso según la hora de embarque.',
     '<b>Grupos.</b> Furgonetas para familias y grupos pequeños, con espacio para el equipaje.']),
   dict(type='split', bg='bone', h='Las terminales de cruceros de Lisboa', p=[
     'La mayoría de los barcos atraca en la Terminal de Cruceros de Lisboa, junto a Santa Apolónia y Alfama, cerca del centro y a unos 20 minutos del aeropuerto.',
     'Algunos barcos utilizan las terminales de Alcântara o Rocha Conde de Óbidos, más al oeste. Díganos el nombre del barco y le esperamos en el lugar correcto.']),
   dict(type='split', h='De vuelta al barco a tiempo', p=[
     'En las excursiones en tierra planificamos el día a partir de la hora de regreso a bordo, con margen para el tráfico. Usted tiene el número del chófer y él el suyo.']),
   dict(type='cta', h='¿Hace escala en Lisboa?', p='Díganos el barco, la fecha y lo que le gustaría hacer. Le respondemos con un plan y un precio.', ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# DESTINOS (mesma estrutura para todos; muda o conteúdo)
# =====================================================================================
# km e tempo aproximados a partir do aeroporto de Lisboa
D = {
 'd-sintra': dict(name='Sintra', km=35, time='35 min', img='leather',
  en=dict(lead='Palaces in the hills, an hour from the airport at most. Go straight to your hotel in Sintra or spend the day there with your driver.',
          about=['Sintra\'s cultural landscape is a UNESCO World Heritage Site: the Pena Palace, Quinta da Regaleira, the Moorish Castle and Monserrate sit among forested hills above the town.',
                 'The historic centre has narrow, busy roads. Your driver drops you as close to each entrance as access allows and picks you up where agreed.'],
          see=['Pena Palace', 'Quinta da Regaleira', 'Moorish Castle', 'Monserrate Palace'], combo='Combine with Cabo da Roca and Cascais on the way back.'),
  pt=dict(lead='Palácios na serra, a menos de uma hora do aeroporto. Vá direto para o seu hotel em Sintra ou passe lá o dia com o seu motorista.',
          about=['A paisagem cultural de Sintra é Património Mundial da UNESCO: o Palácio da Pena, a Quinta da Regaleira, o Castelo dos Mouros e Monserrate ficam entre as encostas arborizadas da serra.',
                 'O centro histórico tem estradas estreitas e movimentadas. O motorista deixa-o o mais perto possível de cada entrada e volta a buscá-lo onde combinarem.'],
          see=['Palácio da Pena', 'Quinta da Regaleira', 'Castelo dos Mouros', 'Palácio de Monserrate'], combo='Combine com o Cabo da Roca e Cascais no regresso.'),
  es=dict(lead='Palacios en la sierra, a menos de una hora del aeropuerto. Vaya directo a su hotel en Sintra o pase allí el día con su chófer.',
          about=['El paisaje cultural de Sintra es Patrimonio Mundial de la UNESCO: el Palacio da Pena, la Quinta da Regaleira, el Castillo de los Moros y Monserrate se reparten por las laderas boscosas de la sierra.',
                 'El centro histórico tiene calles estrechas y concurridas. El chófer le deja lo más cerca posible de cada entrada y le recoge donde acuerden.'],
          see=['Palacio da Pena', 'Quinta da Regaleira', 'Castillo de los Moros', 'Palacio de Monserrate'], combo='Combínelo con el Cabo da Roca y Cascais a la vuelta.')),
 'd-cascais': dict(name='Cascais', km=40, time='35 min', img='van',
  en=dict(lead='The seaside town west of Lisbon, along the Estoril coast. A direct transfer to your hotel or a relaxed day by the sea.',
          about=['Cascais grew from a fishing village into a resort town, with a marina, beaches and a walkable old centre. The road along the Estoril coast is one of the most scenic in the Lisbon area.',
                 'From Cascais it is a short drive to Boca do Inferno and Cabo da Roca, the westernmost point of mainland Europe.'],
          see=['Cascais old town and marina', 'Boca do Inferno', 'Cabo da Roca', 'Estoril and its casino'], combo='Combine with Sintra for a full day west of Lisbon.'),
  pt=dict(lead='A vila à beira-mar a oeste de Lisboa, na linha do Estoril. Transfer direto para o hotel ou um dia tranquilo junto ao mar.',
          about=['Cascais passou de vila piscatória a destino de férias, com marina, praias e um centro antigo que se faz a pé. A estrada pela linha do Estoril é das mais bonitas da região de Lisboa.',
                 'A partir de Cascais ficam perto a Boca do Inferno e o Cabo da Roca, o ponto mais ocidental da Europa continental.'],
          see=['Centro histórico e marina de Cascais', 'Boca do Inferno', 'Cabo da Roca', 'Estoril e o casino'], combo='Combine com Sintra para um dia completo a oeste de Lisboa.'),
  es=dict(lead='La villa marinera al oeste de Lisboa, en la costa de Estoril. Traslado directo a su hotel o un día tranquilo junto al mar.',
          about=['Cascais pasó de pueblo pesquero a destino de vacaciones, con puerto deportivo, playas y un casco antiguo para recorrer a pie. La carretera por la costa de Estoril es de las más bonitas de la región de Lisboa.',
                 'Desde Cascais están muy cerca la Boca do Inferno y el Cabo da Roca, el punto más occidental de Europa continental.'],
          see=['Casco antiguo y puerto de Cascais', 'Boca do Inferno', 'Cabo da Roca', 'Estoril y su casino'], combo='Combínelo con Sintra para un día completo al oeste de Lisboa.')),
 'd-comporta': dict(name='Comporta', km=115, time='1h15', img='van',
  en=dict(lead='Rice fields, pine forest and long empty beaches on the Alentejo coast. Door to door from the airport or from Lisbon.',
          about=['Comporta is a quiet stretch of the Alentejo coast south of Setúbal, known for its beaches, rice paddies, small villages and design hotels.',
                 'We drive you door to door, with room for beach luggage, and can pick you up again on the day you choose.'],
          see=['Comporta and Carvalhal beaches', 'Rice fields and storks', 'Tróia peninsula', 'Alcácer do Sal'], combo='Combine with a stop in Setúbal or the Arrábida hills.'),
  pt=dict(lead='Arrozais, pinhal e praias extensas no litoral alentejano. Porta a porta a partir do aeroporto ou de Lisboa.',
          about=['A Comporta é um troço tranquilo do litoral alentejano a sul de Setúbal, conhecido pelas praias, arrozais, pequenas aldeias e hotéis de design.',
                 'Levamo-lo porta a porta, com espaço para a bagagem de praia, e voltamos a buscá-lo no dia que escolher.'],
          see=['Praias da Comporta e do Carvalhal', 'Arrozais e cegonhas', 'Península de Tróia', 'Alcácer do Sal'], combo='Combine com uma paragem em Setúbal ou na Arrábida.'),
  es=dict(lead='Arrozales, pinares y largas playas vacías en la costa del Alentejo. Puerta a puerta desde el aeropuerto o desde Lisboa.',
          about=['Comporta es un tramo tranquilo de la costa del Alentejo al sur de Setúbal, conocido por sus playas, arrozales, pequeñas aldeas y hoteles de diseño.',
                 'Le llevamos puerta a puerta, con espacio para el equipaje de playa, y le recogemos de nuevo el día que elija.'],
          see=['Playas de Comporta y Carvalhal', 'Arrozales y cigüeñas', 'Península de Tróia', 'Alcácer do Sal'], combo='Combínelo con una parada en Setúbal o la Arrábida.')),
 'd-evora': dict(name='Évora', km=140, time='1h30', img='bridge',
  en=dict(lead='A walled city in the heart of the Alentejo. A day trip with your driver or a transfer to your hotel or wine estate.',
          about=['Évora\'s historic centre is a UNESCO World Heritage Site, with a Roman temple, a Gothic cathedral and the Chapel of Bones within its walls.',
                 'The surrounding Alentejo is wine country. Your driver can take you to estates for tastings, so nobody in the group has to drive.'],
          see=['Roman Temple', 'Évora Cathedral', 'Chapel of Bones', 'Alentejo wine estates'], combo='Combine with Monsaraz or Arraiolos.'),
  pt=dict(lead='Uma cidade muralhada no coração do Alentejo. Passeio de um dia com motorista ou transfer para o hotel ou herdade.',
          about=['O centro histórico de Évora é Património Mundial da UNESCO, com um templo romano, uma sé gótica e a Capela dos Ossos dentro das muralhas.',
                 'À volta é terra de vinho. O motorista leva-o às herdades para provas, para que ninguém do grupo tenha de conduzir.'],
          see=['Templo Romano', 'Sé de Évora', 'Capela dos Ossos', 'Herdades e adegas do Alentejo'], combo='Combine com Monsaraz ou Arraiolos.'),
  es=dict(lead='Una ciudad amurallada en el corazón del Alentejo. Excursión de un día con chófer o traslado a su hotel o finca.',
          about=['El centro histórico de Évora es Patrimonio Mundial de la UNESCO, con un templo romano, una catedral gótica y la Capilla de los Huesos dentro de sus murallas.',
                 'Alrededor es tierra de vino. El chófer le lleva a las bodegas para catas, para que nadie del grupo tenga que conducir.'],
          see=['Templo Romano', 'Catedral de Évora', 'Capilla de los Huesos', 'Bodegas del Alentejo'], combo='Combínelo con Monsaraz o Arraiolos.')),
 'd-fatima': dict(name='Fátima', km=130, time='1h30', img='bridge',
  en=dict(lead='The Sanctuary of Fátima, one of the most visited pilgrimage sites in Europe. A day trip or a transfer, at your pace.',
          about=['The Sanctuary of Our Lady of Fátima receives pilgrims from all over the world, especially around the 13th of each month from May to October.',
                 'The route north passes some of central Portugal\'s best-known towns, so a day trip can include Batalha, Nazaré or Óbidos.'],
          see=['Sanctuary of Fátima', 'Batalha Monastery', 'Nazaré', 'Óbidos'], combo='Combine with Batalha, Nazaré and Óbidos in one day.'),
  pt=dict(lead='O Santuário de Fátima, dos locais de peregrinação mais visitados da Europa. Passeio de um dia ou transfer, ao seu ritmo.',
          about=['O Santuário de Nossa Senhora de Fátima recebe peregrinos de todo o mundo, sobretudo à volta do dia 13 de cada mês, de maio a outubro.',
                 'O caminho para norte passa por algumas das vilas mais conhecidas do centro do país, por isso o dia pode incluir a Batalha, a Nazaré ou Óbidos.'],
          see=['Santuário de Fátima', 'Mosteiro da Batalha', 'Nazaré', 'Óbidos'], combo='Combine com a Batalha, a Nazaré e Óbidos no mesmo dia.'),
  es=dict(lead='El Santuario de Fátima, uno de los lugares de peregrinación más visitados de Europa. Excursión de un día o traslado, a su ritmo.',
          about=['El Santuario de Nuestra Señora de Fátima recibe peregrinos de todo el mundo, sobre todo en torno al día 13 de cada mes, de mayo a octubre.',
                 'El camino hacia el norte pasa por algunas de las villas más conocidas del centro de Portugal, así que el día puede incluir Batalha, Nazaré u Óbidos.'],
          see=['Santuario de Fátima', 'Monasterio de Batalha', 'Nazaré', 'Óbidos'], combo='Combínelo con Batalha, Nazaré y Óbidos en el mismo día.')),
 'd-algarve': dict(name='Algarve', km=260, time='2h45', img='van',
  en=dict(lead='From Lisbon to the beaches of the south, door to door. No hire car and no transfer between flights.',
          about=['The Algarve stretches along Portugal\'s southern coast, from Sagres in the west to the Spanish border. Central resorts such as Albufeira and Vilamoura are about 2h45 from Lisbon airport.',
                 'A private transfer is often simpler than a connecting flight or a hire car, especially for families and groups with luggage. We can stop on the way.'],
          see=['Albufeira', 'Vilamoura', 'Lagos and Ponta da Piedade', 'Faro'], combo='Stop in Comporta or Évora on the way down.'),
  pt=dict(lead='De Lisboa às praias do sul, porta a porta. Sem carro alugado e sem voos de ligação.',
          about=['O Algarve estende-se pela costa sul do país, de Sagres até à fronteira com Espanha. Zonas centrais como Albufeira e Vilamoura ficam a cerca de 2h45 do aeroporto de Lisboa.',
                 'Um transfer privado é muitas vezes mais simples do que um voo de ligação ou um carro alugado, sobretudo para famílias e grupos com malas. Podemos parar pelo caminho.'],
          see=['Albufeira', 'Vilamoura', 'Lagos e Ponta da Piedade', 'Faro'], combo='Pare na Comporta ou em Évora pelo caminho.'),
  es=dict(lead='De Lisboa a las playas del sur, puerta a puerta. Sin coche de alquiler y sin vuelos de conexión.',
          about=['El Algarve se extiende por la costa sur de Portugal, de Sagres a la frontera con España. Zonas centrales como Albufeira y Vilamoura están a unas 2h45 del aeropuerto de Lisboa.',
                 'Un traslado privado suele ser más sencillo que un vuelo de conexión o un coche de alquiler, sobre todo para familias y grupos con maletas. Podemos parar por el camino.'],
          see=['Albufeira', 'Vilamoura', 'Lagos y Ponta da Piedade', 'Faro'], combo='Pare en Comporta o en Évora por el camino.')),
 'd-porto': dict(name={'en': 'Porto', 'pt': 'Porto', 'es': 'Oporto'}, km=310, time='3h', img='bridge',
  en=dict(lead='Lisbon to Porto door to door, with stops wherever you like. A comfortable alternative to the train for families and groups.',
          about=['Porto\'s riverside Ribeira district is a UNESCO World Heritage Site, and the port wine cellars sit across the river in Vila Nova de Gaia. Upriver, the Douro valley is one of the world\'s oldest wine regions.',
                 'The drive takes about three hours. Many travellers break the journey in Coimbra, Aveiro or Fátima.'],
          see=['Ribeira and the Douro riverfront', 'Port wine cellars in Gaia', 'Douro valley', 'Coimbra and Aveiro on the way'], combo='Stop in Coimbra, Aveiro or Fátima on the way.'),
  pt=dict(lead='De Lisboa ao Porto porta a porta, com paragens onde quiser. Uma alternativa confortável ao comboio para famílias e grupos.',
          about=['A Ribeira do Porto é Património Mundial da UNESCO, e as caves de vinho do Porto ficam do outro lado do rio, em Vila Nova de Gaia. Rio acima, o Douro é uma das regiões vinhateiras mais antigas do mundo.',
                 'A viagem demora cerca de três horas. Muitos viajantes param em Coimbra, Aveiro ou Fátima.'],
          see=['Ribeira e a frente do Douro', 'Caves do vinho do Porto em Gaia', 'Vale do Douro', 'Coimbra e Aveiro pelo caminho'], combo='Pare em Coimbra, Aveiro ou Fátima pelo caminho.'),
  es=dict(lead='De Lisboa a Oporto puerta a puerta, con paradas donde quiera. Una alternativa cómoda al tren para familias y grupos.',
          about=['La Ribeira de Oporto es Patrimonio Mundial de la UNESCO, y las bodegas de vino de Oporto están al otro lado del río, en Vila Nova de Gaia. Río arriba, el Duero es una de las regiones vinícolas más antiguas del mundo.',
                 'El viaje dura unas tres horas. Muchos viajeros paran en Coímbra, Aveiro o Fátima.'],
          see=['Ribeira y la orilla del Duero', 'Bodegas de vino de Oporto en Gaia', 'Valle del Duero', 'Coímbra y Aveiro por el camino'], combo='Pare en Coímbra, Aveiro o Fátima por el camino.')),
}

DL = {  # rótulos comuns às páginas de destino
 'en': dict(title='Private transfer from Lisbon to {nt} · Day trips with driver · Dark Diamond Luxury',
            desc='Private transfer from Lisbon or Lisbon airport to {nt}, about {t}. One-way, return or a day trip with your driver at your disposal. Price confirmed before you book.',
            h1='Private transfer from Lisbon to {nt}', about='About {nt}', see='Worth seeing', opts='How to go',
            o=['<b>One-way or return transfer</b>, from the airport, your hotel, the cruise port or any address.', '<b>Day trip</b> with the driver waiting and moving you between stops.', '{combo}'],
            facts='The journey', rows=[('From Lisbon airport', '≈ {km} km'), ('Journey time', '≈ {t}'), ('Vehicle', 'Car or Mercedes-Benz V-Class van'), ('Pick-up', 'Airport, hotel, cruise port or any address')],
            note='Indicative times without traffic.', others='Other destinations', book='Book this transfer', call='Call us',
            cta='Going to {nt}?', ctap='Tell us the date, time and number of passengers. We reply with confirmation and price.'),
 'pt': dict(title='Transfer privado de Lisboa para {nt} · Passeios com motorista · Dark Diamond Luxury',
            desc='Transfer privado de Lisboa ou do aeroporto para {nt}, cerca de {t}. Só ida, ida e volta ou passeio de um dia com motorista à disposição. Preço confirmado antes de reservar.',
            h1='Transfer privado de Lisboa para {nt}', about='Sobre {nt}', see='A não perder', opts='Como ir',
            o=['<b>Transfer só de ida ou ida e volta</b>, a partir do aeroporto, do hotel, do porto de cruzeiros ou de qualquer morada.', '<b>Passeio de um dia</b> com o motorista à espera e a levá-lo entre paragens.', '{combo}'],
            facts='A viagem', rows=[('Desde o aeroporto de Lisboa', '≈ {km} km'), ('Duração', '≈ {t}'), ('Veículo', 'Carro ou carrinha Mercedes-Benz Classe V'), ('Recolha', 'Aeroporto, hotel, porto de cruzeiros ou qualquer morada')],
            note='Tempos indicativos, sem trânsito.', others='Outros destinos', book='Reservar este transfer', call='Ligar',
            cta='Vai {ng}?', ctap='Diga-nos a data, a hora e o número de passageiros. Respondemos com a confirmação e o preço.'),
 'es': dict(title='Traslado privado de Lisboa {ng} · Excursiones con chófer · Dark Diamond Luxury',
            desc='Traslado privado desde Lisboa o el aeropuerto {ng}, unos {t}. Solo ida, ida y vuelta o excursión de un día con chófer a disposición. Precio confirmado antes de reservar.',
            h1='Traslado privado de Lisboa {ng}', about='Sobre {nt}', see='Imprescindibles', opts='Cómo ir',
            o=['<b>Traslado solo ida o ida y vuelta</b>, desde el aeropuerto, el hotel, el puerto de cruceros o cualquier dirección.', '<b>Excursión de un día</b> con el chófer esperando y llevándole entre paradas.', '{combo}'],
            facts='El viaje', rows=[('Desde el aeropuerto de Lisboa', '≈ {km} km'), ('Duración', '≈ {t}'), ('Vehículo', 'Coche o furgoneta Mercedes-Benz Clase V'), ('Recogida', 'Aeropuerto, hotel, puerto de cruceros o cualquier dirección')],
            note='Tiempos orientativos, sin tráfico.', others='Otros destinos', book='Reservar este traslado', call='Llamar',
            cta='¿Va {ng}?', ctap='Díganos la fecha, la hora y el número de pasajeros. Le respondemos con la confirmación y el precio.'),
}


ART = {
    'd-porto': {'pt': {'nt': 'o Porto', 'ng': 'ao Porto'}},
    'd-algarve': {'pt': {'nt': 'o Algarve', 'ng': 'ao Algarve'}, 'en': {'nt': 'the Algarve', 'ng': 'to the Algarve'},
                  'es': {'nt': 'el Algarve', 'ng': 'al Algarve'}},
}


def dest_page(key, lang):
    d, l, c = D[key], DL[lang], D[key][lang]
    n = d['name'][lang] if isinstance(d['name'], dict) else d['name']
    # Formas com artigo: "para o Porto", "to the Algarve", "al Algarve"…
    art = ART.get(key, {}).get(lang, {})
    nt = art.get('nt', n)
    ng = art.get('ng', {'pt': f'a {n}', 'es': f'a {n}', 'en': f'to {n}'}[lang])
    f = lambda s: s.format(n=n, nt=nt, ng=ng, t=d['time'], km=d['km'], combo=c['combo'])  # noqa: E731
    return dict(
        title=f(l['title']), desc=f(l['desc']), crumb=n, h1=f(l['h1']), lead=c['lead'], img=d['img'], to=n,
        ctas=[('book', l['book']), ('tel', l['call'])],
        blocks=[
            dict(type='split', h=f(l['about']), p=c['about']),
            dict(type='split', bg='bone', h=l['see'], ticks=c['see']),
            dict(type='split', h=l['opts'], ticks=[f(x) for x in l['o']]),
            dict(type='split', bg='alt', h=l['facts'], rows=[(a, f(b)) for a, b in l['rows']], after=[l['note']],
                 related=[x for x in DESTS if x != key]),
            dict(type='cta', h=f(l['cta']), p=l['ctap'], ctas=[('book', l['book']), ('tel', l['call'])]),
        ])


for _k in DESTS:
    PAGES[_k] = {lang: dest_page(_k, lang) for lang in ('en', 'pt', 'es')}

# =====================================================================================
# INFORMAÇÃO LEGAL
# =====================================================================================
def legal_html(lang):
    t = LEGAL['type'][lang]
    reg = LEGAL['registry'][lang]
    if lang == 'pt':
        return f'''<h2>Identificação da empresa</h2>
<p><b>Dark Diamond Luxury</b> é o nome comercial de <b>{LEGAL["name"]}</b>, {t.lower()}, com sede em {ADDR}, matriculada na {reg} sob o número único de matrícula e de pessoa coletiva {LEGAL["nipc"]}, com o capital social de {LEGAL["capital"]}.</p>
<p>Agente de animação turística registado no Turismo de Portugal, RNAAT n.º {LEGAL["rnaat"]}. Seguros de responsabilidade civil e de acidentes pessoais em vigor.</p>
<h2>Contactos</h2>
<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Telefone: {PH}</p>
<h2>Livro de Reclamações</h2>
<p>Pode apresentar uma reclamação no <a href="https://www.livroreclamacoes.pt" rel="noopener">Livro de Reclamações Eletrónico</a>.</p>
<h2>Resolução alternativa de litígios</h2>
<p>Em caso de litígio de consumo, o consumidor pode recorrer ao Centro de Arbitragem de Conflitos de Consumo de Lisboa (<a href="https://www.centroarbitragemlisboa.pt" rel="noopener">www.centroarbitragemlisboa.pt</a>). Mais informação no Portal do Consumidor (<a href="https://www.consumidor.gov.pt" rel="noopener">www.consumidor.gov.pt</a>).</p>
<h2>Fotografias</h2>
<p>As fotografias deste site são ilustrativas e usadas ao abrigo da Unsplash License. Os autores estão identificados no rodapé.</p>'''
    if lang == 'es':
        return f'''<h2>Identificación de la empresa</h2>
<p><b>Dark Diamond Luxury</b> es el nombre comercial de <b>{LEGAL["name"]}</b>, {t.lower()} de derecho portugués, con domicilio social en {ADDR}, Portugal, inscrita en el {reg} con el número único de registro y de identificación fiscal {LEGAL["nipc"]}, con un capital social de {LEGAL["capital"]}.</p>
<p>Agente de animación turística registrado en Turismo de Portugal, RNAAT n.º {LEGAL["rnaat"]}. Seguros de responsabilidad civil y de accidentes personales en vigor.</p>
<h2>Contacto</h2>
<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Teléfono: {PH}</p>
<h2>Libro de Reclamaciones</h2>
<p>Puede presentar una reclamación en el <a href="https://www.livroreclamacoes.pt" rel="noopener">Libro de Reclamaciones Electrónico (Livro de Reclamações)</a>.</p>
<h2>Resolución alternativa de litigios</h2>
<p>En caso de litigio de consumo, el consumidor puede recurrir al Centro de Arbitraje de Conflictos de Consumo de Lisboa (<a href="https://www.centroarbitragemlisboa.pt" rel="noopener">www.centroarbitragemlisboa.pt</a>). Más información en el Portal do Consumidor (<a href="https://www.consumidor.gov.pt" rel="noopener">www.consumidor.gov.pt</a>).</p>
<h2>Fotografías</h2>
<p>Las fotografías de este sitio son ilustrativas y se utilizan bajo la Unsplash License. Los autores se indican al pie de página.</p>'''
    return f'''<h2>Company details</h2>
<p><b>Dark Diamond Luxury</b> is the trading name of <b>{LEGAL["name"]}</b>, a {t.lower()} under Portuguese law, with registered office at {ADDR}, Portugal, registered with the {reg} under the single registration and tax number {LEGAL["nipc"]}, with a share capital of {LEGAL["capital"]}.</p>
<p>Tourism activity operator registered with Turismo de Portugal, RNAAT no. {LEGAL["rnaat"]}. Civil liability and personal accident insurance in force.</p>
<h2>Contact</h2>
<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Phone: {PH}</p>
<h2>Complaints</h2>
<p>You can file a complaint in the Portuguese <a href="https://www.livroreclamacoes.pt" rel="noopener">Electronic Complaints Book (Livro de Reclamações)</a>.</p>
<h2>Alternative dispute resolution</h2>
<p>In the event of a consumer dispute, consumers may refer to the Lisbon Consumer Arbitration Centre (<a href="https://www.centroarbitragemlisboa.pt" rel="noopener">www.centroarbitragemlisboa.pt</a>). More information on the Portuguese Consumer Portal (<a href="https://www.consumidor.gov.pt" rel="noopener">www.consumidor.gov.pt</a>).</p>
<h2>Photographs</h2>
<p>The photographs on this site are illustrative and used under the Unsplash License. Authors are credited in the footer.</p>'''


PAGES['legal'] = {
 'en': dict(title='Legal information · Dark Diamond Luxury', desc=f'Company details of {LEGAL["name"]} (Dark Diamond Luxury), complaints and dispute resolution.', crumb='Legal information', h1='Legal information', lead=f'Dark Diamond Luxury · {LEGAL["name"]}', blocks=[dict(type='prose', html=legal_html('en'))]),
 'pt': dict(title='Informação legal · Dark Diamond Luxury', desc=f'Identificação de {LEGAL["name"]} (Dark Diamond Luxury), Livro de Reclamações e resolução alternativa de litígios.', crumb='Informação legal', h1='Informação legal', lead=f'Dark Diamond Luxury · {LEGAL["name"]}', blocks=[dict(type='prose', html=legal_html('pt'))]),
 'es': dict(title='Aviso legal · Dark Diamond Luxury', desc=f'Datos de {LEGAL["name"]} (Dark Diamond Luxury), reclamaciones y resolución de litigios.', crumb='Aviso legal', h1='Aviso legal', lead=f'Dark Diamond Luxury · {LEGAL["name"]}', blocks=[dict(type='prose', html=legal_html('es'))]),
}

# =====================================================================================
# PRIVACIDADE
# =====================================================================================
PRIV = {
 'pt': f'''<p>Última atualização: outubro de 2026.</p>
<h2>Quem é responsável pelos seus dados</h2>
<p>{LEGAL["name"]} (Dark Diamond Luxury), NIPC {LEGAL["nipc"]}, {ADDR}. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Este site</h2>
<ul><li>Não usa cookies nem guarda os dados que escreve no formulário de reserva.</li>
<li>O formulário apenas prepara uma mensagem e abre o WhatsApp. O que enviar passa a ser tratado pelo WhatsApp (Meta) e por nós, para responder ao seu pedido.</li>
<li>Contamos visitas de forma anónima com o GoatCounter, sem cookies e sem identificar quem visita.</li></ul>
<h2>Quando reserva um serviço</h2>
<p>Tratamos o nome, o contacto, os dados do voo, as moradas de recolha e destino, o número de passageiros e as notas que nos der, para prestar o serviço (execução do contrato) e para cumprir obrigações fiscais e contabilísticas. Os dados necessários são partilhados com o motorista que faz o serviço. Se a reserva vier de uma agência ou parceiro, recebemos estes dados deles.</p>
<p>Guardamos os dados enquanto forem necessários para o serviço e, depois, pelo prazo exigido por lei para fins fiscais.</p>
<h2>App interna Despacho</h2>
<p>A equipa e os motoristas usam uma app interna para organizar os serviços. A localização dos motoristas é registada apenas quando estes atualizam o estado de um serviço, e só é visível à gerência. Agências e parceiros nunca têm acesso à localização.</p>
<h2>Os seus direitos</h2>
<p>Pode pedir acesso, retificação, apagamento, limitação ou portabilidade dos seus dados, ou opor-se ao seu tratamento, através de <a href="mailto:{EMAIL}">{EMAIL}</a>. Pode também apresentar queixa à Comissão Nacional de Proteção de Dados (<a href="https://www.cnpd.pt" rel="noopener">www.cnpd.pt</a>).</p>''',
 'en': f'''<p>Last updated: October 2026.</p>
<h2>Who is responsible for your data</h2>
<p>{LEGAL["name"]} (Dark Diamond Luxury), VAT no. {LEGAL["nipc"]}, {ADDR}, Portugal. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>This website</h2>
<ul><li>It does not use cookies and does not store what you type in the booking form.</li>
<li>The form only prepares a message and opens WhatsApp. What you send is then processed by WhatsApp (Meta) and by us, to reply to your request.</li>
<li>We count visits anonymously with GoatCounter, without cookies and without identifying visitors.</li></ul>
<h2>When you book a service</h2>
<p>We process your name, contact details, flight details, pick-up and drop-off addresses, number of passengers and any notes you give us, to provide the service (performance of a contract) and to meet tax and accounting obligations. The necessary details are shared with the driver who carries out the service. If the booking comes from an agency or partner, we receive these details from them.</p>
<p>We keep the data for as long as needed for the service and then for the period required by law for tax purposes.</p>
<h2>Internal app (Despacho)</h2>
<p>Our team and drivers use an internal app to organise services. Drivers\' location is recorded only when they update the status of a service, and is visible only to management. Agencies and partners never have access to location data.</p>
<h2>Your rights</h2>
<p>You can request access to, rectification, erasure, restriction or portability of your data, or object to its processing, by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>. You can also lodge a complaint with the Portuguese data protection authority, CNPD (<a href="https://www.cnpd.pt" rel="noopener">www.cnpd.pt</a>).</p>''',
 'es': f'''<p>Última actualización: octubre de 2026.</p>
<h2>Responsable de sus datos</h2>
<p>{LEGAL["name"]} (Dark Diamond Luxury), NIF {LEGAL["nipc"]}, {ADDR}, Portugal. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Este sitio</h2>
<ul><li>No utiliza cookies ni guarda lo que escribe en el formulario de reserva.</li>
<li>El formulario solo prepara un mensaje y abre WhatsApp. Lo que envíe pasa a ser tratado por WhatsApp (Meta) y por nosotros, para responder a su solicitud.</li>
<li>Contamos las visitas de forma anónima con GoatCounter, sin cookies y sin identificar a los visitantes.</li></ul>
<h2>Cuando reserva un servicio</h2>
<p>Tratamos su nombre, datos de contacto, datos del vuelo, direcciones de recogida y destino, número de pasajeros y las notas que nos facilite, para prestar el servicio (ejecución del contrato) y cumplir obligaciones fiscales y contables. Los datos necesarios se comparten con el chófer que realiza el servicio. Si la reserva llega a través de una agencia o partner, recibimos estos datos de ellos.</p>
<p>Conservamos los datos mientras sean necesarios para el servicio y, después, durante el plazo exigido por la ley a efectos fiscales.</p>
<h2>App interna (Despacho)</h2>
<p>Nuestro equipo y los chóferes utilizan una app interna para organizar los servicios. La ubicación de los chóferes solo se registra cuando actualizan el estado de un servicio y solo es visible para la gerencia. Las agencias y partners nunca tienen acceso a la ubicación.</p>
<h2>Sus derechos</h2>
<p>Puede solicitar el acceso, rectificación, supresión, limitación o portabilidad de sus datos, u oponerse a su tratamiento, escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. También puede presentar una reclamación ante la autoridad portuguesa de protección de datos, CNPD (<a href="https://www.cnpd.pt" rel="noopener">www.cnpd.pt</a>).</p>''',
}
PAGES['privacy'] = {
 'en': dict(title='Privacy policy · Dark Diamond Luxury', desc='How Dark Diamond Luxury handles personal data on this website, in bookings and in its internal app.', crumb='Privacy', h1='Privacy policy', lead='What we collect, why, and your rights.', blocks=[dict(type='prose', html=PRIV['en'])]),
 'pt': dict(title='Política de privacidade · Dark Diamond Luxury', desc='Como a Dark Diamond Luxury trata dados pessoais neste site, nas reservas e na app interna.', crumb='Privacidade', h1='Política de privacidade', lead='O que recolhemos, porquê, e os seus direitos.', blocks=[dict(type='prose', html=PRIV['pt'])]),
 'es': dict(title='Política de privacidad · Dark Diamond Luxury', desc='Cómo trata Dark Diamond Luxury los datos personales en este sitio, en las reservas y en su app interna.', crumb='Privacidad', h1='Política de privacidad', lead='Qué recogemos, por qué y sus derechos.', blocks=[dict(type='prose', html=PRIV['es'])]),
}

# =====================================================================================
# SUPORTE DA APP (página pedida pela Apple para a app Despacho)
# =====================================================================================
SUP = {
 'pt': ('Suporte da app Despacho', 'Despacho é a app interna da equipa e dos motoristas da Dark Diamond Luxury.',
        f'<h2>Precisa de ajuda?</h2><p>Para problemas de acesso, palavra-passe ou funcionamento da app, contacte-nos:</p><p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Telefone: {PH}</p><p>O acesso à app é criado pela gerência. Se é motorista e ainda não tem acesso, fale com o escritório.</p>'),
 'en': ('Despacho app support', 'Despacho is the internal app used by the Dark Diamond Luxury team and drivers.',
        f'<h2>Need help?</h2><p>For sign-in, password or app issues, contact us:</p><p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Phone: {PH}</p><p>Access to the app is created by management. If you are a driver without access yet, please contact the office.</p>'),
 'es': ('Soporte de la app Despacho', 'Despacho es la app interna del equipo y los chóferes de Dark Diamond Luxury.',
        f'<h2>¿Necesita ayuda?</h2><p>Para problemas de acceso, contraseña o funcionamiento de la app, contáctenos:</p><p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Teléfono: {PH}</p><p>El acceso a la app lo crea la gerencia. Si es chófer y aún no tiene acceso, hable con la oficina.</p>'),
}
PAGES['support'] = {l: dict(title=f'{v[0]} · Dark Diamond Luxury', desc=v[1], crumb=v[0], h1=v[0], lead=v[1], blocks=[dict(type='prose', html=v[2])]) for l, v in SUP.items()}
