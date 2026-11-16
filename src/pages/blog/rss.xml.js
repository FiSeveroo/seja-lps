// Feed RSS do blog: /blog/rss.xml
import rss from '@astrojs/rss';
import { postsPublicados } from '../../data/blog';
import { autores } from '../../data/autores';

export async function GET(context) {
  const posts = await postsPublicados();
  return rss({
    title: 'Blog da Seja Creator',
    description: 'Divulgação científica nas plataformas digitais, por Filipe Severo e Igor da Silva.',
    site: context.site,
    customData: '<language>pt-BR</language>',
    items: posts.map((post) => ({
      title: post.data.titulo,
      description: post.data.descricao,
      pubDate: post.data.data,
      link: `/blog/${post.id}/`,
      author: autores[post.data.autor].nome,
    })),
  });
}
