# Tabela de preços do site (versão final de 25/11/2026, documento do Projeto "claude/tabela-precos-site.md").
# Valores em euros, IVA incluído, preço final para o cliente. Transfers só ida, a partir do aeroporto ou de Lisboa.
# Para mudar um preço: alterar aqui e voltar a gerar o site. Nada mais no código tem valores.

# Viaturas públicas, por ordem de preço. Código usado no formulário de reserva.
VEH = [('E', 'Classe E'), ('V', 'Classe V'), ('T', 'Vito'), ('S', 'Classe S'), ('P', 'Sprinter'), ('M', 'Minibus')]
VEH_NAME = {
    'pt': ['Classe E', 'Classe V', 'Vito', 'Classe S', 'Sprinter', 'Minibus'],
    'en': ['E-Class', 'V-Class', 'Vito', 'S-Class', 'Sprinter', 'Minibus'],
    'es': ['Clase E', 'Clase V', 'Vito', 'Clase S', 'Sprinter', 'Minibús'],
    'fr': ['Classe E', 'Classe V', 'Vito', 'Classe S', 'Sprinter', 'Minibus'],
}

def _n(pt, en=None, es=None, fr=None):
    return {'pt': pt, 'en': en or pt, 'es': es or pt, 'fr': fr or pt}

# Grupos de destinos: (nome, [(nome do destino, km, [E, V, Vito, S, Sprinter, Minibus]), ...])
TRANSFERS = [
    (_n('Lisboa', 'Lisbon', 'Lisboa', 'Lisbonne'), [
        (_n('Lisboa (aeroporto ↔ cidade)', 'Lisbon (airport ↔ city)', 'Lisboa (aeropuerto ↔ ciudad)', 'Lisbonne (aéroport ↔ ville)'), 15, [49, 69, 79, 89, 129, 159]),
    ]),
    (_n('Linha de Cascais e Sintra', 'Cascais coast and Sintra', 'Costa de Cascais y Sintra', 'Côte de Cascais et Sintra'), [
        (_n('Oeiras'), 23, [55, 75, 86, 97, 137, 168]),
        (_n('Taguspark'), 23, [55, 75, 86, 97, 137, 168]),
        (_n('Carcavelos'), 27, [55, 75, 86, 97, 137, 168]),
        (_n('Estoril'), 31, [59, 80, 90, 102, 143, 174]),
        (_n('Sintra'), 29, [59, 80, 90, 102, 143, 174]),
        (_n('Cascais'), 36, [65, 86, 97, 110, 151, 183]),
        (_n('Guincho'), 39, [69, 91, 102, 115, 157, 189]),
    ]),
    (_n('Margem Sul', 'South of the Tagus', 'Sur del Tajo', 'Rive sud du Tage'), [
        (_n('Costa da Caparica'), 22, [57, 77, 88, 99, 142, 173]),
        (_n('Aroeira'), 27, [61, 82, 92, 104, 148, 179]),
        (_n('Alcochete'), 29, [62, 83, 93, 105, 151, 182]),
        (_n('Sesimbra'), 44, [95, 118, 132, 149, 193, 228]),
        (_n('Palmela'), 46, [97, 121, 134, 151, 196, 231]),
        (_n('Setúbal'), 49, [99, 123, 137, 154, 199, 234]),
        (_n('Tróia por barco ¹', 'Tróia by ferry ¹', 'Tróia en ferry ¹', 'Tróia en ferry ¹'), 49, [178, 219, 245, 250, 380, 450]),
        (_n('Tróia por Alcácer', 'Tróia via Alcácer', 'Tróia por Alcácer', 'Tróia via Alcácer'), 137, [295, 333, 362, 408, 476, 530]),
        (_n('Comporta'), 118, [255, 290, 316, 357, 417, 468]),
    ]),
    (_n('Oeste', 'West coast', 'Oeste', 'Ouest'), [
        (_n('Mafra'), 35, [89, 112, 125, 141, 185, 219]),
        (_n('Ericeira'), 46, [95, 118, 132, 149, 193, 228]),
        (_n('Torres Vedras'), 46, [95, 118, 132, 149, 193, 228]),
        (_n('Santa Cruz'), 61, [109, 134, 148, 167, 213, 249]),
        (_n('Óbidos'), 80, [179, 209, 228, 258, 311, 354]),
        (_n("Praia d'El Rey"), 93, [205, 237, 258, 292, 347, 393]),
        (_n('Peniche'), 97, [213, 245, 268, 302, 359, 405]),
    ]),
    (_n('Centro', 'Centre', 'Centro', 'Centre'), [
        (_n('Nazaré'), 118, [255, 290, 316, 357, 417, 468]),
        (_n('Alcobaça'), 118, [255, 290, 316, 357, 417, 468]),
        (_n('Fátima'), 120, [259, 295, 320, 362, 423, 474]),
        (_n('Tomar'), 130, [279, 316, 344, 388, 451, 504]),
        (_n('Leiria'), 139, [297, 336, 364, 411, 476, 531]),
        (_n('Figueira da Foz'), 193, [405, 452, 488, 552, 627, 693]),
        (_n('Coimbra'), 199, [417, 465, 502, 567, 644, 711]),
        (_n('Buçaco', 'Buçaco', 'Buçaco', 'Buçaco'), 225, [469, 520, 562, 635, 717, 789]),
    ]),
    (_n('Alentejo'), [
        (_n('Évora'), 133, [285, 323, 350, 396, 459, 513]),
        (_n('Sines'), 158, [335, 376, 408, 461, 529, 588]),
        (_n('Beja'), 175, [369, 413, 447, 505, 577, 639]),
    ]),
    (_n('Algarve'), [
        (_n('Albufeira'), 254, [527, 583, 629, 710, 798, 876]),
        (_n('Vilamoura'), 262, [543, 600, 647, 731, 821, 900]),
        (_n('Faro'), 275, [569, 628, 677, 765, 857, 939]),
        (_n('Lagos'), 294, [607, 669, 721, 814, 910, 996]),
    ]),
    (_n('Norte e interior', 'North and inland', 'Norte e interior', 'Nord et intérieur'), [
        (_n('Covilhã'), 272, [563, 622, 670, 757, 849, 930]),
        (_n('Viseu'), 284, [587, 647, 698, 788, 882, 966]),
        (_n('Porto'), 306, [626, 689, 743, 839, 937, 1025]),
        (_n('Régua / Douro', 'Régua / Douro Valley', 'Régua / Valle del Duero', 'Régua / Vallée du Douro'), 350, [679, 746, 804, 908, 1011, 1104]),
    ]),
    (_n('Espanha', 'Spain', 'España', 'Espagne'), [
        (_n('Badajoz'), 224, [467, 518, 560, 632, 714, 786]),
        (_n('Sevilha', 'Seville', 'Sevilla', 'Séville'), 461, [812, 889, 957, 1081, 1197, 1304]),
        (_n('Madrid'), 627, [1011, 1104, 1186, 1340, 1476, 1603]),
        (_n('Marbella'), 712, [1113, 1213, 1303, 1473, 1619, 1756]),
    ]),
]

