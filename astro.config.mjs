// Configuração do Astro. A home é src/pages/index.astro; as demais páginas
// ficam em src/pages/<nome>/index.astro e seus arquivos em public/<nome>/.
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://sejacreator.com.br',
  build: { format: 'directory' },
  compressHTML: false,
  integrations: [
    // Gera /sitemap-index.xml com todas as páginas, menos a 404
    sitemap({ filter: (pagina) => !pagina.includes('/404') }),
  ],
});
