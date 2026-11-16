# seja-lps

Site da Seja Creator: https://sejacreator.com.br

- `src/pages/index.astro` → sejacreator.com.br
- `src/pages/ciencia/` → sejacreator.com.br/ciencia/
- `src/pages/aula/` → sejacreator.com.br/aula/

Site em Astro, gerado como HTML estático; fontes e imagens ficam em `public/`. Para ver no computador: `npm install` e `npm run dev`. O Cloudflare roda `npm run build` e publica `dist/` a cada push na `main`; `worker/index.js` leva os endereços antigos (subdomínios e páginas da Wix) para os novos. Detalhes de identidade, tom de voz e fluxo de trabalho em `CLAUDE.md`.
