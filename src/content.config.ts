// Coleção do blog. Cada post é um arquivo .md em src/content/blog/.
// Arquivos que começam com _ (como _modelo.md) não são publicados.
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/blog' }),
  schema: ({ image }) =>
    z.object({
      titulo: z.string().max(100),
      // Aparece no Google e ao compartilhar: entre 70 e 160 caracteres
      descricao: z.string().min(70).max(160),
      data: z.coerce.date(),
      atualizado: z.coerce.date().optional(),
      autor: z.enum(['filipe-severo', 'igor-da-silva']),
      capa: image().optional(),
      capaAlt: z.string().optional(),
      rascunho: z.boolean().default(false),
    }),
});

export const collections = { blog };
