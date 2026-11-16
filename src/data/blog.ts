// Funções do blog: lista de posts publicados e datas por extenso.
import { getCollection } from 'astro:content';

export async function postsPublicados() {
  const posts = await getCollection('blog', ({ data }) => !data.rascunho);
  return posts.sort((a, b) => b.data.data.valueOf() - a.data.data.valueOf());
}

const formato = new Intl.DateTimeFormat('pt-BR', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
export const dataPorExtenso = (d: Date) => formato.format(d);
export const dataISO = (d: Date) => d.toISOString().slice(0, 10);
