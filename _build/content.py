# Textos das páginas interiores, em EN / PT / ES.
# Onde falta um dado da empresa aparece <span class="todo">[…]</span> (a dourado) para ser fácil de encontrar.
from config import COVERAGE, DESTS, EMAIL, FLEET, LANGS_SPOKEN, LEGAL, PHONES

TODO = lambda s: f'<span class="todo">[{s}]</span>'  # noqa: E731
PH = ' · '.join(PHONES)
ADDR = f"{LEGAL['street']}, {LEGAL['postcode']} {LEGAL['city']}"

PAGES = {}

# =====================================================================================
# AGÊNCIAS E PARCEIROS
# =====================================================================================
PAGES['agencies'] = {
 'en': dict(
  title='Ground partner in Portugal for travel agencies · Dark Diamond Luxury',
  desc='Private transfers, tours and chauffeur services for agencies, tour operators, DMCs and cruise lines in Portugal, Spain and France. RNAAT 682/2022.',
  crumb='Agencies and partners', h1='Your ground partner in Portugal.',
  lead='Private transfers, tours and chauffeured services for travel agencies, tour operators, DMCs and cruise lines. Portugal, Spain and France.',
  subject='Partnership request / rates', ctas=[('mail', 'Request our rates'), ('tel', 'Call us')],
  blocks=[
   dict(type='split', h='Why agencies work with us', ticks=[
     '<b>Registered with Turismo de Portugal.</b> Licensed tourism activity operator, RNAAT no. 682/2022.',
     '<b>Insured.</b> Civil liability and personal accident insurance in force.',
     '<b>Flight tracking, meet and greet.</b> Your client is met at arrivals with a name sign, whatever time the flight lands.',
     '<b>A direct line, 24/7.</b> You speak to the people who plan and dispatch the service, not a call centre.',
     '<b>Multilingual drivers.</b> Portuguese, English, Spanish and French.',
     '<b>From one passenger to groups of 19.</b> Mercedes-Benz S-Class, E-Class and V-Class, Sprinter and a 19-seat minibus.',
     '<b>Written confirmation.</b> Every booking is confirmed in writing, and the driver\'s details are sent before the service.']),
   dict(type='split', bg='bone', h='Where we operate', p=['Based in Lisbon, with regular services across Portugal and long-distance transfers to Spain and France.'], ticks=[
     'Lisbon airport (LIS), city hotels and the cruise terminals', 'Sintra, Cascais and the Estoril coast', 'Comporta and the Alentejo coast',
     'Évora and the Alentejo', 'Fátima, Óbidos, Nazaré and Batalha', 'Porto and the Douro valley', 'The Algarve', 'Spain and France, on request']),
   dict(type='split', h='How it works', steps=[
     ('Send the booking', 'By email or WhatsApp: passenger name, date, flight or pick-up time, number of passengers and luggage.'),
     ('We confirm', 'Availability and price confirmed in writing, quickly and at any hour.'),
     ('Before the service', 'You receive the driver\'s name, phone number and vehicle.'),
     ('On the day', 'Meet and greet, flight tracking and direct contact with the driver. If anything changes, we tell you straight away.'),
     ('Invoicing', f'Per service or monthly, as agreed. Invoices issued by {LEGAL["name"]}, VAT PT{LEGAL["nipc"]}.')]),
   dict(type='split', bg='alt', h='Services', ticks=[
     'Airport and cruise port transfers', 'Chauffeur at disposal, by the hour or by the day', 'Private tours and day trips',
     'Events, weddings and groups', 'Long distance within Portugal and to Spain and France']),
   dict(type='split', h='Company details', rows=[
     ('Trading name', 'Dark Diamond Luxury'), ('Legal name', LEGAL['name']), ('VAT number (NIPC)', LEGAL['nipc']),
     ('Registered office', ADDR), ('Tourism registration', f'RNAAT {LEGAL["rnaat"]}'),
     ('Insurance', 'Civil liability · Personal accident'), ('Fleet', FLEET['en']), ('Drivers\' languages', LANGS_SPOKEN['en']), ('Operations', '24 hours, 7 days'), ('Coverage', COVERAGE['en']), ('Contact', f'{EMAIL}<br>{PH}')]),
   dict(type='cta', h='Let\'s work together.', p='Send us your usual routes and volumes and we will prepare a rate sheet for your agency.',
        ctas=[('mail', 'Request our rates'), ('tel', 'Call us')]),
  ]),
 'pt': dict(
  title='Parceiro de transporte para agências em Portugal · Dark Diamond Luxury',
  desc='Transfers privados, tours e motorista para agências, operadores turísticos, DMCs e linhas de cruzeiro em Portugal, Espanha e França. RNAAT 682/2022.',
  crumb='Agências e parceiros', h1='O seu parceiro em terra, em Portugal.',
  lead='Transfers privados, tours e serviços com motorista para agências de viagens, operadores turísticos, DMCs e linhas de cruzeiro. Portugal, Espanha e França.',
  subject='Pedido de parceria / tabela de preços', ctas=[('mail', 'Pedir tabela de preços'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Porque trabalham connosco', ticks=[
     '<b>Registados no Turismo de Portugal.</b> Agente de animação turística, RNAAT n.º 682/2022.',
     '<b>Com seguro.</b> Seguros de responsabilidade civil e de acidentes pessoais em vigor.',
     '<b>Seguimento de voos e receção com placa.</b> O seu cliente é recebido nas chegadas com o nome, à hora a que o voo aterrar.',
     '<b>Contacto direto, 24/7.</b> Fale com quem planeia e despacha o serviço, não com um call center.',
     '<b>Motoristas que falam a língua do cliente.</b> Português, inglês, espanhol e francês.',
     '<b>De um passageiro a grupos de 19.</b> Mercedes-Benz Classe S, Classe E e Classe V, Sprinter e minibus de 19 lugares.',
     '<b>Confirmação por escrito.</b> Cada reserva é confirmada por escrito e os dados do motorista seguem antes do serviço.']),
   dict(type='split', bg='bone', h='Onde trabalhamos', p=['Com base em Lisboa, serviços regulares em todo o país e transfers de longa distância para Espanha e França.'], ticks=[
     'Aeroporto de Lisboa, hotéis da cidade e terminais de cruzeiros', 'Sintra, Cascais e a linha do Estoril', 'Comporta e o litoral alentejano',
     'Évora e o Alentejo', 'Fátima, Óbidos, Nazaré e Batalha', 'Porto e o vale do Douro', 'Algarve', 'Espanha e França, por pedido']),
   dict(type='split', h='Como funciona', steps=[
     ('Envie a reserva', 'Por email ou WhatsApp: nome do passageiro, data, voo ou hora de recolha, número de passageiros e malas.'),
     ('Confirmamos', 'Disponibilidade e preço confirmados por escrito, com rapidez e a qualquer hora.'),
     ('Antes do serviço', 'Receberá o nome e o telefone do motorista e o veículo.'),
     ('No dia', 'Receção com placa, seguimento do voo e contacto direto com o motorista. Se algo mudar, avisamos de imediato.'),
     ('Faturação', f'Por serviço ou mensal, conforme acordado. Faturas emitidas por {LEGAL["name"]}, NIPC {LEGAL["nipc"]}.')]),
   dict(type='split', bg='alt', h='Serviços', ticks=[
     'Transfers de aeroporto e de porto de cruzeiros', 'Motorista à disposição, à hora ou ao dia', 'Tours privados e passeios de um dia',
     'Eventos, casamentos e grupos', 'Longa distância em Portugal e para Espanha e França']),
   dict(type='split', h='Dados da empresa', rows=[
     ('Nome comercial', 'Dark Diamond Luxury'), ('Firma', LEGAL['name']), ('NIPC', LEGAL['nipc']),
     ('Sede', ADDR), ('Registo de turismo', f'RNAAT {LEGAL["rnaat"]}'),
     ('Seguros', 'Responsabilidade civil · Acidentes pessoais'), ('Frota', FLEET['pt']), ('Línguas dos motoristas', LANGS_SPOKEN['pt']), ('Operação', '24 horas, 7 dias'), ('Cobertura', COVERAGE['pt']), ('Contacto', f'{EMAIL}<br>{PH}')]),
   dict(type='cta', h='Vamos trabalhar juntos.', p='Envie-nos as rotas e volumes habituais e preparamos uma tabela de preços para a sua agência.',
        ctas=[('mail', 'Pedir tabela de preços'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Partner de transporte para agencias en Portugal · Dark Diamond Luxury',
  desc='Traslados privados, tours y chófer para agencias, turoperadores, DMCs y navieras en Portugal, España y Francia. RNAAT 682/2022.',
  crumb='Agencias y partners', h1='Su partner en tierra, en Portugal.',
  lead='Traslados privados, tours y servicios con chófer para agencias de viajes, turoperadores, DMCs y navieras. Portugal, España y Francia.',
  subject='Solicitud de colaboración / tarifas', ctas=[('mail', 'Solicitar tarifas'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='Por qué trabajan con nosotros', ticks=[
     '<b>Registrados en Turismo de Portugal.</b> Agente de animación turística, RNAAT n.º 682/2022.',
     '<b>Asegurados.</b> Seguros de responsabilidad civil y de accidentes personales en vigor.',
     '<b>Seguimiento de vuelos y recepción con cartel.</b> Su cliente es recibido en llegadas con su nombre, a la hora a la que aterrice el vuelo.',
     '<b>Contacto directo, 24/7.</b> Hable con quien planifica y asigna el servicio, no con un call center.',
     '<b>Chóferes que hablan el idioma del cliente.</b> Portugués, inglés, español y francés.',
     '<b>De un pasajero a grupos de 19.</b> Mercedes-Benz Clase S, Clase E y Clase V, Sprinter y minibús de 19 plazas.',
     '<b>Confirmación por escrito.</b> Cada reserva se confirma por escrito y los datos del chófer se envían antes del servicio.']),
   dict(type='split', bg='bone', h='Dónde trabajamos', p=['Con base en Lisboa, servicios regulares en todo Portugal y traslados de larga distancia a España y Francia.'], ticks=[
     'Aeropuerto de Lisboa, hoteles de la ciudad y terminales de cruceros', 'Sintra, Cascais y la costa de Estoril', 'Comporta y la costa del Alentejo',
     'Évora y el Alentejo', 'Fátima, Óbidos, Nazaré y Batalha', 'Oporto y el valle del Duero', 'El Algarve', 'España y Francia, bajo petición']),
   dict(type='split', h='Cómo funciona', steps=[
     ('Envíe la reserva', 'Por email o WhatsApp: nombre del pasajero, fecha, vuelo u hora de recogida, número de pasajeros y maletas.'),
     ('Confirmamos', 'Disponibilidad y precio confirmados por escrito, con rapidez y a cualquier hora.'),
     ('Antes del servicio', 'Recibirá el nombre y el teléfono del chófer y el vehículo.'),
     ('El día del servicio', 'Recepción con cartel, seguimiento del vuelo y contacto directo con el chófer. Si algo cambia, le avisamos de inmediato.'),
     ('Facturación', f'Por servicio o mensual, según lo acordado. Facturas emitidas por {LEGAL["name"]}, NIF PT{LEGAL["nipc"]}.')]),
   dict(type='split', bg='alt', h='Servicios', ticks=[
     'Traslados de aeropuerto y de puerto de cruceros', 'Chófer a disposición, por horas o por días', 'Tours privados y excursiones de un día',
     'Eventos, bodas y grupos', 'Larga distancia en Portugal y a España y Francia']),
   dict(type='split', h='Datos de la empresa', rows=[
     ('Nombre comercial', 'Dark Diamond Luxury'), ('Razón social', LEGAL['name']), ('NIF (NIPC)', LEGAL['nipc']),
     ('Domicilio social', ADDR), ('Registro de turismo', f'RNAAT {LEGAL["rnaat"]}'),
     ('Seguros', 'Responsabilidad civil · Accidentes personales'), ('Flota', FLEET['es']), ('Idiomas de los chóferes', LANGS_SPOKEN['es']), ('Operación', '24 horas, 7 días'), ('Cobertura', COVERAGE['es']), ('Contacto', f'{EMAIL}<br>{PH}')]),
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
  title='Lisbon Airport Transfer · Meet and greet · Dark Diamond Luxury',
  desc='Private transfer from Lisbon Airport (LIS) to your hotel or anywhere in Portugal. Flight tracking, meet and greet with your name, price confirmed before booking.',
  crumb='Lisbon airport transfer', h1='Lisbon airport transfers, met by name.', img='plane',
  lead='Private transfer from Lisbon Humberto Delgado Airport (LIS) to your hotel, home or anywhere in Portugal. Your driver tracks the flight and waits at arrivals with your name.',
  ctas=[('book', 'Book airport transfer'), ('tel', 'Call us')],
  blocks=[
   dict(type='split', h='How it works', steps=[
     ('Book', 'Send us your flight number, destination and number of passengers and bags. We reply with confirmation and price.'),
     ('We track your flight', 'If the flight lands early or late, your driver adjusts to the real landing time.'),
     ('Meet at arrivals', 'Your driver waits in the arrivals hall of Terminal 1 or 2, holding a sign with your name.'),
     ('Straight to your door', 'Help with luggage and a direct ride, with no shared stops.')]),
   dict(type='split', bg='bone', h='Journey times from the airport', rows=TIMES, after=['Indicative times, which may vary.']),
   dict(type='split', h='Good to know', ticks=[
     'A private vehicle just for your group: no shared shuttles.', 'Child seats on request: tell us the children\'s ages when booking.',
     'Departures too: pick-up at your hotel at the time you choose.', 'Drivers who speak Portuguese, English, Spanish and French.', 'Available 24/7, whatever time you land.', 'Price confirmed in writing before you book.'], related=DESTS),
   dict(type='cta', h='Landing soon?', p='Send us your flight and destination. We reply with confirmation and price.', ctas=[('book', 'Book airport transfer'), ('tel', 'Call us')]),
  ]),
 'pt': dict(
  title='Transfer do Aeroporto de Lisboa · Dark Diamond Luxury',
  desc='Transfer privado do aeroporto de Lisboa para o seu hotel ou para qualquer ponto do país. Seguimento do voo, receção com o seu nome, preço confirmado antes de reservar.',
  crumb='Transfer aeroporto de Lisboa', h1='Transfers do aeroporto de Lisboa, recebido pelo nome.', img='plane',
  lead='Transfer privado do Aeroporto Humberto Delgado (LIS) para o seu hotel, casa ou qualquer ponto do país. O motorista acompanha o voo e espera nas chegadas com o seu nome.',
  ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Como funciona?', steps=[
     ('Reserve', 'Envie-nos o número do voo, o destino e o número de passageiros e malas. Respondemos com a confirmação e o preço.'),
     ('Acompanhamos o voo', 'Se o voo chegar mais cedo ou mais tarde, o motorista ajusta-se à hora real de aterragem.'),
     ('Receção nas chegadas', 'O motorista espera na zona de chegadas do Terminal 1 ou 2, com uma placa com o seu nome.'),
     ('Direto à porta', 'Ajuda com as malas e viagem direta, sem paragens partilhadas.')]),
   dict(type='split', bg='bone', h='Tempos de viagem a partir do aeroporto', rows=TIMES, after=['Tempos indicativos, que podem variar.']),
   dict(type='split', h='Bom saber', ticks=[
     'Veículo privado só para o seu grupo: sem shuttles partilhados.', 'Cadeiras de criança por pedido: indique a idade das crianças ao reservar.',
     'Também para partidas: recolha no hotel à hora que escolher.', 'Motoristas que falam português, inglês, espanhol e francês.', 'Disponível 24/7, a qualquer hora do voo.', 'Preço confirmado por escrito antes de reservar.'], related=DESTS),
   dict(type='cta', h='Vai aterrar em breve?', p='Envie-nos o voo e o destino. Respondemos com a confirmação e o preço.', ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Traslado Aeropuerto de Lisboa · Dark Diamond Luxury',
  desc='Traslado privado desde el aeropuerto de Lisboa a su hotel o a cualquier punto de Portugal. Seguimiento del vuelo, recepción con su nombre y precio antes de reservar.',
  crumb='Traslado aeropuerto de Lisboa', h1='Traslados desde el aeropuerto de Lisboa, con su nombre.', img='plane',
  lead='Traslado privado desde el Aeropuerto Humberto Delgado (LIS) a su hotel, su casa o cualquier punto de Portugal. El chófer sigue el vuelo y le espera en llegadas con su nombre.',
  ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='¿Cómo funciona?', steps=[
     ('Reserve', 'Envíenos el número de vuelo, el destino y el número de pasajeros y maletas. Le respondemos con la confirmación y el precio.'),
     ('Seguimos su vuelo', 'Si el vuelo llega antes o después, el chófer se ajusta a la hora real de aterrizaje.'),
     ('Recepción en llegadas', 'El chófer le espera en la zona de llegadas de la Terminal 1 o 2, con un cartel con su nombre.'),
     ('Directo a su puerta', 'Ayuda con las maletas y viaje directo, sin paradas compartidas.')]),
   dict(type='split', bg='bone', h='Tiempos de viaje desde el aeropuerto', rows=TIMES, after=['Tiempos orientativos, que pueden variar.']),
   dict(type='split', h='Conviene saber', ticks=[
     'Vehículo privado solo para su grupo: sin shuttles compartidos.', 'Sillas infantiles bajo petición: indíquenos la edad de los niños al reservar.',
     'También para salidas: recogida en su hotel a la hora que elija.', 'Chóferes que hablan portugués, inglés, español y francés.', 'Disponible 24/7, a cualquier hora del vuelo.', 'Precio confirmado por escrito antes de reservar.'], related=DESTS),
   dict(type='cta', h='¿Aterriza pronto?', p='Envíenos el vuelo y el destino. Le respondemos con la confirmación y el precio.', ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# CRUZEIROS
# =====================================================================================
PAGES['cruise'] = {
 'en': dict(
  title='Lisbon Cruise Port Transfers and Excursions · Dark Diamond Luxury',
  desc='Private transfers between Lisbon\'s cruise terminals, the airport and hotels, plus shore excursions to Sintra, Cascais and Lisbon, timed to your all-aboard.',
  crumb='Lisbon cruise terminal', h1='Lisbon cruise port transfers and shore excursions.', img='cruise',
  lead='From the ship to the airport, your hotel or a private tour, timed around your port call. For passengers, agencies and cruise lines.',
  ctas=[('book', 'Book a port transfer'), ('agencies', 'For agencies and cruise lines')],
  blocks=[
   dict(type='split', h='What we do at the port', ticks=[
     '<b>Port and airport.</b> Transfers on embarkation and disembarkation day.', '<b>Port and hotel.</b> For stays before or after the cruise.',
     '<b>Private shore excursions.</b> Lisbon, Sintra, Cascais or Fátima, with a driver who plans the return around the all-aboard time.',
     '<b>Groups.</b> V-Class, Sprinter and a 19-seat minibus, with room for luggage.']),
   dict(type='split', bg='bone', h='Lisbon\'s cruise terminals', p=[
     'Most ships dock at the Lisbon Cruise Terminal, next to Santa Apolónia and Alfama, close to the city centre and around 20 minutes from the airport.',
     'Some ships use the Alcântara or Rocha Conde de Óbidos terminals, further west. Tell us the ship\'s name and we will meet you at the right place.']),
   dict(type='split', h='Back on board on time', p=[
     'On shore excursions we plan the day backwards from the all-aboard time, with a margin for traffic. You keep the driver\'s number and the driver keeps yours.']),
   dict(type='cta', h='Docking in Lisbon?', p='Tell us the ship, the date and what you would like to do. We reply with a plan and a price.', ctas=[('book', 'Book a port transfer'), ('tel', 'Call us')]),
  ]),
 'pt': dict(
  title='Transfers no Terminal de Cruzeiros de Lisboa · Dark Diamond Luxury',
  desc='Transfers privados entre os terminais de cruzeiros de Lisboa, o aeroporto e os hotéis, e excursões a Sintra, Cascais e Lisboa, à hora de regresso ao navio.',
  crumb='Terminal de cruzeiros de Lisboa', h1='Transfers no porto de cruzeiros de Lisboa e excursões em terra.', img='cruise',
  lead='Do navio para o aeroporto, para o hotel ou para um tour privado, ao ritmo da escala. Para passageiros, agências e linhas de cruzeiro.',
  ctas=[('book', 'Reservar transfer'), ('agencies', 'Para agências e linhas de cruzeiro')],
  blocks=[
   dict(type='split', h='O que fazemos no porto', ticks=[
     '<b>Porto e aeroporto.</b> Transfers no dia de embarque e de desembarque.', '<b>Porto e hotel.</b> Para estadias antes ou depois do cruzeiro.',
     '<b>Excursões privadas em terra.</b> Lisboa, Sintra, Cascais ou Fátima, com um motorista que planeia o regresso em função da hora de embarque.',
     '<b>Grupos.</b> Classe V, Sprinter e minibus de 19 lugares, com espaço para as malas.']),
   dict(type='split', bg='bone', h='Os terminais de cruzeiros de Lisboa', p=[
     'A maioria dos navios atraca no Terminal de Cruzeiros de Lisboa, junto a Santa Apolónia e Alfama, perto do centro e a cerca de 20 minutos do aeroporto.',
     'Alguns navios usam os terminais de Alcântara ou da Rocha Conde de Óbidos, mais a oeste. Diga-nos o nome do navio e esperamos no sítio certo.']),
   dict(type='split', h='De volta ao navio a horas', p=[
     'Nas excursões em terra planeamos o dia a partir da hora de regresso a bordo, com margem para o trânsito. Terá o número do motorista e ele o seu.']),
   dict(type='cta', h='Vai fazer escala em Lisboa?', p='Diga-nos o navio, a data e o que gostaria de fazer. Respondemos com um plano e um preço.', ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Traslados en la Terminal de Cruceros de Lisboa · Dark Diamond Luxury',
  desc='Traslados privados entre las terminales de cruceros de Lisboa, el aeropuerto y los hoteles, y excursiones a Sintra, Cascais y Lisboa, a la hora de regreso al barco.',
  crumb='Terminal de cruceros de Lisboa', h1='Traslados en el puerto de cruceros de Lisboa y excursiones en tierra.', img='cruise',
  lead='Del barco al aeropuerto, al hotel o a un tour privado, al ritmo de la escala. Para pasajeros, agencias y navieras.',
  ctas=[('book', 'Reservar traslado'), ('agencies', 'Para agencias y navieras')],
  blocks=[
   dict(type='split', h='Qué hacemos en el puerto', ticks=[
     '<b>Puerto y aeropuerto.</b> Traslados el día de embarque y de desembarque.', '<b>Puerto y hotel.</b> Para estancias antes o después del crucero.',
     '<b>Excursiones privadas en tierra.</b> Lisboa, Sintra, Cascais o Fátima, con un chófer que planifica el regreso según la hora de embarque.',
     '<b>Grupos.</b> Clase V, Sprinter y minibús de 19 plazas, con espacio para el equipaje.']),
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
 'd-sintra': dict(name='Sintra', km=35, time='35 min', img='d-sintra',
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
 'd-cascais': dict(name='Cascais', km=40, time='35 min', img='d-cascais',
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
 'd-comporta': dict(name='Comporta', km=115, time='1h15', img='d-comporta',
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
 'd-evora': dict(name='Évora', km=140, time='1h30', img='d-evora',
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
 'd-fatima': dict(name='Fátima', km=130, time='1h30', img='d-fatima',
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
 'd-algarve': dict(name='Algarve', km=260, time='2h45', img='d-algarve',
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
 'd-porto': dict(name={'en': 'Porto', 'pt': 'Porto', 'es': 'Oporto', 'fr': 'Porto'}, km=310, time='3h', img='d-porto',
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
 'd-madrid': dict(name='Madrid', km=625, time='6h', img='d-madrid',
  en=dict(lead='Lisbon to Madrid door to door, across the Alentejo and Extremadura. No check-in, no luggage limits, and stops wherever you like.',
          about=['Madrid is Spain\'s capital. The Prado, Reina Sofía and Thyssen museums line the Paseo del Prado, which together with Retiro Park is a UNESCO World Heritage Site.',
                 'The drive takes about six hours. The road passes Elvas, Badajoz and Mérida, whose Roman theatre is one of the best preserved in Spain, so the journey can include a stop.'],
          see=['Prado Museum', 'Royal Palace', 'Retiro Park', 'Gran Vía'], combo='Stop in Elvas, Mérida or Trujillo on the way.'),
  pt=dict(lead='De Lisboa a Madrid porta a porta, pelo Alentejo e pela Extremadura. Sem check-in, sem limite de bagagem e com paragens onde quiser.',
          about=['Madrid é a capital de Espanha. Os museus do Prado, Reina Sofía e Thyssen ficam ao longo do Paseo del Prado, que com o Parque do Retiro é Património Mundial da UNESCO.',
                 'A viagem demora cerca de seis horas. A estrada passa por Elvas, Badajoz e Mérida, cujo teatro romano é dos mais bem conservados de Espanha, por isso pode parar pelo caminho.'],
          see=['Museu do Prado', 'Palácio Real', 'Parque do Retiro', 'Gran Vía'], combo='Pare em Elvas, Mérida ou Trujillo pelo caminho.'),
  es=dict(lead='De Lisboa a Madrid puerta a puerta, por el Alentejo y Extremadura. Sin facturación, sin límite de equipaje y con paradas donde quiera.',
          about=['Madrid es la capital de España. Los museos del Prado, Reina Sofía y Thyssen se suceden en el Paseo del Prado, que junto al Parque del Retiro es Patrimonio Mundial de la UNESCO.',
                 'El viaje dura unas seis horas. La carretera pasa por Elvas, Badajoz y Mérida, cuyo teatro romano es de los mejor conservados de España, así que puede parar por el camino.'],
          see=['Museo del Prado', 'Palacio Real', 'Parque del Retiro', 'Gran Vía'], combo='Pare en Elvas, Mérida o Trujillo por el camino.')),
 'd-sevilla': dict(name={'en': 'Seville', 'pt': 'Sevilha', 'es': 'Sevilla', 'fr': 'Séville'}, km=460, time='4h', img='d-sevilla',
  en=dict(lead='Lisbon to Seville door to door, through the Algarve and across the Guadiana. A private alternative to a connecting flight.',
          about=['Seville\'s Cathedral, the Alcázar and the Archivo de Indias form a UNESCO World Heritage Site in the heart of the old town. Across the river, Triana is known for its ceramics and flamenco.',
                 'The drive takes about four hours and crosses into Spain over the Guadiana river, so the Algarve makes an easy stop on the way.'],
          see=['Cathedral and the Giralda', 'Real Alcázar', 'Plaza de España', 'Triana'], combo='Stop in the Algarve or Évora on the way.'),
  pt=dict(lead='De Lisboa a Sevilha porta a porta, pelo Algarve e pela ponte do Guadiana. Uma alternativa privada a um voo de ligação.',
          about=['A Catedral, o Alcázar e o Arquivo das Índias de Sevilha são Património Mundial da UNESCO, no centro da cidade antiga. Do outro lado do rio, Triana é conhecida pela cerâmica e pelo flamenco.',
                 'A viagem demora cerca de quatro horas e entra em Espanha pelo Guadiana, por isso o Algarve é uma paragem fácil pelo caminho.'],
          see=['Catedral e Giralda', 'Real Alcázar', 'Plaza de España', 'Triana'], combo='Pare no Algarve ou em Évora pelo caminho.'),
  es=dict(lead='De Lisboa a Sevilla puerta a puerta, por el Algarve y cruzando el Guadiana. Una alternativa privada a un vuelo de conexión.',
          about=['La Catedral, el Alcázar y el Archivo de Indias de Sevilla son Patrimonio Mundial de la UNESCO, en el corazón del casco antiguo. Al otro lado del río, Triana es conocida por su cerámica y su flamenco.',
                 'El viaje dura unas cuatro horas y entra en España por el Guadiana, así que el Algarve es una parada fácil por el camino.'],
          see=['Catedral y Giralda', 'Real Alcázar', 'Plaza de España', 'Triana'], combo='Pare en el Algarve o en Évora por el camino.')),
 'd-marbella': dict(name='Marbella', km=660, time='5h30', img='d-marbella',
  en=dict(lead='Lisbon to the Costa del Sol door to door. One car, one driver, and your luggage with you the whole way.',
          about=['Marbella lies on the Costa del Sol between Málaga and Gibraltar, with a whitewashed old town around the Plaza de los Naranjos and the marina at Puerto Banús.',
                 'The drive takes about five and a half hours via Seville, which makes a natural stop. Ronda, in the hills above the coast, is about an hour inland.'],
          see=['Old town and Plaza de los Naranjos', 'Puerto Banús', 'The Golden Mile', 'Ronda'], combo='Stop in Seville on the way.'),
  pt=dict(lead='De Lisboa à Costa del Sol porta a porta. Um carro, um motorista e a sua bagagem consigo o caminho todo.',
          about=['Marbella fica na Costa del Sol, entre Málaga e Gibraltar, com uma cidade antiga caiada à volta da Plaza de los Naranjos e a marina de Puerto Banús.',
                 'A viagem demora cerca de cinco horas e meia, por Sevilha, que é uma paragem natural. Ronda, na serra acima da costa, fica a cerca de uma hora para o interior.'],
          see=['Cidade antiga e Plaza de los Naranjos', 'Puerto Banús', 'A Milla de Oro', 'Ronda'], combo='Pare em Sevilha pelo caminho.'),
  es=dict(lead='De Lisboa a la Costa del Sol puerta a puerta. Un coche, un chófer y su equipaje con usted todo el camino.',
          about=['Marbella está en la Costa del Sol, entre Málaga y Gibraltar, con un casco antiguo encalado en torno a la Plaza de los Naranjos y el puerto deportivo de Puerto Banús.',
                 'El viaje dura unas cinco horas y media, pasando por Sevilla, que es una parada natural. Ronda, en la sierra sobre la costa, está a una hora hacia el interior.'],
          see=['Casco antiguo y Plaza de los Naranjos', 'Puerto Banús', 'La Milla de Oro', 'Ronda'], combo='Pare en Sevilla por el camino.')),
 'd-arrabida': dict(name='Arrábida', km=45, time='45 min', img='d-arrabida',
  en=dict(lead='The Arrábida hills and their beaches, 45 minutes south of Lisbon. A day by the sea or a wine afternoon in Azeitão.',
          about=['The Serra da Arrábida natural park drops straight into the sea between Setúbal and Sesimbra, with some of the clearest water near Lisbon at Portinho da Arrábida and Galapinhos beach.',
                 'In Azeitão, historic cellars open for tastings of moscatel and local wine, and Setúbal is known for fish restaurants and fried cuttlefish. With a driver, nobody has to skip the tasting.'],
          see=['Portinho da Arrábida and Galapinhos', 'Azeitão wine cellars', 'Setúbal and its fish restaurants', 'Sesimbra'], combo='Combine with Comporta, across the Sado river.'),
  pt=dict(lead='A serra da Arrábida e as suas praias, a 45 minutos de Lisboa. Um dia de mar ou uma tarde de vinho em Azeitão.',
          about=['O parque natural da Arrábida desce a direito até ao mar entre Setúbal e Sesimbra, com algumas das águas mais límpidas perto de Lisboa, no Portinho da Arrábida e na praia dos Galapinhos.',
                 'Em Azeitão, adegas históricas abrem para provas de moscatel e de vinho da região, e Setúbal é conhecida pelos restaurantes de peixe e pelo choco frito. Com motorista, ninguém tem de ficar de fora da prova.'],
          see=['Portinho da Arrábida e Galapinhos', 'Adegas de Azeitão', 'Setúbal e os restaurantes de peixe', 'Sesimbra'], combo='Combine com a Comporta, do outro lado do Sado.'),
  es=dict(lead='La sierra de la Arrábida y sus playas, a 45 minutos de Lisboa. Un día de mar o una tarde de vino en Azeitão.',
          about=['El parque natural de la Arrábida cae directamente al mar entre Setúbal y Sesimbra, con algunas de las aguas más claras cerca de Lisboa, en Portinho da Arrábida y la playa de Galapinhos.',
                 'En Azeitão, bodegas históricas abren para catas de moscatel y vino de la región, y Setúbal es conocida por sus restaurantes de pescado y el choco frito. Con chófer, nadie tiene que perderse la cata.'],
          see=['Portinho da Arrábida y Galapinhos', 'Bodegas de Azeitão', 'Setúbal y sus restaurantes de pescado', 'Sesimbra'], combo='Combínelo con Comporta, al otro lado del Sado.')),
 'd-obidos': dict(name={'pt': 'Óbidos e Nazaré', 'en': 'Óbidos and Nazaré', 'es': 'Óbidos y Nazaré', 'fr': 'Óbidos et Nazaré'}, km=85, time='1h', img='d-obidos',
  en=dict(lead='The walled town and the giant waves, one hour north of Lisbon. Two of Portugal\'s most photographed places in one day.',
          about=['Óbidos is a medieval walled town of whitewashed houses, climbing roses and the castle at the top; the local ginjinha cherry liqueur is served in a chocolate cup.',
                 'Half an hour further, Nazaré is a fishing town below the Sítio clifftop, where in winter surfers ride some of the biggest waves on the planet at Praia do Norte.'],
          see=['The walls and old town of Óbidos', 'Ginjinha in a chocolate cup', 'The Sítio viewpoint in Nazaré', 'Praia do Norte and the big waves'], combo='Combine with the Batalha or Alcobaça monasteries, or with Fátima.'),
  pt=dict(lead='A vila muralhada e as ondas gigantes, a uma hora de Lisboa. Dois dos lugares mais fotografados do país num só dia.',
          about=['Óbidos é uma vila medieval de casas caiadas, rosas trepadeiras e castelo no alto; a ginjinha da terra bebe-se em copo de chocolate.',
                 'Meia hora adiante, a Nazaré é uma vila de pescadores aos pés do Sítio, onde no inverno se surfam no Norte algumas das maiores ondas do planeta.'],
          see=['As muralhas e o centro de Óbidos', 'Ginjinha em copo de chocolate', 'O miradouro do Sítio, na Nazaré', 'A Praia do Norte e as ondas gigantes'], combo='Combine com os mosteiros da Batalha ou de Alcobaça, ou com Fátima.'),
  es=dict(lead='La villa amurallada y las olas gigantes, a una hora de Lisboa. Dos de los lugares más fotografiados de Portugal en un solo día.',
          about=['Óbidos es una villa medieval de casas encaladas, rosales trepadores y castillo en lo alto; la ginjinha local se bebe en un vasito de chocolate.',
                 'Media hora más allá, Nazaré es un pueblo de pescadores a los pies del Sítio, donde en invierno se surfean en Praia do Norte algunas de las olas más grandes del planeta.'],
          see=['Las murallas y el centro de Óbidos', 'Ginjinha en vasito de chocolate', 'El mirador del Sítio, en Nazaré', 'Praia do Norte y las olas gigantes'], combo='Combínelo con los monasterios de Batalha o Alcobaça, o con Fátima.')),
 'd-douro': dict(name={'pt': 'Vale do Douro', 'en': 'Douro Valley', 'es': 'Valle del Duero', 'fr': 'Vallée du Douro'}, km=380, time='3h30', img='d-douro',
  en=dict(lead='Terraced vineyards along the river, with a driver so the whole group can taste. A long day trip or part of a longer route.',
          about=['The Alto Douro wine region is a UNESCO World Heritage Site: terraced vineyards carved into the hillsides along the river, with historic quintas open for tastings of port and Douro wines.',
                 'Pinhão, with its tiled railway station, and Peso da Régua are the heart of the valley; the viewpoints above the river are among the finest in Portugal. With a driver, nobody misses the tastings.'],
          see=['Quintas and wine tastings', 'Pinhão and its tiled station', 'The viewpoints over the river', 'Peso da Régua and Lamego'], combo='Combine with Porto, an hour and a half from the valley.'),
  pt=dict(lead='Vinhas em socalcos ao longo do rio, com motorista para todo o grupo poder provar. Um dia longo ou parte de uma rota maior.',
          about=['O Alto Douro Vinhateiro é Património Mundial da UNESCO: vinhas em socalcos talhadas nas encostas ao longo do rio, com quintas históricas abertas para provas de vinho do Porto e do Douro.',
                 'O Pinhão, com a estação forrada de azulejos, e o Peso da Régua são o coração do vale; os miradouros sobre o rio estão entre os mais bonitos do país. Com motorista, ninguém fica de fora das provas.'],
          see=['Quintas e provas de vinho', 'O Pinhão e a estação de azulejos', 'Os miradouros sobre o rio', 'Peso da Régua e Lamego'], combo='Combine com o Porto, a hora e meia do vale.'),
  es=dict(lead='Viñedos en terrazas a lo largo del río, con chófer para que todo el grupo pueda catar. Un día largo o parte de una ruta mayor.',
          about=['El Alto Duero vinícola es Patrimonio Mundial de la UNESCO: viñedos en terrazas tallados en las laderas junto al río, con quintas históricas abiertas para catas de oporto y vinos del Duero.',
                 'Pinhão, con su estación revestida de azulejos, y Peso da Régua son el corazón del valle; los miradores sobre el río están entre los más bellos de Portugal. Con chófer, nadie se queda sin catar.'],
          see=['Quintas y catas de vino', 'Pinhão y su estación de azulejos', 'Los miradores sobre el río', 'Peso da Régua y Lamego'], combo='Combínelo con Oporto, a hora y media del valle.')),
}

DL = {  # rótulos comuns às páginas de destino
 'en': dict(title='Private transfer from Lisbon to {nt} · Dark Diamond Luxury',
            desc='Private transfer from Lisbon or Lisbon airport to {nt}, about {t}. One-way, return or a day trip with a driver. Price confirmed before you book.',
            h1='Private transfer from Lisbon to {nt}', about='About {nt}', see='Worth seeing', opts='How to go',
            o=['<b>One-way or return transfer</b>, from the airport, your hotel, the cruise port or any address.', '<b>Day trip</b> with the driver waiting and moving you between stops.', '{combo}'],
            facts='The journey', rows=[('From Lisbon airport', '≈ {km} km'), ('Journey time', '≈ {t}'), ('Vehicle', FLEET['en']), ('Pick-up', 'Airport, hotel, cruise port or any address')],
            note='Indicative times, which may vary.', others='Other destinations', book='Book this transfer', call='Call us',
            cta='Going to {nt}?', ctap='Tell us the date, time and number of passengers. We reply with confirmation and price.'),
 'pt': dict(title='Transfer privado de Lisboa para {nt} · Dark Diamond Luxury',
            desc='Transfer privado de Lisboa ou do aeroporto para {nt}, cerca de {t}. Só ida, ida e volta ou passeio de um dia com motorista. Preço confirmado antes de reservar.',
            h1='Transfer privado de Lisboa para {nt}', about='Sobre {nt}', see='A não perder', opts='Como ir',
            o=['<b>Transfer só de ida ou ida e volta</b>, a partir do aeroporto, do hotel, do porto de cruzeiros ou de qualquer morada.', '<b>Passeio de um dia</b> com o motorista à espera e a levá-lo entre paragens.', '{combo}'],
            facts='A viagem', rows=[('Desde o aeroporto de Lisboa', '≈ {km} km'), ('Duração', '≈ {t}'), ('Veículo', FLEET['pt']), ('Recolha', 'Aeroporto, hotel, porto de cruzeiros ou qualquer morada')],
            note='Tempos indicativos, que podem variar.', others='Outros destinos', book='Reservar este transfer', call='Ligar',
            cta='Vai {ng}?', ctap='Diga-nos a data, a hora e o número de passageiros. Respondemos com a confirmação e o preço.'),
 'es': dict(title='Traslado privado de Lisboa {ng} · Dark Diamond Luxury',
            desc='Traslado privado desde Lisboa o el aeropuerto {ng}, unos {t}. Solo ida, ida y vuelta o excursión de un día con chófer. Precio confirmado antes de reservar.',
            h1='Traslado privado de Lisboa {ng}', about='Sobre {nt}', see='Imprescindibles', opts='Cómo ir',
            o=['<b>Traslado solo ida o ida y vuelta</b>, desde el aeropuerto, el hotel, el puerto de cruceros o cualquier dirección.', '<b>Excursión de un día</b> con el chófer esperando y llevándole entre paradas.', '{combo}'],
            facts='El viaje', rows=[('Desde el aeropuerto de Lisboa', '≈ {km} km'), ('Duración', '≈ {t}'), ('Vehículo', FLEET['es']), ('Recogida', 'Aeropuerto, hotel, puerto de cruceros o cualquier dirección')],
            note='Tiempos orientativos, que pueden variar.', others='Otros destinos', book='Reservar este traslado', call='Llamar',
            cta='¿Va {ng}?', ctap='Díganos la fecha, la hora y el número de pasajeros. Le respondemos con la confirmación y el precio.'),
}


ART = {
    'd-porto': {'pt': {'nt': 'o Porto', 'ng': 'ao Porto'}},
    'd-algarve': {'pt': {'nt': 'o Algarve', 'ng': 'ao Algarve'}, 'en': {'nt': 'the Algarve', 'ng': 'to the Algarve'},
                  'es': {'nt': 'el Algarve', 'ng': 'al Algarve'}},
    'd-arrabida': {'pt': {'nt': 'a Arrábida', 'ng': 'à Arrábida'}, 'en': {'nt': 'the Arrábida', 'ng': 'to the Arrábida'},
                   'es': {'nt': 'la Arrábida', 'ng': 'a la Arrábida'}},
    'd-obidos': {'pt': {'ng': 'a Óbidos e à Nazaré'}},
    'd-douro': {'pt': {'nt': 'o vale do Douro', 'ng': 'ao vale do Douro'}, 'en': {'nt': 'the Douro Valley', 'ng': 'to the Douro Valley'},
                'es': {'nt': 'el valle del Duero', 'ng': 'al valle del Duero'}},
}


def dest_page(key, lang):
    d, l, c = D[key], DL[lang], D[key][lang]
    n = d['name'][lang] if isinstance(d['name'], dict) else d['name']
    # Formas com artigo: "para o Porto", "to the Algarve", "al Algarve"…
    art = ART.get(key, {}).get(lang, {})
    nt = art.get('nt', n)
    ng = art.get('ng', {'pt': f'a {n}', 'es': f'a {n}', 'en': f'to {n}', 'fr': f'à {n}'}[lang])
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
<ul><li>Não usa cookies.</li>
<li>Quando envia o formulário de reserva, guardamos o pedido (serviço, trajeto, data, hora, voo, passageiros, malas, nome, telefone, email e notas) no nosso sistema de gestão de serviços (Supabase), apenas para lhe responder e organizar o serviço. Se não reservar, apagamos o pedido.</li>
<li>O formulário também abre o WhatsApp com a mensagem pronta. O que enviar por lá passa a ser tratado pelo WhatsApp (Meta) e por nós.</li>
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
<ul><li>It does not use cookies.</li>
<li>When you send the booking form, we store the request (service, route, date, time, flight, passengers, luggage, name, phone, email and notes) in our service management system (Supabase), only to reply to you and organise the service. If you do not book, we delete the request.</li>
<li>The form also opens WhatsApp with the message ready. What you send there is processed by WhatsApp (Meta) and by us.</li>
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
<ul><li>No utiliza cookies.</li>
<li>Cuando envía el formulario de reserva, guardamos la solicitud (servicio, trayecto, fecha, hora, vuelo, pasajeros, maletas, nombre, teléfono, email y notas) en nuestro sistema de gestión de servicios (Supabase), solo para responderle y organizar el servicio. Si no reserva, borramos la solicitud.</li>
<li>El formulario también abre WhatsApp con el mensaje listo. Lo que envíe por allí pasa a ser tratado por WhatsApp (Meta) y por nosotros.</li>
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

from services_pages import PAGES_NEW  # noqa: E402
PAGES.update(PAGES_NEW)


# =====================================================================================
# TERMOS E CONDIÇÕES (valores em terms.py; escondida enquanto TERMS['live'] for False)
# =====================================================================================
from terms import terms_html  # noqa: E402
PAGES['terms'] = {
 'en': dict(title='Terms and conditions · Dark Diamond Luxury', desc='Booking, payment, waiting time, cancellation and conduct on board for Dark Diamond Luxury services.', crumb='Terms and conditions', h1='Terms and conditions', lead='The rules for every booking, in plain words.', blocks=[dict(type='prose', html=terms_html('en'))]),
 'pt': dict(title='Termos e condições · Dark Diamond Luxury', desc='Reserva, pagamento, tempo de espera, cancelamento e conduta a bordo nos serviços da Dark Diamond Luxury.', crumb='Termos e condições', h1='Termos e condições', lead='As regras de cada reserva, em palavras simples.', blocks=[dict(type='prose', html=terms_html('pt'))]),
 'es': dict(title='Términos y condiciones · Dark Diamond Luxury', desc='Reserva, pago, tiempo de espera, cancelación y conducta a bordo en los servicios de Dark Diamond Luxury.', crumb='Términos y condiciones', h1='Términos y condiciones', lead='Las reglas de cada reserva, en palabras sencillas.', blocks=[dict(type='prose', html=terms_html('es'))]),
}


# =====================================================================================
# FRANCÊS (4.ª língua): rótulos, destinos e páginas
# =====================================================================================
DL['fr'] = dict(
    title='Transfert privé de Lisbonne {ng} · Dark Diamond Luxury',
    desc="Transfert privé depuis Lisbonne ou l'aéroport {ng}, environ {t}. Aller simple, aller-retour ou excursion d'une journée avec chauffeur. Prix confirmé avant de réserver.",
    h1='Transfert privé de Lisbonne {ng}', about='Découvrir {nt}', see='À ne pas manquer', opts='Comment y aller',
    o=["<b>Transfert aller simple ou aller-retour</b>, depuis l'aéroport, votre hôtel, le port de croisières ou toute adresse.", "<b>Excursion d'une journée</b> avec le chauffeur qui vous attend et vous conduit d'étape en étape.", '{combo}'],
    facts='Le trajet', rows=[("Depuis l'aéroport de Lisbonne", '≈ {km} km'), ('Durée', '≈ {t}'), ('Véhicule', FLEET['fr']), ('Prise en charge', 'Aéroport, hôtel, port de croisières ou toute adresse')],
    note='Temps indicatifs, pouvant varier.', others='Autres destinations', book='Réserver ce transfert', call='Appeler',
    cta='Vous allez {ng} ?', ctap="Indiquez-nous la date, l'heure et le nombre de passagers. Nous répondons avec la confirmation et le prix.")

ART.setdefault('d-algarve', {})['fr'] = {'nt': "l'Algarve", 'ng': 'en Algarve'}
ART.setdefault('d-arrabida', {})['fr'] = {'nt': "l'Arrábida", 'ng': "à l'Arrábida"}
ART.setdefault('d-douro', {})['fr'] = {'nt': 'la vallée du Douro', 'ng': 'dans la vallée du Douro'}
ART.setdefault('d-obidos', {})['fr'] = {'ng': 'à Óbidos et Nazaré'}

D['d-sintra']['fr'] = dict(
    lead="Des palais dans la montagne, à moins d'une heure de l'aéroport. Rejoignez directement votre hôtel à Sintra ou passez-y la journée avec votre chauffeur.",
    about=["Le paysage culturel de Sintra est classé au patrimoine mondial de l'UNESCO : le palais de Pena, la Quinta da Regaleira, le château des Maures et Monserrate parsèment les collines boisées au-dessus de la ville.",
           'Le centre historique a des rues étroites et très fréquentées. Votre chauffeur vous dépose au plus près de chaque entrée et vous reprend où vous le souhaitez.'],
    see=['Palais de Pena', 'Quinta da Regaleira', 'Château des Maures', 'Palais de Monserrate'], combo='À combiner avec le cap de Roca et Cascais au retour.')
D['d-cascais']['fr'] = dict(
    lead="La ville balnéaire à l'ouest de Lisbonne, sur la côte d'Estoril. Un transfert direct vers votre hôtel ou une journée tranquille au bord de la mer.",
    about=["De village de pêcheurs, Cascais est devenue une station balnéaire, avec une marina, des plages et un centre ancien qui se parcourt à pied. La route le long de la côte d'Estoril est l'une des plus belles de la région de Lisbonne.",
           "Depuis Cascais, la Boca do Inferno et le cap de Roca, le point le plus occidental de l'Europe continentale, sont tout proches."],
    see=['Vieille ville et marina de Cascais', 'Boca do Inferno', 'Cap de Roca', 'Estoril et son casino'], combo="À combiner avec Sintra pour une journée complète à l'ouest de Lisbonne.")
D['d-arrabida']['fr'] = dict(
    lead="La serra da Arrábida et ses plages, à 45 minutes de Lisbonne. Une journée de mer ou un après-midi de vin à Azeitão.",
    about=["Le parc naturel de l'Arrábida plonge droit dans la mer entre Setúbal et Sesimbra, avec certaines des eaux les plus claires des environs de Lisbonne, à Portinho da Arrábida et à la plage de Galapinhos.",
           "À Azeitão, des caves historiques ouvrent leurs portes pour des dégustations de moscatel et de vins de la région, et Setúbal est connue pour ses restaurants de poisson. Avec un chauffeur, personne ne manque la dégustation."],
    see=['Portinho da Arrábida et Galapinhos', "Caves d'Azeitão", 'Setúbal et ses restaurants de poisson', 'Sesimbra'], combo="À combiner avec Comporta, de l'autre côté du Sado.")
D['d-obidos']['fr'] = dict(
    lead='La cité fortifiée et les vagues géantes, à une heure de Lisbonne. Deux des lieux les plus photographiés du Portugal en une seule journée.',
    about=["Óbidos est une cité médiévale de maisons blanchies à la chaux, de rosiers grimpants et d'un château qui la domine ; la ginjinha locale se boit dans un petit verre en chocolat.",
           "Une demi-heure plus loin, Nazaré est un village de pêcheurs au pied du promontoire du Sítio, où l'hiver les surfeurs affrontent à Praia do Norte certaines des plus grandes vagues de la planète."],
    see=["Les remparts et le centre d'Óbidos", 'La ginjinha en verre de chocolat', 'Le belvédère du Sítio, à Nazaré', 'Praia do Norte et les vagues géantes'], combo="À combiner avec les monastères de Batalha ou d'Alcobaça, ou avec Fátima.")
D['d-comporta']['fr'] = dict(
    lead="Rizières, pinèdes et longues plages désertes sur la côte de l'Alentejo. Porte à porte depuis l'aéroport ou depuis Lisbonne.",
    about=["Comporta est un coin paisible du littoral de l'Alentejo au sud de Setúbal, connu pour ses plages, ses rizières, ses petits villages et ses hôtels design.",
           'Nous vous conduisons porte à porte, avec de la place pour les affaires de plage, et revenons vous chercher le jour de votre choix.'],
    see=['Plages de Comporta et de Carvalhal', 'Rizières et cigognes', 'Péninsule de Tróia', 'Alcácer do Sal'], combo="À combiner avec un arrêt à Setúbal ou dans l'Arrábida.")
D['d-evora']['fr'] = dict(
    lead="Une ville fortifiée au cœur de l'Alentejo. Une excursion d'une journée avec chauffeur, ou un transfert vers votre hôtel ou votre domaine viticole.",
    about=["Le centre historique d'Évora est classé au patrimoine mondial de l'UNESCO : un temple romain, une cathédrale gothique et la chapelle des Os à l'intérieur des remparts.",
           "Tout autour, c'est le pays du vin. Votre chauffeur vous emmène dans les domaines pour des dégustations, pour que personne du groupe n'ait à conduire."],
    see=['Temple romain', "Cathédrale d'Évora", 'Chapelle des Os', "Domaines viticoles de l'Alentejo"], combo='À combiner avec Monsaraz ou Arraiolos.')
D['d-fatima']['fr'] = dict(
    lead="Le sanctuaire de Fátima, l'un des lieux de pèlerinage les plus visités d'Europe. Excursion d'une journée ou transfert, à votre rythme.",
    about=['Le sanctuaire de Notre-Dame de Fátima accueille des pèlerins du monde entier, surtout autour du 13 de chaque mois, de mai à octobre.',
           'La route vers le nord passe par quelques-unes des villes les plus connues du centre du Portugal : la journée peut inclure Batalha, Nazaré ou Óbidos.'],
    see=['Sanctuaire de Fátima', 'Monastère de Batalha', 'Nazaré', 'Óbidos'], combo='À combiner avec Batalha, Nazaré et Óbidos le même jour.')
D['d-algarve']['fr'] = dict(
    lead='De Lisbonne aux plages du sud, porte à porte. Sans voiture de location et sans vol de correspondance.',
    about=["L'Algarve s'étend le long de la côte sud du Portugal, de Sagres à la frontière espagnole. Les stations centrales comme Albufeira et Vilamoura sont à environ 2h45 de l'aéroport de Lisbonne.",
           "Un transfert privé est souvent plus simple qu'une correspondance ou une voiture de location, surtout pour les familles et les groupes chargés. Nous pouvons nous arrêter en chemin."],
    see=['Albufeira', 'Vilamoura', 'Lagos et Ponta da Piedade', 'Faro'], combo='Arrêt possible à Comporta ou à Évora en descendant.')
D['d-porto']['fr'] = dict(
    lead='De Lisbonne à Porto porte à porte, avec des arrêts où vous voulez. Une alternative confortable au train pour les familles et les groupes.',
    about=["La Ribeira de Porto est classée au patrimoine mondial de l'UNESCO, et les caves de porto se trouvent juste en face, à Vila Nova de Gaia. En amont, le Douro est l'une des plus anciennes régions viticoles du monde.",
           'Le trajet dure environ trois heures. Beaucoup de voyageurs font étape à Coimbra, Aveiro ou Fátima.'],
    see=['La Ribeira et les quais du Douro', 'Les caves de porto à Gaia', 'La vallée du Douro', 'Coimbra et Aveiro en chemin'], combo='Arrêt possible à Coimbra, Aveiro ou Fátima en chemin.')
D['d-douro']['fr'] = dict(
    lead="Des vignes en terrasses le long du fleuve, avec un chauffeur pour que tout le groupe puisse déguster. Une longue journée, ou l'étape d'un itinéraire plus vaste.",
    about=["Le Haut-Douro viticole est classé au patrimoine mondial de l'UNESCO : des vignes en terrasses taillées dans les versants le long du fleuve, et des quintas historiques ouvertes pour des dégustations de porto et de vins du Douro.",
           'Pinhão, avec sa gare aux azulejos, et Peso da Régua sont le cœur de la vallée ; les belvédères au-dessus du fleuve comptent parmi les plus beaux du Portugal. Avec un chauffeur, personne ne manque les dégustations.'],
    see=['Quintas et dégustations', 'Pinhão et sa gare aux azulejos', 'Les belvédères sur le fleuve', 'Peso da Régua et Lamego'], combo='À combiner avec Porto, à une heure et demie de la vallée.')
D['d-madrid']['fr'] = dict(
    lead="De Lisbonne à Madrid porte à porte, par l'Alentejo et l'Estrémadure. Sans enregistrement, sans limite de bagages, avec des arrêts où vous voulez.",
    about=["Madrid est la capitale de l'Espagne. Les musées du Prado, Reina Sofía et Thyssen bordent le Paseo del Prado, classé avec le parc du Retiro au patrimoine mondial de l'UNESCO.",
           "Le trajet dure environ six heures. La route passe par Elvas, Badajoz et Mérida, dont le théâtre romain est l'un des mieux conservés d'Espagne : l'occasion d'une étape."],
    see=['Musée du Prado', 'Palais royal', 'Parc du Retiro', 'Gran Vía'], combo='Arrêt possible à Elvas, Mérida ou Trujillo en chemin.')
D['d-sevilla']['fr'] = dict(
    lead="De Lisbonne à Séville porte à porte, par l'Algarve et le pont du Guadiana. Une alternative privée au vol de correspondance.",
    about=["La cathédrale, l'Alcázar et les Archives des Indes de Séville forment un ensemble classé au patrimoine mondial de l'UNESCO, au cœur de la vieille ville. De l'autre côté du fleuve, Triana est connue pour sa céramique et son flamenco.",
           "Le trajet dure environ quatre heures et entre en Espagne par le Guadiana : l'Algarve est une étape toute trouvée."],
    see=['Cathédrale et Giralda', 'Real Alcázar', 'Plaza de España', 'Triana'], combo='Arrêt possible en Algarve ou à Évora en chemin.')
D['d-marbella']['fr'] = dict(
    lead='De Lisbonne à la Costa del Sol porte à porte. Une voiture, un chauffeur, et vos bagages avec vous tout du long.',
    about=['Marbella se trouve sur la Costa del Sol, entre Málaga et Gibraltar, avec une vieille ville blanchie autour de la Plaza de los Naranjos et la marina de Puerto Banús.',
           "Le trajet dure environ cinq heures et demie, en passant par Séville, étape toute naturelle. Ronda, dans la montagne au-dessus de la côte, est à une heure vers l'intérieur."],
    see=['Vieille ville et Plaza de los Naranjos', 'Puerto Banús', 'La Milla de Oro', 'Ronda'], combo='Arrêt possible à Séville en chemin.')

for _k in DESTS:
    PAGES[_k]['fr'] = dest_page(_k, 'fr')

PAGES['airport']['fr'] = dict(
  title='Transfert aéroport de Lisbonne · Dark Diamond Luxury',
  desc="Transfert privé depuis l'aéroport de Lisbonne vers votre hôtel ou tout point du pays. Suivi du vol, accueil avec votre nom, prix confirmé avant de réserver.",
  crumb='Transfert aéroport de Lisbonne', h1="Transferts de l'aéroport de Lisbonne, accueilli par votre nom.", img='plane',
  lead="Transfert privé depuis l'aéroport Humberto Delgado (LIS) vers votre hôtel, votre domicile ou tout point du pays. Le chauffeur suit votre vol et vous attend aux arrivées avec votre nom.",
  ctas=[('book', 'Réserver un transfert'), ('tel', 'Appeler')],
  blocks=[
   dict(type='split', h='Comment ça marche ?', steps=[
     ['Réservez', 'Envoyez-nous le numéro de vol, la destination et le nombre de passagers et de valises. Nous répondons avec la confirmation et le prix.'],
     ['Nous suivons le vol', "Si le vol arrive en avance ou en retard, le chauffeur s'adapte à l'heure réelle d'atterrissage."],
     ['Accueil aux arrivées', 'Le chauffeur vous attend dans la zone des arrivées du Terminal 1 ou 2, avec une pancarte à votre nom.'],
     ['Directement à destination', 'Aide avec les bagages et trajet direct, sans arrêts partagés.']]),
   dict(type='split', bg='bone', h="Temps de trajet depuis l'aéroport", rows=[
     ['Baixa · Chiado', '20 min'], ['Belém', '25 min'], ['Parque das Nações', '10 min'], ['Cascais', '35 min'], ['Sintra', '35 min'],
     ['Comporta', '1h15'], ['Évora', '1h30'], ['Fátima', '1h30'], ['Algarve', '2h45'], ['Porto', '3h']],
     after=['Temps indicatifs, pouvant varier.']),
   dict(type='split', h='Bon à savoir', ticks=[
     'Véhicule privé rien que pour votre groupe : pas de navettes partagées.',
     "Sièges enfants sur demande : indiquez l'âge des enfants en réservant.",
     "Aussi pour les départs : prise en charge à l'hôtel à l'heure de votre choix.",
     'Des chauffeurs qui parlent français, anglais, espagnol et portugais.',
     'Disponible 24/7, à toute heure du vol.',
     'Prix confirmé par écrit avant de réserver.'], related=list(DESTS)),
   dict(type='cta', h='Vous atterrissez bientôt ?', p='Envoyez-nous le vol et la destination. Nous répondons avec la confirmation et le prix.', ctas=[('book', 'Réserver un transfert'), ('tel', 'Appeler')]),
  ])

PAGES['cruise']['fr'] = dict(
  title='Transferts au terminal de croisières de Lisbonne · Dark Diamond Luxury',
  desc="Transferts privés entre les terminaux de croisières de Lisbonne, l'aéroport et les hôtels, et excursions à Sintra, Cascais et Lisbonne, réglées sur l'heure de retour à bord.",
  crumb='Terminal de croisières de Lisbonne', h1='Transferts au port de croisières de Lisbonne et excursions à terre.', img='cruise',
  lead="Du navire à l'aéroport, à l'hôtel ou en tour privé, au rythme de l'escale. Pour les passagers, les agences et les compagnies de croisière.",
  ctas=[('book', 'Réserver un transfert'), ('agencies', 'Pour les agences et compagnies')],
  blocks=[
   dict(type='split', h='Ce que nous faisons au port', ticks=[
     "<b>Port et aéroport.</b> Transferts le jour de l'embarquement et du débarquement.",
     '<b>Port et hôtel.</b> Pour les séjours avant ou après la croisière.',
     "<b>Excursions privées à terre.</b> Lisbonne, Sintra, Cascais ou Fátima, avec un chauffeur qui planifie le retour selon l'heure d'embarquement.",
     '<b>Groupes.</b> Classe V, Sprinter et minibus de 19 places, avec de la place pour les bagages.']),
   dict(type='split', bg='bone', h='Les terminaux de croisières de Lisbonne', p=[
     "La plupart des navires accostent au Terminal de croisières de Lisbonne, près de Santa Apolónia et de l'Alfama, proche du centre et à une vingtaine de minutes de l'aéroport.",
     "Certains navires utilisent les terminaux d'Alcântara ou de Rocha Conde de Óbidos, plus à l'ouest. Donnez-nous le nom du navire et nous attendrons au bon endroit."]),
   dict(type='split', h="De retour à bord à l'heure", p=[
     "Pour les excursions à terre, nous planifions la journée à partir de l'heure de retour à bord, avec de la marge pour la circulation. Vous aurez le numéro du chauffeur et lui le vôtre."]),
   dict(type='cta', h='Escale à Lisbonne ?', p='Indiquez-nous le navire, la date et vos envies. Nous répondons avec un plan et un prix.', ctas=[('book', 'Réserver un transfert'), ('tel', 'Appeler')]),
  ])

PAGES['agencies']['fr'] = dict(
  title='Partenaire de transport pour agences au Portugal · Dark Diamond Luxury',
  desc='Transferts privés, tours et chauffeur pour agences, tour-opérateurs, DMC et compagnies de croisière au Portugal, en Espagne et en France. RNAAT 682/2022.',
  crumb='Agences et partenaires', h1='Votre partenaire au sol, au Portugal.',
  lead='Transferts privés, tours et services avec chauffeur pour agences de voyages, tour-opérateurs, DMC et compagnies de croisière. Portugal, Espagne et France.',
  subject='Demande de partenariat / tarifs', ctas=[('mail', 'Demander nos tarifs'), ('tel', 'Appeler')],
  blocks=[
   dict(type='split', h='Pourquoi travailler avec nous', ticks=[
     "<b>Enregistrés auprès de Turismo de Portugal.</b> Agent d'animation touristique, RNAAT nº 682/2022.",
     "<b>Assurés.</b> Assurances de responsabilité civile et d'accidents personnels en vigueur.",
     "<b>Suivi des vols et accueil avec pancarte.</b> Votre client est accueilli aux arrivées avec son nom, à l'heure réelle d'atterrissage.",
     "<b>Contact direct, 24/7.</b> Vous parlez à la personne qui planifie et dispatche le service, pas à un centre d'appels.",
     '<b>Des chauffeurs qui parlent la langue du client.</b> Portugais, anglais, espagnol et français.',
     "<b>D'un passager aux groupes de 19.</b> Mercedes-Benz Classe S, Classe E et Classe V, Sprinter et minibus de 19 places.",
     '<b>Confirmation par écrit.</b> Chaque réservation est confirmée par écrit et les coordonnées du chauffeur sont envoyées avant le service.']),
   dict(type='split', bg='bone', h='Où nous travaillons', p=[
     "Basés à Lisbonne, des services réguliers dans tout le pays et des transferts longue distance vers l'Espagne et la France."], ticks=[
     'Aéroport de Lisbonne, hôtels de la ville et terminaux de croisières', "Sintra, Cascais et la côte d'Estoril",
     "Comporta et le littoral de l'Alentejo", "Évora et l'Alentejo", 'Fátima, Óbidos, Nazaré et Batalha',
     'Porto et la vallée du Douro', 'Algarve', 'Espagne et France, sur demande']),
   dict(type='split', h='Comment ça marche', steps=[
     ['Envoyez la réservation', 'Par email ou WhatsApp : nom du passager, date, vol ou heure de prise en charge, nombre de passagers et de valises.'],
     ['Nous confirmons', 'Disponibilité et prix confirmés par écrit, rapidement et à toute heure.'],
     ['Avant le service', 'Vous recevez le nom et le téléphone du chauffeur, ainsi que le véhicule.'],
     ['Le jour même', 'Accueil avec pancarte, suivi du vol et contact direct avec le chauffeur. Si quelque chose change, nous prévenons aussitôt.'],
     ['Facturation', 'Au service ou mensuelle, selon accord. Factures émises par Artur Danilo, Unipessoal Lda, NIPC 515565458.']]),
   dict(type='split', bg='alt', h='Services', ticks=[
     'Transferts aéroport et port de croisières', "Chauffeur à disposition, à l'heure ou à la journée",
     "Tours privés et excursions d'une journée", 'Événements, mariages et groupes',
     "Longue distance au Portugal et vers l'Espagne et la France"]),
   dict(type='split', h="Données de l'entreprise", rows=[
     ['Nom commercial', 'Dark Diamond Luxury'], ['Raison sociale', LEGAL['name']], ['NIPC', LEGAL['nipc']],
     ['Siège', ADDR], ['Registre du tourisme', f"RNAAT {LEGAL['rnaat']}"],
     ['Assurances', 'Responsabilité civile · Accidents personnels'], ['Flotte', FLEET['fr']],
     ['Langues des chauffeurs', 'Portugais, anglais, espagnol et français'], ['Fonctionnement', '24 h/24, 7 j/7'],
     ['Zone couverte', 'Portugal, Espagne et France'], ['Contact', f'{EMAIL}<br>{PH}']]),
   dict(type='cta', h='Travaillons ensemble.', p='Envoyez-nous vos routes et volumes habituels : nous préparons une grille tarifaire pour votre agence.', ctas=[('mail', 'Demander nos tarifs'), ('tel', 'Appeler')]),
  ])

PAGES['legal']['fr'] = dict(
  title='Mentions légales · Dark Diamond Luxury', desc=f'Identification de {LEGAL["name"]} (Dark Diamond Luxury), réclamations et résolution des litiges.',
  crumb='Mentions légales', h1='Mentions légales', lead=f'Dark Diamond Luxury · {LEGAL["name"]}',
  blocks=[dict(type='prose', html=f"""<h2>Identification de l'entreprise</h2>
<p><b>Dark Diamond Luxury</b> est le nom commercial de <b>{LEGAL["name"]}</b>, société unipersonnelle à responsabilité limitée de droit portugais, dont le siège est situé {ADDR}, Portugal, immatriculée au registre du commerce sous le numéro unique d'immatriculation et d'identification fiscale {LEGAL["nipc"]}, au capital social de {LEGAL["capital"]}.</p>
<p>Agent d'animation touristique enregistré auprès de Turismo de Portugal, RNAAT nº {LEGAL["rnaat"]}. Assurances de responsabilité civile et d'accidents personnels en vigueur.</p>
<h2>Contact</h2>
<p>Email : <a href="mailto:{EMAIL}">{EMAIL}</a><br>Téléphone : {PH}</p>
<h2>Livre de réclamations</h2>
<p>Vous pouvez déposer une réclamation sur le <a href="https://www.livroreclamacoes.pt" rel="noopener">Livre de réclamations électronique (Livro de Reclamações)</a>.</p>
<h2>Résolution alternative des litiges</h2>
<p>En cas de litige de consommation, le consommateur peut s'adresser au Centre d'arbitrage des conflits de consommation de Lisbonne (<a href="https://www.centroarbitragemlisboa.pt" rel="noopener">www.centroarbitragemlisboa.pt</a>).</p>
<h2>Photographies</h2>
<p>Les photographies de ce site sont illustratives et utilisées dans le cadre de la licence Unsplash. Les auteurs sont crédités en bas de page.</p>""")])

PRIV['fr'] = f"""<p>Dernière mise à jour : octobre 2026.</p>
<h2>Qui est responsable de vos données</h2>
<p>{LEGAL["name"]} (Dark Diamond Luxury), NIPC {LEGAL["nipc"]}, {ADDR}. Contact : <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Ce site</h2>
<ul><li>N'utilise pas de cookies.</li>
<li>Quand vous envoyez le formulaire de réservation, nous enregistrons la demande (service, trajet, date, heure, vol, passagers, bagages, nom, téléphone, email et notes) dans notre système de gestion des services (Supabase), uniquement pour vous répondre et organiser le service. Sans réservation, la demande est supprimée.</li>
<li>Le formulaire ouvre aussi WhatsApp avec le message prêt. Ce que vous y envoyez est traité par WhatsApp (Meta) et par nous.</li>
<li>Nous comptons les visites de façon anonyme avec GoatCounter, sans cookies et sans identifier les visiteurs.</li></ul>
<h2>Quand vous réservez un service</h2>
<p>Nous traitons le nom, le contact, les données du vol, les adresses de prise en charge et de destination, le nombre de passagers et vos notes, pour assurer le service (exécution du contrat) et respecter nos obligations fiscales et comptables. Les données nécessaires sont partagées avec le chauffeur qui effectue le service. Si la réservation vient d'une agence ou d'un partenaire, nous recevons ces données de leur part.</p>
<p>Nous conservons les données tant qu'elles sont nécessaires au service, puis pendant la durée exigée par la loi à des fins fiscales.</p>
<h2>App interne Despacho</h2>
<p>L'équipe et les chauffeurs utilisent une app interne pour organiser les services. La position des chauffeurs n'est enregistrée que lorsqu'ils mettent à jour l'état d'un service, et seule la direction peut la voir. Les agences et partenaires n'y ont jamais accès.</p>
<h2>Vos droits</h2>
<p>Vous pouvez demander l'accès, la rectification, l'effacement, la limitation ou la portabilité de vos données, ou vous opposer à leur traitement, via <a href="mailto:{EMAIL}">{EMAIL}</a>. Vous pouvez aussi déposer plainte auprès de la Comissão Nacional de Proteção de Dados (<a href="https://www.cnpd.pt" rel="noopener">www.cnpd.pt</a>).</p>"""
PAGES['privacy']['fr'] = dict(
  title='Politique de confidentialité · Dark Diamond Luxury', desc='Comment Dark Diamond Luxury traite les données personnelles sur ce site, dans les réservations et dans son app interne.',
  crumb='Confidentialité', h1='Politique de confidentialité', lead='Ce que nous collectons, pourquoi, et vos droits.',
  blocks=[dict(type='prose', html=PRIV['fr'])])

PAGES['support']['fr'] = dict(
  title="Assistance de l'app Despacho · Dark Diamond Luxury",
  desc="Despacho est l'application interne de l'équipe et des chauffeurs de Dark Diamond Luxury.",
  crumb="Assistance de l'app", h1="Assistance de l'app Despacho", lead="Despacho est l'application interne de l'équipe et des chauffeurs de Dark Diamond Luxury.",
  blocks=[dict(type='prose', html=f"<h2>Besoin d'aide ?</h2><p>Pour tout problème d'accès, de mot de passe ou de fonctionnement de l'app, contactez-nous :</p><p>Email : <a href=\"mailto:{EMAIL}\">{EMAIL}</a><br>Téléphone : {PH}</p><p>L'accès à l'app est créé par la direction. Si vous êtes chauffeur et n'avez pas encore d'accès, parlez-en au bureau.</p>")])

PAGES['terms']['fr'] = dict(
  title='Conditions générales · Dark Diamond Luxury',
  desc="Réservation, paiement, temps d'attente, annulation et conduite à bord pour les services Dark Diamond Luxury.",
  crumb='Conditions générales', h1='Conditions générales', lead='Les règles de chaque réservation, en mots simples.',
  blocks=[dict(type='prose', html=terms_html('fr'))])


PAGES['chauffeur']['fr'] = dict(
  title='Chauffeur à disposition à Lisbonne et au Portugal · Dark Diamond Luxury',
  desc="Chauffeur et voiture privés à votre disposition à Lisbonne et dans tout le pays, à l'heure ou à la journée. Réunions, shopping, tours et soirées.",
  crumb='Chauffeur à disposition', h1="Un chauffeur à votre disposition, à l'heure ou à la journée.", img='van',
  lead='Un chauffeur et une voiture rien que pour vous : réunions, shopping ou une journée sans regarder la montre.',
  ctas=[('book', 'Réserver un chauffeur'), ('tel', 'Appeler')],
  blocks=[
   dict(type='split', h='Comment ça marche ?', steps=[
     ['Choisissez le jour et les heures', 'Date, heure de début, durée prévue et point de départ.'],
     ['Confirmation par écrit', 'Disponibilité et prix confirmés par écrit avant le service.'],
     ['Le chauffeur reste avec vous', 'Le même chauffeur et la même voiture pendant tout le service, qui vous attend où vous le souhaitez.'],
     ['Itinéraire flexible', 'Des arrêts et des changements tout au long de la journée, sans complications.']]),
   dict(type='split', bg='bone', h='À quoi ça sert', ticks=[
     "Réunions d'affaires et trajets entre bureaux", 'Shopping et journées en ville', 'Plusieurs visites en une seule journée',
     "Dîners et événements, avec retour à l'heure", 'Cadres, délégations et invités']),
   dict(type='split', h='Bon à savoir', ticks=[
     'Véhicule privé rien que pour vous et votre groupe.', 'Mercedes-Benz Classe S, Classe E et Classe V, Sprinter et minibus de 19 places.',
     'Des chauffeurs qui parlent français, anglais, espagnol et portugais.', 'Disponible 24/7.', 'Prix confirmé par écrit avant de réserver.']),
   dict(type='cta', h="Besoin d'un chauffeur ?", p='Indiquez la date, les heures et le point de départ. Nous répondons avec la confirmation et le prix.', ctas=[('book', 'Réserver un chauffeur'), ('tel', 'Appeler')]),
  ])

PAGES['tours']['fr'] = dict(
  title='Tours privés au Portugal avec chauffeur · Dark Diamond Luxury',
  desc="Excursions privées d'une journée au départ de Lisbonne : Sintra, Cascais, Fátima, Évora, le Douro et plus encore, avec un chauffeur rien que pour vous et des arrêts où vous voulez.",
  crumb='Tours privés', h1='Tours privés au Portugal, à votre rythme.', img='d-sintra',
  lead='Sintra, Cascais, Fátima, Évora ou le Douro, avec un chauffeur rien que pour vous et des arrêts où vous voulez.',
  ctas=[('book', 'Réserver un tour'), ('tel', 'Appeler')],
  blocks=[
   dict(type='split', h='Comment ça marche ?', steps=[
     ['Choisissez la destination', 'Choisissez un lieu de la liste ou demandez une suggestion.'],
     ['Confirmation par écrit', 'Horaires et prix confirmés par écrit.'],
     ["Prise en charge à l'hôtel", "Le chauffeur vient vous chercher à l'heure et au lieu convenus."],
     ['Des arrêts à votre mesure', 'Le temps passé à chaque étape dépend de vous, et la journée est planifiée en conséquence.']]),
   dict(type='split', bg='bone', h='Tours les plus demandés', ticks=[
     'Sintra et le cap de Roca', "Cascais et la côte d'Estoril", 'Fátima, Nazaré et Óbidos', "Évora et l'Alentejo",
     'La vallée du Douro', "Comporta et le littoral de l'Alentejo", "L'Algarve"]),
   dict(type='split', h='Bon à savoir', ticks=[
     'Véhicule privé rien que pour votre groupe : pas de tours partagés.', "D'un passager aux groupes de 19.",
     "Sièges enfants sur demande : indiquez l'âge des enfants en réservant.",
     'Des chauffeurs qui parlent français, anglais, espagnol et portugais.', 'Prix confirmé par écrit avant de réserver.'], related=list(DESTS)),
   dict(type='cta', h='Vous préparez une excursion ?', p='Dites-nous où vous aimeriez aller et quand. Nous répondons avec un plan et un prix.', ctas=[('book', 'Réserver un tour'), ('tel', 'Appeler')]),
  ])

PAGES['events']['fr'] = dict(
  title='Transport pour événements et mariages au Portugal · Dark Diamond Luxury',
  desc="Transport avec chauffeur pour grands événements, événements d'entreprise comme le Web Summit, sport professionnel, golf et mariages au Portugal.",
  crumb='Événements et mariages', h1="Événements et mariages, un transport à l'heure.", img='events',
  lead="Des invités accueillis et conduits à l'heure, avec la coordination assurée par nous.",
  subject='Transport pour événement / mariage', ctas=[('mail', 'Demander une proposition'), ('tel', 'Appeler')],
  blocks=[
   dict(type='split', h='Les événements que nous accompagnons', ticks=[
     '<b>Grands événements.</b> Conférences et salons internationaux, comme le Web Summit.',
     "<b>Événements d'entreprise.</b> Réunions, conventions, lancements et voyages incentive.",
     "<b>Sport professionnel.</b> Équipes, organisations et invités lors d'événements sportifs professionnels.",
     '<b>Golf.</b> Tournois et voyages de golf, avec de la place pour les sacs.',
     '<b>Mariages.</b> Mariés et invités, de la cérémonie au lieu de réception et retour.']),
   dict(type='split', bg='bone', h='Notre façon de travailler', ticks=[
     "Un seul contact pour toute l'opération.", "Des horaires définis avec l'organisation.",
     'Des véhicules pour groupes : Classe V, Sprinter et minibus de 19 places.',
     "Autant de véhicules que le nombre d'invités l'exige.",
     'Des chauffeurs qui parlent français, anglais, espagnol et portugais.']),
   dict(type='split', h='Comment ça marche ?', steps=[
     ["Envoyez les données de l'événement", "Dates, lieux et nombre d'invités prévu."],
     ['Proposition et prix', 'Envoyés par écrit, avec les véhicules et les horaires.'],
     ["Planification avec l'organisation", "Prises en charge, trajets et horaires définis à l'avance."],
     ['Le jour même', 'Coordination directe avec les chauffeurs, pour traiter tout changement immédiatement.']]),
   dict(type='cta', h='Vous préparez un événement ?', p="Envoyez les dates, les lieux et le nombre d'invités. Nous répondons avec une proposition.", ctas=[('mail', 'Demander une proposition'), ('tel', 'Appeler')]),
  ])

PAGES['longdistance']['fr'] = dict(
  title='Transferts longue distance · Dark Diamond Luxury',
  desc="Transferts privés porte à porte de Lisbonne vers Porto, l'Algarve, Madrid, Séville, Marbella et la France, en véhicule privé avec chauffeur professionnel.",
  crumb='Longue distance', h1='Transferts longue distance, porte à porte.', img='longdist',
  lead='Porto, Algarve, Espagne et France, porte à porte, en véhicule privé.',
  ctas=[('book', 'Réserver un transfert'), ('tel', 'Appeler')],
  blocks=[
   dict(type='split', h='Routes habituelles', ticks=[
     'Lisbonne – Porto et vallée du Douro', 'Lisbonne – Algarve', 'Lisbonne – Madrid', 'Lisbonne – Séville',
     'Lisbonne – Marbella', 'France, sur demande'], related=['d-porto', 'd-douro', 'd-algarve', 'd-madrid', 'd-sevilla', 'd-marbella']),
   dict(type='split', bg='bone', h='Comment ça marche ?', steps=[
     ['Envoyez le trajet', 'Origine, destination, date, heure, nombre de passagers et de valises.'],
     ['Confirmation par écrit', 'Prix et horaires confirmés par écrit avant de réserver.'],
     ['Voyage porte à porte', "Véhicule privé, de l'adresse de prise en charge à la destination finale."],
     ['Arrêts convenus', "Des pauses en chemin, convenues à l'avance avec le chauffeur."]]),
   dict(type='split', h='Bon à savoir', ticks=[
     'Véhicule privé rien que pour vous et votre groupe.', 'Mercedes-Benz Classe S, Classe E et Classe V, Sprinter et minibus de 19 places.',
     'Des chauffeurs qui parlent français, anglais, espagnol et portugais.', 'Disponible 24/7.', 'Prix confirmé par écrit avant de réserver.']),
   dict(type='cta', h='Un long voyage en vue ?', p='Indiquez le trajet, la date et le nombre de passagers. Nous répondons avec la confirmation et le prix.', ctas=[('book', 'Réserver un transfert'), ('tel', 'Appeler')]),
  ])
