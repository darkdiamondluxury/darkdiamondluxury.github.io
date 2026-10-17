# Como o site é gerado

As páginas `.html` deste repositório são **geradas**. Não se editam à mão.

| Ficheiro | O que tem |
|---|---|
| `config.py` | Dados da empresa (nome legal, NIPC, contactos, WhatsApp, domínio) e o endereço de cada página |
| `home_i18n.py` | Textos da página inicial em PT, EN e ES |
| `home.html` | Modelo da página inicial (design, animações, formulário) |
| `content.py` | Textos das outras páginas (agências, aeroporto, cruzeiros, destinos, legal, privacidade) |
| `chrome.py` | Partes comuns: cabeçalho, troca de língua, rodapé, dados para o Google |
| `build.py` | Junta tudo e escreve os ficheiros |

Depois de mudar alguma coisa, gera o site com:

    python3 _build/build.py

Os dados em falta aparecem a dourado como `[…]` (classe `todo`).
