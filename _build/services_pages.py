# Páginas "Saber mais" dos serviços: motorista à disposição, tours, eventos e casamentos, longa distância.
# Mesma estrutura das páginas do aeroporto e dos cruzeiros. Tratamento por "você" (PT) e "usted" (ES).
from config import DESTS

PAGES_NEW = {}


def steps_block(h, steps):
    return dict(type='split', h=h, steps=steps)


# =====================================================================================
# MOTORISTA À DISPOSIÇÃO
# =====================================================================================
PAGES_NEW['chauffeur'] = {
 'en': dict(
  title='Chauffeur at Disposal in Lisbon and Portugal · Dark Diamond Luxury',
  desc='A private chauffeur and car at your disposal in Lisbon and across Portugal, by the hour or by the day. Meetings, shopping, tours and evenings out.',
  crumb='Chauffeur at disposal', h1='A chauffeur at your disposal, by the hour or by the day.', img='van',
  lead='A driver and a car just for you: meetings, shopping or a day without looking at the clock.',
  ctas=[('book', 'Book a chauffeur'), ('tel', 'Call')],
  blocks=[
   dict(type='split', h='How it works', steps=[
     ('Choose the day and hours', 'Date, start time, expected duration and starting point.'),
     ('Written confirmation', 'Availability and price are confirmed in writing before the service.'),
     ('The driver stays with you', 'The same driver and the same car throughout, waiting wherever you agree.'),
     ('A flexible route', 'Stops and changes during the day, without fuss.')]),
   dict(type='split', bg='bone', h='What it is for', ticks=[
     'Business meetings and trips between offices', 'Shopping and days in the city', 'Several visits in a single day',
     'Dinners and events, with a timely return', 'Executives, delegations and guests']),
   dict(type='split', h='Good to know', ticks=[
     'A private vehicle just for you and your group.', 'Mercedes-Benz S-Class, E-Class and V-Class, Sprinter and a 19-seat minibus.',
     'Drivers who speak Portuguese, English, Spanish and French.', 'Available 24/7.', 'Price confirmed in writing before you book.']),
   dict(type='cta', h='Need a chauffeur?', p='Tell us the date, the hours and the starting point. We reply with confirmation and price.', ctas=[('book', 'Book a chauffeur'), ('tel', 'Call')]),
  ]),
 'pt': dict(
  title='Motorista à Disposição em Lisboa e Portugal · Dark Diamond Luxury',
  desc='Motorista e carro privados à sua disposição em Lisboa e em todo o país, à hora ou ao dia. Reuniões, compras, tours e serões.',
  crumb='Motorista à disposição', h1='Motorista à sua disposição, à hora ou ao dia.', img='van',
  lead='Um motorista e um carro só para si: reuniões, compras ou um dia sem olhar para o relógio.',
  ctas=[('book', 'Reservar motorista'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Como funciona?', steps=[
     ('Escolha o dia e as horas', 'Data, hora de início, duração prevista e ponto de partida.'),
     ('Confirmação por escrito', 'Disponibilidade e preço são confirmados por escrito antes do serviço.'),
     ('O motorista fica consigo', 'O mesmo motorista e o mesmo carro durante todo o serviço, à espera onde combinarem.'),
     ('Itinerário flexível', 'Paragens e alterações ao longo do dia, sem complicações.')]),
   dict(type='split', bg='bone', h='Para que serve', ticks=[
     'Reuniões de negócios e deslocações entre escritórios', 'Compras e dias na cidade', 'Várias visitas num só dia',
     'Jantares e eventos, com regresso a horas', 'Executivos, delegações e convidados']),
   dict(type='split', h='Bom saber', ticks=[
     'Veículo privado só para si e para o seu grupo.', 'Mercedes-Benz Classe S, Classe E e Classe V, Sprinter e minibus de 19 lugares.',
     'Motoristas que falam português, inglês, espanhol e francês.', 'Disponível 24/7.', 'Preço confirmado por escrito antes de reservar.']),
   dict(type='cta', h='Precisa de motorista?', p='Indique a data, as horas e o ponto de partida. Respondemos com a confirmação e o preço.', ctas=[('book', 'Reservar motorista'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Chófer a Disposición en Lisboa y Portugal · Dark Diamond Luxury',
  desc='Chófer y coche privados a su disposición en Lisboa y en todo el país, por horas o por días. Reuniones, compras, tours y veladas.',
  crumb='Chófer a disposición', h1='Chófer a su disposición, por horas o por días.', img='van',
  lead='Un chófer y un coche solo para usted: reuniones, compras o un día sin mirar el reloj.',
  ctas=[('book', 'Reservar chófer'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='¿Cómo funciona?', steps=[
     ('Elija el día y las horas', 'Fecha, hora de inicio, duración prevista y punto de partida.'),
     ('Confirmación por escrito', 'Disponibilidad y precio se confirman por escrito antes del servicio.'),
     ('El chófer se queda con usted', 'El mismo chófer y el mismo coche durante todo el servicio, esperando donde acuerden.'),
     ('Itinerario flexible', 'Paradas y cambios a lo largo del día, sin complicaciones.')]),
   dict(type='split', bg='bone', h='Para qué sirve', ticks=[
     'Reuniones de negocios y desplazamientos entre oficinas', 'Compras y días en la ciudad', 'Varias visitas en un solo día',
     'Cenas y eventos, con regreso a la hora', 'Ejecutivos, delegaciones e invitados']),
   dict(type='split', h='Conviene saber', ticks=[
     'Vehículo privado solo para usted y su grupo.', 'Mercedes-Benz Clase S, Clase E y Clase V, Sprinter y minibús de 19 plazas.',
     'Chóferes que hablan portugués, inglés, español y francés.', 'Disponible 24/7.', 'Precio confirmado por escrito antes de reservar.']),
   dict(type='cta', h='¿Necesita chófer?', p='Indique la fecha, las horas y el punto de partida. Respondemos con la confirmación y el precio.', ctas=[('book', 'Reservar chófer'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# TOURS PRIVADOS
# =====================================================================================
PAGES_NEW['tours'] = {
 'en': dict(
  title='Private Tours in Portugal with a Chauffeur · Dark Diamond Luxury',
  desc='Private day trips from Lisbon to Sintra, Cascais, Fátima, Évora, the Douro and more, with a chauffeur just for you and stops wherever you like.',
  crumb='Private tours', h1='Private tours in Portugal, at your pace.', img='d-sintra',
  lead='Sintra, Cascais, Fátima, Évora or the Douro, with a driver just for you and stops wherever you like.',
  ctas=[('book', 'Book a tour'), ('tel', 'Call')],
  blocks=[
   dict(type='split', h='How it works', steps=[
     ('Choose the destination', 'Pick a place from the list or ask for a suggestion.'),
     ('Written confirmation', 'Times and price are confirmed in writing.'),
     ('Pick-up at your hotel', 'The driver collects you at the agreed time and place.'),
     ('Stops to suit you', 'Time at each stop is yours to decide, with the day planned around it.')]),
   dict(type='split', bg='bone', h='Most requested tours', ticks=[
     'Sintra and Cabo da Roca', 'Cascais and the Estoril coast', 'Fátima, Nazaré and Óbidos', 'Évora and the Alentejo',
     'The Douro valley', 'Comporta and the Alentejo coast', 'The Algarve']),
   dict(type='split', h='Good to know', ticks=[
     'A private vehicle just for your group: no shared tours.', 'From one passenger to groups of 19.',
     'Child seats on request: tell us the children\'s ages when booking.', 'Drivers who speak Portuguese, English, Spanish and French.',
     'Price confirmed in writing before you book.'], related=DESTS),
   dict(type='cta', h='Planning a day out?', p='Tell us where you would like to go and when. We reply with a plan and a price.', ctas=[('book', 'Book a tour'), ('tel', 'Call')]),
  ]),
 'pt': dict(
  title='Tours Privados em Portugal com Motorista · Dark Diamond Luxury',
  desc='Passeios privados de um dia a partir de Lisboa: Sintra, Cascais, Fátima, Évora, o Douro e mais, com um motorista só para si e paragens onde quiser.',
  crumb='Tours privados', h1='Tours privados em Portugal, ao seu ritmo.', img='d-sintra',
  lead='Sintra, Cascais, Fátima, Évora ou o Douro, com um motorista só para si e paragens onde quiser.',
  ctas=[('book', 'Reservar tour'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Como funciona?', steps=[
     ('Escolha o destino', 'Escolha um local da lista ou peça uma sugestão.'),
     ('Confirmação por escrito', 'Horários e preço são confirmados por escrito.'),
     ('Recolha no hotel', 'O motorista recolhe-o à hora e no local combinados.'),
     ('Paragens à sua medida', 'O tempo em cada paragem é consigo, e o dia é planeado em função disso.')]),
   dict(type='split', bg='bone', h='Tours mais pedidos', ticks=[
     'Sintra e Cabo da Roca', 'Cascais e a linha do Estoril', 'Fátima, Nazaré e Óbidos', 'Évora e o Alentejo',
     'O vale do Douro', 'Comporta e o litoral alentejano', 'O Algarve']),
   dict(type='split', h='Bom saber', ticks=[
     'Veículo privado só para o seu grupo: sem tours partilhados.', 'De um passageiro a grupos de 19.',
     'Cadeiras de criança por pedido: indique a idade das crianças ao reservar.', 'Motoristas que falam português, inglês, espanhol e francês.',
     'Preço confirmado por escrito antes de reservar.'], related=DESTS),
   dict(type='cta', h='Está a planear um passeio?', p='Indique onde gostaria de ir e quando. Respondemos com um plano e um preço.', ctas=[('book', 'Reservar tour'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Tours Privados en Portugal con Chófer · Dark Diamond Luxury',
  desc='Excursiones privadas de un día desde Lisboa: Sintra, Cascais, Fátima, Évora, el Duero y más, con un chófer solo para usted y paradas donde quiera.',
  crumb='Tours privados', h1='Tours privados en Portugal, a su ritmo.', img='d-sintra',
  lead='Sintra, Cascais, Fátima, Évora o el Duero, con un chófer solo para usted y paradas donde quiera.',
  ctas=[('book', 'Reservar tour'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='¿Cómo funciona?', steps=[
     ('Elija el destino', 'Elija un lugar de la lista o pida una sugerencia.'),
     ('Confirmación por escrito', 'Horarios y precio se confirman por escrito.'),
     ('Recogida en el hotel', 'El chófer le recoge a la hora y en el lugar acordados.'),
     ('Paradas a su medida', 'El tiempo en cada parada es suyo, y el día se planifica en función de ello.')]),
   dict(type='split', bg='bone', h='Tours más solicitados', ticks=[
     'Sintra y Cabo da Roca', 'Cascais y la costa de Estoril', 'Fátima, Nazaré y Óbidos', 'Évora y el Alentejo',
     'El valle del Duero', 'Comporta y la costa del Alentejo', 'El Algarve']),
   dict(type='split', h='Conviene saber', ticks=[
     'Vehículo privado solo para su grupo: sin tours compartidos.', 'De un pasajero a grupos de 19.',
     'Sillas infantiles bajo petición: indique la edad de los niños al reservar.', 'Chóferes que hablan portugués, inglés, español y francés.',
     'Precio confirmado por escrito antes de reservar.'], related=DESTS),
   dict(type='cta', h='¿Planea una excursión?', p='Indique adónde le gustaría ir y cuándo. Respondemos con un plan y un precio.', ctas=[('book', 'Reservar tour'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# EVENTOS E CASAMENTOS
# =====================================================================================
PAGES_NEW['events'] = {
 'en': dict(
  title='Event and Wedding Transport in Portugal · Dark Diamond Luxury',
  desc='Chauffeured transport for large events, corporate events such as Web Summit, professional sport, golf and weddings in Portugal. Guests met and taken on time.',
  subject='Event transport request',
  crumb='Events and weddings', h1='Events and weddings, with transport on time.', img='events',
  lead='Guests met and taken on time, with the coordination handled by us.',
  ctas=[('mail', 'Request a proposal'), ('tel', 'Call')],
  blocks=[
   dict(type='split', h='Events we work with', ticks=[
     '<b>Large events.</b> International conferences and fairs, such as Web Summit.',
     '<b>Corporate events.</b> Meetings, conventions, launches and incentive trips.',
     '<b>Professional sport.</b> Teams, organisations and guests at professional sporting events.',
     '<b>Golf.</b> Tournaments and golf trips, with room for luggage.',
     '<b>Weddings.</b> Couples and guests, from the ceremony to the venue and back.']),
   dict(type='split', bg='bone', h='How we work', ticks=[
     'A single point of contact for the whole operation.', 'Times agreed with the organisers.',
     'Vehicles for groups: V-Class, Sprinter and a 19-seat minibus.', 'As many vehicles as the number of guests requires.',
     'Drivers who speak Portuguese, English, Spanish and French.']),
   dict(type='split', h='How it works', steps=[
     ('Send the event details', 'Dates, venues and expected number of guests.'),
     ('Proposal and price', 'Sent in writing, with the vehicles and the times.'),
     ('Planning with the organisers', 'Pick-ups, routes and times agreed in advance.'),
     ('On the day', 'Direct coordination with the drivers, so any change is handled straight away.')]),
   dict(type='cta', h='Preparing an event?', p='Send the dates, the venues and the number of guests. We reply with a proposal.', ctas=[('mail', 'Request a proposal'), ('tel', 'Call')]),
  ]),
 'pt': dict(
  title='Transporte para Eventos e Casamentos em Portugal · Dark Diamond Luxury',
  desc='Transporte com motorista para grandes eventos, eventos corporativos como a Web Summit, desporto profissional, golfe e casamentos em Portugal.',
  subject='Pedido de transporte para evento',
  crumb='Eventos e casamentos', h1='Eventos e casamentos, com transporte a horas.', img='events',
  lead='Convidados recebidos e levados a horas, com a coordenação feita por nós.',
  ctas=[('mail', 'Pedir proposta'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Eventos com que trabalhamos', ticks=[
     '<b>Grandes eventos.</b> Conferências e feiras internacionais, como a Web Summit.',
     '<b>Eventos corporativos.</b> Reuniões, convenções, lançamentos e viagens de incentivo.',
     '<b>Desporto profissional.</b> Equipas, organizações e convidados em eventos desportivos profissionais.',
     '<b>Golfe.</b> Torneios e viagens de golfe, com espaço para bagagem.',
     '<b>Casamentos.</b> Noivos e convidados, da cerimónia ao local da festa e de volta.']),
   dict(type='split', bg='bone', h='Como trabalhamos', ticks=[
     'Um único contacto para toda a operação.', 'Horários combinados com a organização.',
     'Veículos para grupos: Classe V, Sprinter e minibus de 19 lugares.', 'Tantos veículos quantos o número de convidados exigir.',
     'Motoristas que falam português, inglês, espanhol e francês.']),
   dict(type='split', h='Como funciona?', steps=[
     ('Envie os dados do evento', 'Datas, locais e número previsto de convidados.'),
     ('Proposta e preço', 'Enviados por escrito, com os veículos e os horários.'),
     ('Planeamento com a organização', 'Recolhas, percursos e horários combinados com antecedência.'),
     ('No dia', 'Coordenação direta com os motoristas, para que qualquer alteração seja tratada de imediato.')]),
   dict(type='cta', h='Está a preparar um evento?', p='Envie as datas, os locais e o número de convidados. Respondemos com uma proposta.', ctas=[('mail', 'Pedir proposta'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Transporte para Eventos y Bodas en Portugal · Dark Diamond Luxury',
  desc='Transporte con chófer para grandes eventos, eventos corporativos como la Web Summit, deporte profesional, golf y bodas en Portugal.',
  subject='Solicitud de transporte para evento',
  crumb='Eventos y bodas', h1='Eventos y bodas, con transporte puntual.', img='events',
  lead='Invitados recibidos y llevados a la hora, con la coordinación a nuestro cargo.',
  ctas=[('mail', 'Solicitar propuesta'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='Eventos con los que trabajamos', ticks=[
     '<b>Grandes eventos.</b> Conferencias y ferias internacionales, como la Web Summit.',
     '<b>Eventos corporativos.</b> Reuniones, convenciones, lanzamientos y viajes de incentivo.',
     '<b>Deporte profesional.</b> Equipos, organizaciones e invitados en eventos deportivos profesionales.',
     '<b>Golf.</b> Torneos y viajes de golf, con espacio para el equipaje.',
     '<b>Bodas.</b> Novios e invitados, de la ceremonia al lugar de la fiesta y de vuelta.']),
   dict(type='split', bg='bone', h='Cómo trabajamos', ticks=[
     'Un único contacto para toda la operación.', 'Horarios acordados con la organización.',
     'Vehículos para grupos: Clase V, Sprinter y minibús de 19 plazas.', 'Tantos vehículos como exija el número de invitados.',
     'Chóferes que hablan portugués, inglés, español y francés.']),
   dict(type='split', h='¿Cómo funciona?', steps=[
     ('Envíe los datos del evento', 'Fechas, lugares y número previsto de invitados.'),
     ('Propuesta y precio', 'Enviados por escrito, con los vehículos y los horarios.'),
     ('Planificación con la organización', 'Recogidas, rutas y horarios acordados con antelación.'),
     ('El día del evento', 'Coordinación directa con los chóferes, para resolver cualquier cambio de inmediato.')]),
   dict(type='cta', h='¿Prepara un evento?', p='Envíe las fechas, los lugares y el número de invitados. Respondemos con una propuesta.', ctas=[('mail', 'Solicitar propuesta'), ('tel', 'Llamar')]),
  ]),
}

# =====================================================================================
# LONGA DISTÂNCIA
# =====================================================================================
PAGES_NEW['longdistance'] = {
 'en': dict(
  title='Long-Distance Private Transfers · Dark Diamond Luxury',
  desc='Private door-to-door transfers from Lisbon to Porto, the Algarve, Madrid, Seville, Marbella and France, in a private vehicle with a professional driver.',
  crumb='Long distance', h1='Long-distance transfers, door to door.', img='longdist',
  lead='Porto, the Algarve, Spain and France, door to door, in a private vehicle.',
  ctas=[('book', 'Book a transfer'), ('tel', 'Call')],
  blocks=[
   dict(type='split', h='Usual routes', ticks=[
     'Lisbon to Porto and the Douro valley', 'Lisbon to the Algarve', 'Lisbon to Madrid', 'Lisbon to Seville', 'Lisbon to Marbella',
     'France, on request'], related=['d-porto', 'd-algarve']),
   dict(type='split', bg='bone', h='How it works', steps=[
     ('Send the route', 'Origin, destination, date, time, number of passengers and luggage.'),
     ('Written confirmation', 'Price and times are confirmed in writing before you book.'),
     ('Door-to-door ride', 'A private vehicle from the pick-up address to the final destination.'),
     ('Stops as agreed', 'Breaks along the way, agreed in advance with the driver.')]),
   dict(type='split', h='Good to know', ticks=[
     'A private vehicle just for you and your group.', 'Mercedes-Benz S-Class, E-Class and V-Class, Sprinter and a 19-seat minibus.',
     'Drivers who speak Portuguese, English, Spanish and French.', 'Available 24/7.', 'Price confirmed in writing before you book.']),
   dict(type='cta', h='Planning a long trip?', p='Tell us the route, the date and the number of passengers. We reply with confirmation and price.', ctas=[('book', 'Book a transfer'), ('tel', 'Call')]),
  ]),
 'pt': dict(
  title='Transfers de Longa Distância · Dark Diamond Luxury',
  desc='Transfers privados de porta a porta de Lisboa para o Porto, Algarve, Madrid, Sevilha, Marbella e França, em viatura privada e com motorista profissional.',
  crumb='Longa distância', h1='Transfers de longa distância, de porta a porta.', img='longdist',
  lead='Porto, Algarve, Espanha e França, de porta a porta, em viatura privada.',
  ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')],
  blocks=[
   dict(type='split', h='Rotas habituais', ticks=[
     'Lisboa – Porto e vale do Douro', 'Lisboa – Algarve', 'Lisboa – Madrid', 'Lisboa – Sevilha', 'Lisboa – Marbella',
     'França, por pedido'], related=['d-porto', 'd-algarve']),
   dict(type='split', bg='bone', h='Como funciona?', steps=[
     ('Envie o trajeto', 'Origem, destino, data, hora, número de passageiros e malas.'),
     ('Confirmação por escrito', 'Preço e horários são confirmados por escrito antes de reservar.'),
     ('Viagem de porta a porta', 'Viatura privada, da morada de recolha até ao destino final.'),
     ('Paragens combinadas', 'Pausas ao longo do caminho, combinadas antes com o motorista.')]),
   dict(type='split', h='Bom saber', ticks=[
     'Veículo privado só para si e para o seu grupo.', 'Mercedes-Benz Classe S, Classe E e Classe V, Sprinter e minibus de 19 lugares.',
     'Motoristas que falam português, inglês, espanhol e francês.', 'Disponível 24/7.', 'Preço confirmado por escrito antes de reservar.']),
   dict(type='cta', h='Vai fazer uma viagem longa?', p='Indique o trajeto, a data e o número de passageiros. Respondemos com a confirmação e o preço.', ctas=[('book', 'Reservar transfer'), ('tel', 'Ligar')]),
  ]),
 'es': dict(
  title='Traslados de Larga Distancia · Dark Diamond Luxury',
  desc='Traslados privados puerta a puerta de Lisboa a Oporto, el Algarve, Madrid, Sevilla, Marbella y Francia, en vehículo privado y con chófer profesional.',
  crumb='Larga distancia', h1='Traslados de larga distancia, de puerta a puerta.', img='longdist',
  lead='Oporto, el Algarve, España y Francia, de puerta a puerta, en vehículo privado.',
  ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')],
  blocks=[
   dict(type='split', h='Rutas habituales', ticks=[
     'Lisboa – Oporto y valle del Duero', 'Lisboa – Algarve', 'Lisboa – Madrid', 'Lisboa – Sevilla', 'Lisboa – Marbella',
     'Francia, bajo petición'], related=['d-porto', 'd-algarve']),
   dict(type='split', bg='bone', h='¿Cómo funciona?', steps=[
     ('Envíe el trayecto', 'Origen, destino, fecha, hora, número de pasajeros y maletas.'),
     ('Confirmación por escrito', 'Precio y horarios se confirman por escrito antes de reservar.'),
     ('Viaje de puerta a puerta', 'Vehículo privado, desde la dirección de recogida hasta el destino final.'),
     ('Paradas acordadas', 'Pausas por el camino, acordadas antes con el chófer.')]),
   dict(type='split', h='Conviene saber', ticks=[
     'Vehículo privado solo para usted y su grupo.', 'Mercedes-Benz Clase S, Clase E y Clase V, Sprinter y minibús de 19 plazas.',
     'Chóferes que hablan portugués, inglés, español y francés.', 'Disponible 24/7.', 'Precio confirmado por escrito antes de reservar.']),
   dict(type='cta', h='¿Va a hacer un viaje largo?', p='Indique el trayecto, la fecha y el número de pasajeros. Respondemos con la confirmación y el precio.', ctas=[('book', 'Reservar traslado'), ('tel', 'Llamar')]),
  ]),
}
