# Seja Creator · Landing pages

Repositório das páginas estáticas da Seja Creator, empresa especializada em divulgação científica nas plataformas digitais (Filipe Severo e Igor da Silva).

## Estrutura

Tudo fica no domínio principal:

| Arquivo | Endereço |
|---|---|
| `src/pages/index.astro` | https://sejacreator.com.br (home) |
| `src/pages/ciencia/index.astro` | https://sejacreator.com.br/ciencia/ |
| `src/pages/aula/index.astro` | https://sejacreator.com.br/aula/ |

O site é feito em Astro (gera HTML estático, sem JavaScript extra). Os arquivos de cada página (fontes Futuru, logos, símbolos, bg1.png, fotos, favicon) ficam em `public/` (home: `public/assets/`; demais: `public/<nome>/assets/`). CSS e scripts das páginas usam `<style is:inline>` e `<script is:inline>`, para o Astro não reescrever nada.

Hospedagem e DNS no Cloudflare (plano grátis): um Worker (`wrangler.jsonc`) roda `npm run build` e publica `dist/` a cada push na `main`. O `worker/index.js` faz os redirecionamentos permanentes: www leva ao endereço sem www, e as páginas antigas da Wix (/blank, /sejapesquisa) e /home levam para as novas. Endereço que mudar entra lá. O site não usa subdomínios: toda página nova é uma pasta do domínio principal (os antigos ciencia., aula. e inicio. foram desligados).

Página nova: criar `src/pages/<nome>/index.astro` e `public/<nome>/assets/`. Ela sai em sejacreator.com.br/<nome>/ sem configuração extra. Só o que sai em `dist/` (páginas de `src/pages/` e arquivos de `public/`) é publicado.

Domínio: sejacreator.com.br registrado no Registro.br (sem provedor), com os servidores DNS do Cloudflare. No Worker seja-creator estão ligados só sejacreator.com.br e www (Production); o endereço workers.dev de produção fica desligado. Cada PR ganha uma prévia em `*-seja-creator.sejacreatordrive.workers.dev`, marcada com noindex para não entrar no Google. Não há e-mail no domínio (nenhum registro MX).

## SEO

- Toda página tem `<link rel="canonical">` com o endereço oficial (https://sejacreator.com.br/<nome>/), `og:*` e `twitter:card`, com a imagem de compartilhamento `public/assets/og-seja.png` (1200×630).
- Dados estruturados (JSON-LD, `<script type="application/ld+json" is:inline>`): a home tem a Organization (`#organizacao`, com os sócios) e o WebSite (`#site`); as demais páginas têm um WebPage ligado a eles.
- O sitemap (`/sitemap-index.xml`) sai sozinho do `@astrojs/sitemap` (a 404 fica de fora). `public/robots.txt` libera buscadores e assistentes de IA. `public/llms.txt` resume a Seja para IAs: atualizar quando mudar serviço, página ou posicionamento, usando só o texto que já está no site.
- Página nova: título e descrição próprios, canonical, og e um WebPage em JSON-LD, seguindo /ciencia/ como modelo.

## Como trabalhar

- Antes de mexer em qualquer página, siga a skill `.claude/skills/seja-lp-design/SKILL.md` (identidade visual, regras de layout, tom de voz e checagem com screenshots). Para revisão técnica, use `.claude/skills/web-design-guidelines/SKILL.md`.
- Prévia: `npm install` uma vez, depois `npm run dev` e abra http://localhost:4321/ (ou /ciencia/, /aula/). Antes de enviar, `npm run build` precisa terminar sem erro. Node 22.23.4 ou mais novo (o Cloudflare usa o 24, ver `.nvmrc`). Para testar os redirecionamentos como no Cloudflare: `npm run build` e `npx wrangler dev`.
- No `.astro`, chaves `{ }` fora de `<style>` e `<script>` viram código: num texto que precise delas, escreva `{'{'}` e `{'}'}`.
- Ajustes visuais podem ser explorados no Design do Claude (canvas). Ele é rascunho: o que for aprovado lá é passado para o HTML deste repositório, que é a versão oficial.

## Design do Claude

- Design system da marca: https://claude.ai/artifact/7uVBRdfP9oNts7onCbcpFS ("Seja Creator": cores, Futuru, logos, símbolos, bg1, fotos dos sócios e as seções Botao, Hero, Dado, Servico, Rodape, Titulo, Acordeao, Pessoa, Projeto, Fechamento). Todo canvas novo de página da Seja usa ele.
- Fluxo: (1) rascunhar a página nova num canvas do Design ("LP <nome> · Seja Creator"); (2) aprovar com Filipe/Igor; (3) passar para `src/pages/<nome>/index.astro` seguindo a skill seja-lp-design; (4) push na `main` publica.
- Mudou cor, fonte, logo ou um bloco padrão no repositório? Atualizar também o design system para os dois não divergirem.
- Commits pequenos e descritivos, em português.

## Regras que não podem ser esquecidas

- Cores: roxo #8338EB, rosa #FF006E, azul #3A86FE, laranja #FB5507, amarelo #FFBE0C, texto #1A1A2E. Fonte única Futuru, corpo em 500.
- bg1.png só no hero; resto em cores sólidas; nada de degradê em CSS, sombras, glass ou textura repetida do símbolo. Outro degradê (como os do site sejacreator.com.br) só quando o Filipe pedir, e só no elemento que ele indicar.
- Texto: sem travessão (—), sem "não é X, é Y", sem jargão de startup (escalar, clientes, leads, cases de sucesso, mindset, conversão). Usar "caminhar ao lado", "parceiros", "Histórias que ajudamos a contar".
- Nunca inventar números, depoimentos ou parceiros. Todo dado com fonte, na redação exata de `notas/dados-com-fonte.md`; dado novo só entra depois de conferido no documento original e registrado lá.
- WhatsApp: `https://wa.me/5551991006411?text=` + mensagem URL-encoded e contextual.
- Rodapé: CNPJ 24.560.652/0001-49.
- A Classe Creator é projeto pessoal do Filipe, não da Seja. Não apresentar como serviço, formação ou braço da Seja; as formações da Seja são outras.

## Na página da aula

- Não incluir links de influenciadores; só projetos de divulgação científica.
- O texto da Classe Creator deve ser idêntico ao do site classecreator.com.
- O formulário de presença é da organização do evento (VII Semidiscom · PPGCOM/UFRGS).
