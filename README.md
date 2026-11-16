# seja-lps

Landing pages da Seja Creator.

- `src/pages/ciencia/` → ciencia.sejacreator.com.br
- `src/pages/aula/` → aula.sejacreator.com.br
- `src/pages/home/` → inicio.sejacreator.com.br

Site em Astro, gerado como HTML estático. Fontes, imagens e o `_redirects` ficam em `public/`. Para ver no computador: `npm install` e `npm run dev`. Um único projeto no Netlify roda `npm run build` e publica `dist/` a cada push na `main`; `public/_redirects` liga cada subdomínio à sua pasta. Detalhes de identidade, tom de voz e fluxo de trabalho em `CLAUDE.md`.
