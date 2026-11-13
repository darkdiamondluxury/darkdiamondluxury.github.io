# Perguntas frequentes por página. Só factos que o site já afirma.
# Quando o Bruno responder à lista Decisões (espera grátis, cancelamento, preço das cadeiras…), acrescentar aqui.

FAQ_H = {'pt': 'Perguntas frequentes', 'en': 'Frequently asked questions', 'es': 'Preguntas frecuentes'}

_PRICE = {
    'pt': ('Quanto custa?', 'Depende do trajeto, da viatura e da hora. Envie o pedido pelo site e respondemos no WhatsApp com o preço, confirmado por escrito antes de reservar.'),
    'en': ('How much does it cost?', 'It depends on the route, the vehicle and the time. Send your request through the site and we reply on WhatsApp with the price, confirmed in writing before you book.'),
    'es': ('¿Cuánto cuesta?', 'Depende del trayecto, del vehículo y de la hora. Envíe su solicitud desde la web y le respondemos por WhatsApp con el precio, confirmado por escrito antes de reservar.'),
}
_LANGS = {
    'pt': ('Os motoristas falam inglês?', 'Sim. Os nossos motoristas falam português, inglês, espanhol e francês.'),
    'en': ('Do the drivers speak English?', 'Yes. Our drivers speak Portuguese, English, Spanish and French.'),
    'es': ('¿Los chóferes hablan español?', 'Sí. Nuestros chóferes hablan portugués, inglés, español y francés.'),
}

FAQ = {
    'airport': {
        'pt': [
            ('Como encontro o motorista no aeroporto?', 'O motorista espera por si nas chegadas, com o seu nome. Antes da viagem recebe o contacto dele.'),
            ('E se o voo atrasar?', 'Acompanhamos o voo, por isso o motorista ajusta a hora de recolha à hora real de aterragem. Não precisa de nos avisar.'),
            _PRICE['pt'],
            ('Têm cadeiras de criança?', 'Sim, por pedido. Indique a idade das crianças ao reservar.'),
            ('A que horas funcionam?', 'A qualquer hora, 24 horas por dia, todos os dias, para chegadas e partidas.'),
            _LANGS['pt'],
        ],
        'en': [
            ('How do I find my driver at the airport?', 'Your driver waits for you at arrivals with your name. You receive their contact before the journey.'),
            ('What if my flight is delayed?', 'We track your flight, so the driver adjusts the pick-up to the actual landing time. You do not need to let us know.'),
            _PRICE['en'],
            ('Do you have child seats?', 'Yes, on request. Tell us the children\'s ages when you book.'),
            ('What are your hours?', 'Any time, 24 hours a day, every day, for arrivals and departures.'),
            _LANGS['en'],
        ],
        'es': [
            ('¿Cómo encuentro al chófer en el aeropuerto?', 'El chófer le espera en llegadas con su nombre. Antes del viaje recibe su contacto.'),
            ('¿Y si mi vuelo se retrasa?', 'Seguimos su vuelo, así que el chófer ajusta la recogida a la hora real de aterrizaje. No hace falta que nos avise.'),
            _PRICE['es'],
            ('¿Tienen sillas para niños?', 'Sí, bajo petición. Indique la edad de los niños al reservar.'),
            ('¿En qué horario trabajan?', 'A cualquier hora, las 24 horas, todos los días, para llegadas y salidas.'),
            _LANGS['es'],
        ],
    },
    'longdistance': {
        'pt': [
            ('Fazem viagens para Espanha e França?', 'Sim. Fazemos Lisboa–Madrid, Lisboa–Sevilha e Lisboa–Marbella, e França por pedido.'),
            ('Podemos parar pelo caminho?', 'Sim. Diga-nos onde quer parar ao reservar, para uma refeição, uma visita ou apenas para descansar.'),
            ('Que viatura é melhor para um grupo?', 'Até 3 passageiros, Classe E ou Classe S. Até 7, Classe V. Para grupos maiores, Sprinter ou minibus de 19 lugares. O formulário sugere a viatura conforme o número de pessoas e malas.'),
            _PRICE['pt'],
            _LANGS['pt'],
        ],
        'en': [
            ('Do you drive to Spain and France?', 'Yes. We drive Lisbon–Madrid, Lisbon–Seville and Lisbon–Marbella, and France on request.'),
            ('Can we stop on the way?', 'Yes. Tell us where you would like to stop when you book, for a meal, a visit or simply a break.'),
            ('Which vehicle suits a group?', 'Up to 3 passengers, E-Class or S-Class. Up to 7, V-Class. For larger groups, a Sprinter or a 19-seat minibus. The booking form suggests a vehicle for your number of people and bags.'),
            _PRICE['en'],
            _LANGS['en'],
        ],
        'es': [
            ('¿Viajan a España y Francia?', 'Sí. Hacemos Lisboa–Madrid, Lisboa–Sevilla y Lisboa–Marbella, y Francia bajo petición.'),
            ('¿Podemos parar por el camino?', 'Sí. Díganos dónde quiere parar al reservar, para comer, para una visita o simplemente para descansar.'),
            ('¿Qué vehículo conviene a un grupo?', 'Hasta 3 pasajeros, Clase E o Clase S. Hasta 7, Clase V. Para grupos mayores, Sprinter o minibús de 19 plazas. El formulario sugiere el vehículo según el número de personas y maletas.'),
            _PRICE['es'],
            _LANGS['es'],
        ],
    },
}
