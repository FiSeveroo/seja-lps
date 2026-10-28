# Seja Creator · Landing pages

Repositório das páginas estáticas da Seja Creator, empresa especializada em divulgação científica nas plataformas digitais (Filipe Severo e Igor da Silva).

## Estrutura

| Pasta | Endereço |
|---|---|
| `site/ciencia/` | https://ciencia.sejacreator.com.br |
| `site/aula/` | https://aula.sejacreator.com.br |

Um único projeto no Netlify (ciencialpseja) publica a pasta `site/` (ver `netlify.toml`) a cada push na `main`. O arquivo `site/_redirects` liga cada subdomínio à sua pasta. Cada página é `index.html` + `assets/` próprios (fontes Futuru, logos, símbolos, bg1.png), HTML e CSS puros, sem build.

Página nova: criar `site/<nome>/index.html` com seus `assets/`, adicionar a linha `https://<nome>.sejacreator.com.br/*  /<nome>/:splat  200!` no `_redirects` (antes da regra de `/`), adicionar `<nome>.sejacreator.com.br` como domínio do projeto no Netlify e criar na Wix o CNAME `<nome>` → `ciencialpseja.netlify.app`. Nada fora de `site/` é publicado.

## Como trabalhar

- Antes de mexer em qualquer página, siga a skill `.claude/skills/seja-lp-design/SKILL.md` (identidade visual, regras de layout, tom de voz e checagem com screenshots). Para revisão técnica, use `.claude/skills/web-design-guidelines/SKILL.md`.
- Prévia: abra `site/ciencia/index.html` direto no navegador, ou rode `npx serve site` e abra /ciencia.
- Ajustes visuais podem ser explorados no Design do Claude (canvas). Ele é rascunho: o que for aprovado lá é passado para o HTML deste repositório, que é a versão oficial.

## Design do Claude

- Design system da marca: https://claude.ai/artifact/7uVBRdfP9oNts7onCbcpFS ("Seja Creator": cores, Futuru, logos, símbolos, bg1 e as seções Botao, Hero, Dado, Servico, Rodape). Todo canvas novo de página da Seja usa ele.
- Fluxo: (1) rascunhar a página nova num canvas do Design ("LP <nome> · Seja Creator"); (2) aprovar com Filipe/Igor; (3) passar para `site/<nome>/index.html` seguindo a skill seja-lp-design; (4) push na `main` publica.
- Mudou cor, fonte, logo ou um bloco padrão no repositório? Atualizar também o design system para os dois não divergirem.
- Commits pequenos e descritivos, em português.

## Regras que não podem ser esquecidas

- Cores: roxo #8338EB, rosa #FF006E, azul #3A86FE, laranja #FB5507, amarelo #FFBE0C, texto #1A1A2E. Fonte única Futuru, corpo em 500.
- bg1.png só no hero; resto em cores sólidas; nada de degradê em CSS, sombras, glass ou textura repetida do símbolo.
- Texto: sem travessão (—), sem "não é X, é Y", sem jargão de startup (escalar, clientes, leads, cases de sucesso, mindset, conversão). Usar "caminhar ao lado", "parceiros", "Histórias que ajudamos a contar".
- Nunca inventar números, depoimentos ou parceiros. Todo dado com fonte.
- WhatsApp: `https://wa.me/5551991006411?text=` + mensagem URL-encoded e contextual.
- Rodapé: CNPJ 24.560.652/0001-49.

## Na página da aula

- Não incluir links de influenciadores; só projetos de divulgação científica.
- O texto da Classe Creator deve ser idêntico ao do site classecreator.com.
- O formulário de presença é da organização do evento (VII Semidiscom · PPGCOM/UFRGS).
