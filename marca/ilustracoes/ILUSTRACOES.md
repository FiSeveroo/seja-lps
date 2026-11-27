# Ilustrações da Seja Creator

As ilustrações deixam a marca mais humana: pessoas que pesquisam, conversando e criando, em volta das plataformas. Valem para o site e para qualquer criação da Seja (posts, carrosséis, materiais).

Primeiro uso no site: a Home (`ilustra-home-topo-v1.svg` no primeiro bloco e `ilustra-home-conversa-v1.svg` em "Agende uma conversa"). Depois, /ciencia/ (`ilustra-ciencia-topo-v1.svg` no primeiro bloco, `ilustra-ciencia-perguntas-v1.svg` em "Perguntas frequentes" e os ícones `ilustra-ciencia-dor-*-v1.svg` na lista de dores).

## Como o estilo funciona

- **Formas chapadas.** Sem contorno, sem degradê, sem sombra, sem textura, sem brilho. Cada peça é uma cor sólida.
- **Pessoas em busto, de frente e sem rosto.** Todas saem do mesmo molde (`pessoa()` em `kit.py`): cabeça oval, pescoço, ombros arredondados. Só mudam tom de pele, cabelo (cacheado, coque, curto, branco, comprido), roupa, acessórios (óculos, brinco, fone) e pose (fala, queixo, escreve) ou objeto (caneca, celular). Nunca desenhar uma pessoa fora do molde: é o molde que mantém todas da mesma família.
- **Diversidade sempre.** Em cena com mais de uma pessoa, variar tom de pele, cabelo, idade e gênero. Toda página com ilustração precisa ter homens e mulheres: para um homem, use `barba=True` (com cabelo "curto" ou "cacheado").
- **Cores só da marca.** Roxo, rosa, azul, laranja, amarelo, texto e branco, mais os tons claros do kit (lilás, lilás médio, rosa claro) e os tons de pele. Nada fora disso.
- **Cenas novas para cada conteúdo.** As cenas da Home são referência de estilo, não de composição: não repita mesa, ideia e plataformas em toda página. Invente a situação que o texto pede (ex.: /ciencia/ mostra um pesquisador gravando com o celular no tripé e o vídeo chegando às telas do público).
- **Objetos simples e reconhecíveis.** Notebook visto por trás, livros, caneca, caderno, celular, mesa. Ícones das plataformas em cartões brancos: vídeo, celular com reels, podcast (microfone com fone), post, página de site com envelope, lâmpada da ideia.
- **Peças do kit:** `pessoa` (com `barba`), ícones das plataformas, `icone_ideia`, `mesa`, `notebook_costas`, `livros`, `caneca`, `balao`, `interrogacao`, `brilhos`, `fio`, `relogio`, `documento` (com `selo`), `coracao`, `tripe_celular` e `janela` (tela de vídeo com uma pessoa dentro).
- **Detalhes de vida.** Tracinhos amarelos de destaque (`brilhos`), fios brancos curvos ligando a ideia às plataformas (`fio`), balões de fala.

## Regras de composição

1. **A cena nasce do conteúdo.** Antes de desenhar, escreva em uma frase o que a seção diz e o que a cena mostra (ex.: "Agende uma conversa" → café virtual por chamada de vídeo). Se a cena não acrescenta nada ao texto, a seção fica sem ilustração.
2. **Poucas cenas por página.** Uma cena grande no primeiro bloco e, no máximo, mais uma ou duas em seções com espaço. Nunca uma ilustração por seção. Ícones pequenos de lista (desenho do kit em 120x120, direto no fundo da página e sem círculo atrás, como as dores de /ciencia/; no fundo branco, nada de peça branca) não contam como cena: servem para trocar símbolos repetidos, um desenho diferente por item.
3. **Tronco nunca cortado no ar.** Pessoa termina atrás de uma mesa, da borda da cena ou de outro objeto.
4. **Ordem de desenho.** Fios primeiro, depois ícones, depois pessoas, por último quem tem pose "fala" (o braço levantado precisa ficar na frente) e então mesa e objetos. Confira se nenhum objeto esconde a mão de quem fala.
5. **Fundo.** A cena é transparente e pensada para o fundo onde vai entrar (bg1 no hero, roxo, laranja, amarelo, branco). No bg1 e no roxo, evitar roupa roxa (some no fundo).
6. **Continua valendo o resto da marca:** um símbolo grande em baixa opacidade, nada de degradê em CSS, contraste do texto.

## Passo a passo

1. Abra `cenas.py` e crie uma função nova seguindo `home_topo()` ou `home_conversa()`, usando só as peças de `kit.py`. Se faltar uma peça, crie em `kit.py` no mesmo estilo (formas chapadas, cores do kit) e reaproveite.
2. Registre a cena em `CENAS` com o nome `ilustra-<pagina>-<secao>-v1` e rode `python3 marca/ilustracoes/cenas.py`. O SVG sai em `public/assets/` e a prévia PNG, sobre o fundo certo, em `marca/ilustracoes/previas/` (fora do git).
3. **Abra a prévia com Read e olhe de verdade.** Confira: mão de quem fala visível, nenhum objeto cortado ou flutuando, tronco atrás de algo, peças sem encostar umas nas outras, cores certas no fundo certo. Corrija e gere de novo até ficar bom. Pular este passo é o que faz a ilustração sair ruim.
4. Coloque na página com `<img src="/assets/ilustra-....svg" width=".." height=".." alt="...">`: `width` e `height` do viewBox, `height: auto` no estilo e um `alt` que descreve a cena. Ilustração é SVG (exceção à regra do WebP: é vetor, fica nítida em qualquer tela e é leve).
5. Siga a checagem da skill seja-lp-design: `npm run build`, screenshots em 1440, 768 e 390, e olhe a cena dentro da página.
6. Mudou o desenho de uma cena já publicada? Suba a versão no nome (`-v2`) e troque a referência na página.

## Fora do site

Para posts, carrosséis e outras peças, use as mesmas funções: gere a cena no tamanho da arte (ex.: 1080 de largura) e leve o SVG para o Design do Claude ou para a ferramenta da arte. O carrossel "E se a nossa pesquisa virasse podcast?" foi o primeiro teste do estilo.
