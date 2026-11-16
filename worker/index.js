// Worker do site da Seja no Cloudflare.
// Leva os endereços antigos (subdomínios e páginas da Wix) para os novos
// com redirecionamento permanente (301) e entrega o resto direto de dist/.

const DOMINIO = 'sejacreator.com.br';

// Subdomínio antigo → pasta no domínio principal
const SUBDOMINIOS = {
  'www.sejacreator.com.br': '/',
  'inicio.sejacreator.com.br': '/',
  'ciencia.sejacreator.com.br': '/ciencia/',
  'aula.sejacreator.com.br': '/aula/',
};

// Página antiga → página nova (sem barra no fim, em minúsculas)
const PAGINAS = {
  '/home': '/',
  '/blank': '/ciencia/',
  '/sejapesquisa': '/ciencia/',
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    const pasta = SUBDOMINIOS[url.hostname];
    if (pasta) {
      const caminho = (pasta + url.pathname.slice(1)).replace(/\/{2,}/g, '/');
      return Response.redirect(`https://${DOMINIO}${caminho}${url.search}`, 301);
    }

    const pagina = PAGINAS[url.pathname.replace(/\/+$/, '').toLowerCase()];
    if (pagina) {
      url.pathname = pagina;
      return Response.redirect(url.toString(), 301);
    }

    return env.ASSETS.fetch(request);
  },
};
