// Worker do site da Seja no Cloudflare.
// Leva o www e os endereços antigos das páginas da Wix para os novos
// com redirecionamento permanente (301) e entrega o resto direto de dist/.

const DOMINIO = 'sejacreator.com.br';

// Outro nome do domínio → pasta no domínio principal.
// O site não usa subdomínios: só o www, que leva ao endereço sem www.
const SUBDOMINIOS = {
  'www.sejacreator.com.br': '/',
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

    const resposta = await env.ASSETS.fetch(request);

    // Prévias de PR (*.workers.dev) não entram no Google
    if (url.hostname.endsWith('.workers.dev')) {
      const previa = new Response(resposta.body, resposta);
      previa.headers.set('X-Robots-Tag', 'noindex');
      return previa;
    }
    return resposta;
  },
};
