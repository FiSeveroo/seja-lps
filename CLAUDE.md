# Seja Creator · Landing pages

Repositório das páginas estáticas da Seja Creator, empresa especializada em divulgação científica nas plataformas digitais (Filipe Severo e Igor da Silva).

## Estrutura

| Pasta | Endereço |
|---|---|
| `src/pages/ciencia/` | https://ciencia.sejacreator.com.br |
| `src/pages/aula/` | https://aula.sejacreator.com.br |
| `src/pages/home/` | https://inicio.sejacreator.com.br (home nova; sejacreator.com.br segue na Wix por enquanto) |

O site é feito em Astro (gera HTML estático, sem JavaScript extra). Cada página é `src/pages/<nome>/index.astro`, e seus arquivos (fontes Futuru, logos, símbolos, bg1.png, fotos, favicon) ficam em `public/<nome>/`. CSS e scripts das páginas usam `<style is:inline>` e `<script is:inline>`, para o Astro não reescrever nada. Um único projeto no Netlify (ciencialpseja) roda `npm run build` e publica a pasta `dist/` (ver `netlify.toml`) a cada push na `main`. O arquivo `public/_redirects` liga cada subdomínio à sua pasta.

Página nova: criar `src/pages/<nome>/index.astro` e `public/<nome>/assets/`, adicionar a linha `https://<nome>.sejacreator.com.br/*  /<nome>/:splat  200!` no `_redirects` (antes da regra de `/`), adicionar `<nome>.sejacreator.com.br` como domínio do projeto no Netlify e criar na Wix o CNAME `<nome>` → `ciencialpseja.netlify.app`. Só o que sai em `dist/` (páginas de `src/pages/` e arquivos de `public/`) é publicado.

## Como trabalhar

- Antes de mexer em qualquer página, siga a skill `.claude/skills/seja-lp-design/SKILL.md` (identidade visual, regras de layout, tom de voz e checagem com screenshots). Para revisão técnica, use `.claude/skills/web-design-guidelines/SKILL.md`.
- Prévia: `npm install` uma vez, depois `npm run dev` e abra http://localhost:4321/ciencia/ (ou /home/, /aula/). Antes de enviar, `npm run build` precisa terminar sem erro. Node 22.23.4 ou mais novo (o Netlify usa o 24, ver `.nvmrc`).
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