# Tours tabeladas. None = sob orçamento (o botão leva ao pedido de orçamento).
TOURS = [
    (_n('Lisboa — 4 h', 'Lisbon — 4 h', 'Lisboa — 4 h', 'Lisbonne — 4 h'), [160, 180, 200, 280, 300, 320]),
    (_n('Lisboa — 8 h', 'Lisbon — 8 h', 'Lisboa — 8 h', 'Lisbonne — 8 h'), [280, 315, 350, 490, 525, 560]),
    (_n('Lisboa à noite — 3 h', 'Lisbon by night — 3 h', 'Lisboa de noche — 3 h', 'Lisbonne de nuit — 3 h'), [171, 186, 201, 261, 276, 291]),
    (_n('Sintra e Cascais — 4 h', 'Sintra and Cascais — 4 h', 'Sintra y Cascais — 4 h', 'Sintra et Cascais — 4 h'), [185, 221, 247, 320, 376, 423]),
    (_n('Queluz, Sintra, Cascais e Estoril — 8 h', 'Queluz, Sintra, Cascais and Estoril — 8 h', 'Queluz, Sintra, Cascais y Estoril — 8 h', 'Queluz, Sintra, Cascais et Estoril — 8 h'), [315, 367, 409, 548, 620, 683]),
    (_n('Estoril e Cascais à noite — 3h30', 'Estoril and Cascais by night — 3h30', 'Estoril y Cascais de noche — 3h30', 'Estoril et Cascais de nuit — 3h30'), [216, 249, 273, 336, 390, 434]),
    (_n('Sesimbra, Arrábida e Setúbal — 8 h', 'Sesimbra, Arrábida and Setúbal — 8 h', 'Sesimbra, Arrábida y Setúbal — 8 h', 'Sesimbra, Arrábida et Setúbal — 8 h'), [334, 387, 431, 565, 640, 704]),
    (_n('Fátima — 4 h de visita', 'Fátima — 4 h visit', 'Fátima — 4 h de visita', 'Fátima — 4 h de visite'), [419, 475, 520, 642, 723, 794]),
    (_n('Óbidos, Nazaré, Alcobaça e Fátima — 10 h', 'Óbidos, Nazaré, Alcobaça and Fátima — 10 h', 'Óbidos, Nazaré, Alcobaça y Fátima — 10 h', 'Óbidos, Nazaré, Alcobaça et Fátima — 10 h'), [489, 554, 606, 760, 849, 929]),
    (_n('Évora — 4 h de visita', 'Évora — 4 h visit', 'Évora — 4 h de visita', 'Évora — 4 h de visite'), [445, 503, 550, 676, 759, 833]),
    (_n('Évora, Arraiolos e Estremoz — 9 h', 'Évora, Arraiolos and Estremoz — 9 h', 'Évora, Arraiolos y Estremoz — 9 h', 'Évora, Arraiolos et Estremoz — 9 h'), [564, 633, 692, 851, 947, 1034]),
    (_n('Coimbra e Buçaco — 12 h', 'Coimbra and Buçaco — 12 h', 'Coimbra y Buçaco — 12 h', 'Coimbra et Buçaco — 12 h'), [719, 801, 874, 1073, None, None]),
    (_n('Porto — dia inteiro (4 h no Porto)', 'Porto — full day (4 h in Porto)', 'Oporto — día completo (4 h en Oporto)', 'Porto — journée complète (4 h à Porto)'), [786, 869, 943, 1119, None, None]),
    (_n('Algarve — 12 h'), [789, 876, 952, 1150, None, None]),
]

