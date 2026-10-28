# Dados da empresa e do site. Mudar aqui muda em todas as páginas e línguas.
# Depois de mudar: python3 _build/build.py  (gera os ficheiros .html)

SITE = 'https://darkdiamondluxury.github.io'   # quando houver domínio: 'https://darkdiamondluxury.pt'
BRAND = 'Dark Diamond Luxury'

LEGAL = {
    'name': 'Artur Danilo, Unipessoal Lda',     # mudança de nome em curso: atualizar quando estiver registada
    'type': {'pt': 'Sociedade unipessoal por quotas', 'en': 'Single-member private limited company', 'es': 'Sociedad unipersonal de responsabilidad limitada'},
    'nipc': '515565458',
    'street': 'Av. Vergílio Ferreira, Lote 764, 6.º Esq.',
    'postcode': '1950-339',
    'city': 'Lisboa',
    'registry': {'pt': 'Conservatória do Registo Comercial de Lisboa', 'en': 'Lisbon Commercial Registry Office', 'es': 'Registro Mercantil de Lisboa'},
    'capital': '20.000 €',
    'rnaat': '682/2022',
}

PHONES = ['+351 932 666 254', '+351 960 033 622']
EMAIL = 'darkdiamondluxury@gmail.com'
WHATSAPP = '351932666254'   # número para onde o formulário de reserva envia (só números, com indicativo)
# Pedidos de reserva do formulário entram na app (tabela booking_requests, função submit_booking).
# A chave "anon" é pública por natureza: só deixa chamar a função que guarda pedidos, nada mais.
# Ambiente: PRÉ-PROD. Quando a app passar a produção, trocar pelos valores do projeto "despacho".
BOOKINGS_URL = 'https://ccwzqtdxugutkgdupgxc.supabase.co/rest/v1/rpc/submit_booking'
BOOKINGS_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNjd3pxdGR4dWd1dGtnZHVwZ3hjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIwNjE1NTgsImV4cCI6MjEwNzYzNzU1OH0.xLQwoKKGOUXW3g4SN3B6wnRUcjO0EhXZ7dREUpzASBQ'
WHATSAPP_ALL = ['351932666254', '351960033622']   # ambos têm WhatsApp
INSTAGRAM = ''         # ex.: 'https://instagram.com/darkdiamondluxury'

FLEET = {'pt': 'Mercedes-Benz Classe S, Classe E, Classe V, Sprinter e minibus de 19 lugares',
         'en': 'Mercedes-Benz S-Class, E-Class, V-Class, Sprinter and a 19-seat minibus',
         'es': 'Mercedes-Benz Clase S, Clase E, Clase V, Sprinter y minibús de 19 plazas'}
LANGS_SPOKEN = {'pt': 'Português, inglês, espanhol e francês', 'en': 'Portuguese, English, Spanish and French', 'es': 'Portugués, inglés, español y francés'}

COVERAGE = {'pt': 'Portugal, Espanha e França', 'en': 'Portugal, Spain and France', 'es': 'Portugal, España y Francia'}

LANGS = ['en', 'pt', 'es']      # a primeira é a da raiz do site (/)
LANG_NAME = {'en': 'EN', 'pt': 'PT', 'es': 'ES'}
LOCALE = {'en': 'en_GB', 'pt': 'pt_PT', 'es': 'es_ES'}

# Endereço de cada página em cada língua.
SLUGS = {
    'home':     {'en': '/', 'pt': '/pt/', 'es': '/es/'},
    'agencies': {'en': '/agencies/', 'pt': '/pt/agencias/', 'es': '/es/agencias/'},
    'airport':  {'en': '/lisbon-airport-transfer/', 'pt': '/pt/transfer-aeroporto-lisboa/', 'es': '/es/traslado-aeropuerto-lisboa/'},
    'cruise':   {'en': '/lisbon-cruise-port-transfer/', 'pt': '/pt/transfer-terminal-cruzeiros-lisboa/', 'es': '/es/traslado-terminal-cruceros-lisboa/'},
    'd-sintra':   {'en': '/lisbon-to-sintra/', 'pt': '/pt/lisboa-sintra/', 'es': '/es/lisboa-sintra/'},
    'd-cascais':  {'en': '/lisbon-to-cascais/', 'pt': '/pt/lisboa-cascais/', 'es': '/es/lisboa-cascais/'},
    'd-comporta': {'en': '/lisbon-to-comporta/', 'pt': '/pt/lisboa-comporta/', 'es': '/es/lisboa-comporta/'},
    'd-evora':    {'en': '/lisbon-to-evora/', 'pt': '/pt/lisboa-evora/', 'es': '/es/lisboa-evora/'},
    'd-fatima':   {'en': '/lisbon-to-fatima/', 'pt': '/pt/lisboa-fatima/', 'es': '/es/lisboa-fatima/'},
    'd-algarve':  {'en': '/lisbon-to-algarve/', 'pt': '/pt/lisboa-algarve/', 'es': '/es/lisboa-algarve/'},
    'd-porto':    {'en': '/lisbon-to-porto/', 'pt': '/pt/lisboa-porto/', 'es': '/es/lisboa-oporto/'},
    'privacy':  {'en': '/privacy/', 'pt': '/pt/privacidade/', 'es': '/es/privacidad/'},
    'legal':    {'en': '/legal/', 'pt': '/pt/informacao-legal/', 'es': '/es/aviso-legal/'},
    'support':  {'en': '/support/', 'pt': '/pt/suporte/', 'es': '/es/soporte/'},
}
DESTS = ['d-sintra', 'd-cascais', 'd-comporta', 'd-evora', 'd-fatima', 'd-algarve', 'd-porto']

# Endereços antigos que passam a reencaminhar.
REDIRECTS = {'/privacidade.html': SLUGS['privacy']['pt'], '/suporte.html': SLUGS['support']['pt']}

# Fotografias (Unsplash License), reutilizadas nas páginas.
IMG = {
    'van': 'https://images.unsplash.com/photo-1765461734605-34657fa04db2?auto=format&fit=crop&w=2000&q=70',
    'plane': 'https://images.unsplash.com/photo-1773673496557-e55445604766?auto=format&fit=crop&w=2000&q=70',
    'leather': 'https://images.unsplash.com/photo-1580929945040-a16adedf9f6a?auto=format&fit=crop&w=2000&q=70',
    'bridge': 'https://images.unsplash.com/photo-1558102400-72da9fdbecae?auto=format&fit=crop&w=2000&q=70',
    'd-sintra': 'https://images.unsplash.com/photo-1697394494123-c6c1323a14f7?auto=format&fit=crop&w=2000&q=70',
    'd-cascais': 'https://images.unsplash.com/photo-1587973878097-ef3aabd5eeaa?auto=format&fit=crop&w=2000&q=70',
    'd-comporta': 'https://images.unsplash.com/photo-1672825952732-ecef34882416?auto=format&fit=crop&w=2000&q=70',
    'd-evora': 'https://images.unsplash.com/photo-1644183521042-377da9d4aea3?auto=format&fit=crop&w=2000&q=70',
    'd-fatima': 'https://images.pexels.com/photos/30443719/pexels-photo-30443719.jpeg?auto=compress&cs=tinysrgb&w=2000',
    'd-algarve': 'https://images.pexels.com/photos/33887497/pexels-photo-33887497.jpeg?auto=compress&cs=tinysrgb&w=2000',
    'd-porto': 'https://images.unsplash.com/photo-1768565540385-5195e32bb44b?auto=format&fit=crop&w=2000&q=70',
}
