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
WHATSAPP = ''          # só números com indicativo, ex.: '351932666254'. Vazio = botão mostra aviso.
INSTAGRAM = ''         # ex.: 'https://instagram.com/darkdiamondluxury'

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
    'plane': 'https://images.unsplash.com/photo-1503944251010-cbf290919d9d?auto=format&fit=crop&w=2000&q=70',
    'leather': 'https://images.unsplash.com/photo-1580929945040-a16adedf9f6a?auto=format&fit=crop&w=2000&q=70',
    'bridge': 'https://images.unsplash.com/photo-1558102400-72da9fdbecae?auto=format&fit=crop&w=2000&q=70',
}
