// Configuração do Astro. Cada página fica em src/pages/<nome>/index.astro
// e seus arquivos (fontes, logos, fotos) em public/<nome>/.
import { defineConfig } from 'astro/config';

export default defineConfig({
  build: { format: 'directory' },
  compressHTML: false,
});
