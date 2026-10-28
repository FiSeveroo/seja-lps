---
name: "seja-lp-design"
description: "Use ao criar, redesenhar ou revisar landing pages e páginas web da Seja Creator (ex.: ciencia.sejacreator.com.br, aula.sejacreator.com.br): identidade visual, regras de layout, tom de voz e checagem visual com screenshots."
---

# Seja Creator: design de landing pages

Um DESIGN.md da Seja (no formato popularizado pelo Google Stitch / awesome-design-md) somado a um método anti-"cara de IA" adaptado do tasteskill e a um ciclo de checagem visual com Playwright. Use em toda LP ou página da Seja.

## 1. Posicionamento que a página precisa carregar

- A Seja é uma empresa especializada em divulgação científica nas plataformas digitais. Caminha ao lado de pesquisadores, grupos de pesquisa e projetos acadêmicos.
- Sócios: Filipe Severo (Fi), pesquisador, mestre em comunicação social, pós-graduado em influência digital; Igor da Silva, criação e tecnologia. Não usar títulos tipo "Diretor"; preferir frases descritivas ("Estratégia e pesquisa", "Criação e tecnologia").
- Antes de desenhar, liste 8 a 12 coisas que pertencem só a este projeto (o edital, a CAPES, o grupo, o evento, a data, a universidade, o material real). A ideia da página sai dessa lista, nunca da categoria "agência".

## 2. Tokens de marca

```css
:root{
  --roxo:#8338EB; --rosa:#FF006E; --azul:#3A86FE;
  --laranja:#FB5507; --amarelo:#FFBE0C; --texto:#1A1A2E; --branco:#FFFFFF;
}
```

- Fonte única: Futuru (.otf, todos os pesos via @font-face, `font-display: swap`). Corpo em Futuru Medium (500), títulos em pesos altos. Corpo mínimo 18px no desktop.
- Logos: Logotipo_SEJA_BRANCO / ROSA / ROXO.png. Logo no hero com ~120px de altura (pequeno demais já foi recusado).
- Símbolos: Simbolo_SEJA_{ROSA,ROXO,LARANJA,AMARELO,PRETO,BRANCO}.png. Usar como UMA imagem grande de fundo em baixa opacidade, ou como ícone de serviço. Nunca como textura repetida.
- bg1.png (degradê azul→roxo da marca) só no hero. Fora dele, blocos em cor sólida (roxo, rosa, amarelo) alternando com fundo claro. Nada de degradês criados em CSS.
- Peça os arquivos ao usuário se não estiverem na sessão; não invente substitutos.

## 3. Regras de casa

| Evitar | Fazer |
|---|---|
| Degradês em CSS, brilhos, sombras em elementos parados, glass/blur | Cor sólida da marca; contraste por mudança de campo de cor |
| Rótulo pequeno em caixa-alta acima do título (eyebrow), pílulas "Novo" | Informação no próprio título ou na primeira frase |
| Fileiras de cards idênticos com ícone em cima | Composição diferente em cada seção vizinha |
| Textura repetida do símbolo | Um símbolo grande, baixa opacidade |
| Monospace, fontes extras | Só Futuru |
| Títulos de 3+ linhas | Título com até 2 linhas em qualquer largura; cortar palavras antes de reduzir fonte |
| Bloco grande alinhado à esquerda com metade da tela vazia | Centralizar momentos de destaque (ex.: bloco CAPES) ou fechar o vazio com imagem/coluna |
| Caixas de destaque redundantes repetindo o que o texto já disse | Remover |
| Dados sem fonte | Todo número com fonte visível (ex.: CAPES Portaria nº 109/2025) |

Páginas sempre com um `h1` claro no primeiro bloco, um título em cada seção, margens iguais, versão mobile pensada (fontes com override próprio).

## 4. Tom de voz (obrigatório)

- Humano, acolhedor, analítico, sem jargão de startup e sem gen Z.
- Proibido: startup, escalar, escalonar, cases de sucesso, clientes, leads, conversão, mindset, tracionar, "vender a essência" e outros clichês.
- Usar: caminhar ao lado, apoio, parceiros, comunidade, impacto social, histórias que ajudamos a contar, Quem caminha com a gente.
- Fugir de padrões de texto de IA: não usar travessão (—), não usar a estrutura "não é X, é Y", nada agressivo ou sarcástico.
- Não inventar provas: nada de depoimentos, números, logos ou parceiros que o usuário não forneceu. Dados de parceiros só com autorização.

## 5. Estrutura típica (LP de divulgação científica)

Hero (bg1, logo, h1 curto, uma frase de apoio, um botão rosa para WhatsApp) → dores → dados com fonte (bloco sólido) → contexto CAPES/editais → serviços (Projeto, Parceria contínua, Formação) → histórias que ajudamos a contar → CTA final sólido → rodapé com CNPJ 24.560.652/0001-49.

Botões de WhatsApp: `https://wa.me/5551991006411?text=` + mensagem pré-escrita (URL-encoded), contextual à página.

## 6. Checagem visual (antes de entregar)

Playwright e Chromium costumam estar pré-instalados no ambiente (não rodar `playwright install`). Tirar screenshots de página inteira em 1440, 768 e 390px:

```js
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const w of [1440, 768, 390]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    await p.goto('file://' + process.argv[2]);
    await p.waitForTimeout(800);
    await p.screenshot({ path: `shot-${w}.png`, fullPage: true });
  }
  await b.close();
})();
```

Abrir cada screenshot com Read e conferir: títulos com até 2 linhas, nenhum overflow horizontal, logo legível, fontes Futuru carregadas, contraste do texto sobre roxo/rosa/amarelo, nenhum trecho vazio maior que meia tela, botões visíveis no primeiro bloco do mobile. Corrigir os 3 piores problemas e repetir (máx. 3 rodadas). Se a skill web-design-guidelines estiver disponível, rodar também.

## 7. Publicação

- Netlify Drop (arrastar a pasta ou .zip com index.html + assets/) é gratuito.
- Subdomínio via DNS da Wix (domínio sejacreator.com.br): primeiro um TXT `subdomain-owner-verification` com o hash do Netlify, depois o CNAME `<sub>` → `<site>.netlify.app`. Cadastrar no Netlify o domínio com .com.br.
- Entregar sempre o .zip pronto para arrastar.