# Extras (secção 3 do documento, 25/11/2026)
NIGHT_EUR = 51                       # só tours e serviços à disposição, 20h00–07h30; transfers sem suplemento
NIGHT_FROM, NIGHT_TO = '20h00', '07h30'
EXTRA_15MIN = [10, 11, 13, 18, 19, 20]   # espera extra e paragem extra, por cada 15 min (E, V, Vito, S, Sprinter, Minibus)
ROUND_TRIP_PCT = 15                  # desconto no regresso, só reservas diretas no site
CAPACITY = [3, 6, 8, 3, 15, 21]      # passageiros (tabela da CM)

# Nomes do formulário de reserva (carrossel de destinos) que correspondem a uma linha da tabela.
# Destinos do carrossel que são uma região (Algarve, Arrábida, Comporta, Óbidos e Nazaré) ficam sem preço automático.
ALIASES = {
    'baixa · chiado': 'Lisboa (aeroporto ↔ cidade)', 'lisboa': 'Lisboa (aeroporto ↔ cidade)', 'lisbon': 'Lisboa (aeroporto ↔ cidade)',
    'lisbonne': 'Lisboa (aeroporto ↔ cidade)', 'vale do douro': 'Régua / Douro', 'douro valley': 'Régua / Douro',
    'valle del duero': 'Régua / Douro', 'vallée du douro': 'Régua / Douro', 'douro': 'Régua / Douro', 'régua': 'Régua / Douro',
    'oporto': 'Porto', 'troia': 'Tróia por barco ¹', 'tróia': 'Tróia por barco ¹', 'bussaco': 'Buçaco',
}
# Destinos do carrossel que são regiões: Óbidos e Nazaré têm linhas próprias; a Arrábida liga à tour; o Algarve fica sob orçamento.
TOUR_ALIASES = {'arrábida': 'Sesimbra, Arrábida e Setúbal — 8 h', 'arrabida': 'Sesimbra, Arrábida e Setúbal — 8 h'}
SPLIT = {'óbidos e nazaré': ['Óbidos', 'Nazaré'], 'óbidos and nazaré': ['Óbidos', 'Nazaré'], 'óbidos y nazaré': ['Óbidos', 'Nazaré'], 'óbidos et nazaré': ['Óbidos', 'Nazaré']}


def _check():
    for _, rows in TRANSFERS:
        for n, _km, p in rows:
            assert len(p) == 6 and all(p[i] < p[i + 1] for i in range(5)), n['pt']
    for n, p in TOURS:
        assert len(p) == 6, n['pt']


_check()


def lookup_json(lang):
    """Mapa nome-normalizado → preços, para o formulário de reserva (transfers e tours)."""
    tr, to = {}, {}
    for _, rows in TRANSFERS:
        for n, _km, p in rows:
            for x in n.values():
                tr[x.replace(' ¹', '').lower()] = p
    for a, target in ALIASES.items():
        for _, rows in TRANSFERS:
            for n, _km, p in rows:
                if n['pt'] == target:
                    tr[a] = p
    for n, p in TOURS:
        for x in n.values():
            to[x.lower()] = p
    tours_pt = {n['pt']: (n[lang], p) for n, p in TOURS}
    alias_tour = {a: tours_pt[t] for a, t in TOUR_ALIASES.items()}
    split = {k: [(x, tr[x.lower()]) for x in v] for k, v in SPLIT.items()}
    night = [x.lower() for n, _ in TOURS for x in n.values() if any(w in x for w in ('noite', 'night', 'noche', 'nuit'))]
    tours = [[n[lang], p] for n, p in TOURS]  # lista das tours tabeladas, para o passo 2 do formulário
    return {'tr': tr, 'tour': to, 'aliasTour': alias_tour, 'split': split, 'night': night, 'nightEur': NIGHT_EUR, 'tours': tours}
