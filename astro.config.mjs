// Configuração do Astro. A home é src/pages/index.astro; as demais páginas
// ficam em src/pages/<nome>/index.astro, com as imagens em public/assets/.
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync } from 'node:fs';

// Data de cada post (atualizado ou data, do cabeçalho do .md), para o
// <lastmod> do sitemap. /blog/ leva a data do post mais recente.
const datas = {};
const pasta = './src/content/blog';
for (const arquivo of readdirSync(pasta)) {
  if (!arquivo.endsWith('.md') || arquivo.startsWith('_')) continue;
  const texto = readFileSync(`${pasta}/${arquivo}`, 'utf8');
  if (/^rascunho:\s*true/m.test(texto)) continue;
  const campo = (nome) => texto.match(new RegExp(`^${nome}:\\s*"?(\\d{4}-\\d{2}-\\d{2})`, 'm'))?.[1];
  const data = campo('atualizado') ?? campo('data');
  if (data) datas[`https://sejacreator.com.br/blog/${arquivo.slice(0, -3)}/`] = data;
}
const maisRecente = Object.values(datas).sort().at(-1);
if (maisRecente) datas['https://sejacreator.com.br/blog/'] = maisRecente;

export default defineConfig({
  site: 'https://sejacreator.com.br',
  build: { format: 'directory' },
  compressHTML: false,
  integrations: [
    // Gera /sitemap-index.xml com todas as páginas, menos a 404
    sitemap({
      filter: (pagina) => !pagina.includes('/404'),
      serialize: (item) => (datas[item.url] ? { ...item, lastmod: datas[item.url] } : item),
    }),
  ],
});
