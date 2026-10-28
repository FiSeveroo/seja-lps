# Seja Creator · Landing pages

Repositório das páginas estáticas da Seja Creator, empresa especializada em divulgação científica nas plataformas digitais (Filipe Severo e Igor da Silva).

## Estrutura

| Pasta | Site no ar | Netlify |
|---|---|---|
| `ciencia/` | https://ciencia.sejacreator.com.br | ciencialpseja.netlify.app |
| `aula/` | https://aula.sejacreator.com.br | marvelous-blancmange-e93061.netlify.app |

Cada pasta é um site independente: `index.html` + `assets/` (fontes Futuru, logos, símbolos, bg1.png). HTML e CSS puros, sem build. No Netlify, cada site usa a própria pasta como *Base directory* e *Publish directory*, e publica sozinho a cada push na `main`.

## Como trabalhar

- Antes de mexer em qualquer página, siga a skill `.claude/skills/seja-lp-design/SKILL.md` (identidade visual, regras de layout, tom de voz e checagem com screenshots). Para revisão técnica, use `.claude/skills/web-design-guidelines/SKILL.md`.
- Prévia: abra `ciencia/index.html` direto no navegador, ou rode `npx serve ciencia`.
- Ajustes visuais podem ser explorados no Design do Claude (canvas). Ele é rascunho: o que for aprovado lá é passado para o HTML deste repositório, que é a versão oficial.
- Commits pequenos e descritivos, em português.

## Regras que não podem ser esquecidas

- Cores: roxo #8338EB, rosa #FF006E, azul #3A86FE, laranja #FB5507, amarelo #FFBE0C, texto #1A1A2E. Fonte única Futuru, corpo em 500.
- bg1.png só no hero; resto em cores sólidas; nada de degradê em CSS, sombras, glass ou textura repetida do símbolo.
- Texto: sem travessão (—), sem "não é X, é Y", sem jargão de startup (escalar, clientes, leads, cases de sucesso, mindset, conversão). Usar "caminhar ao lado", "parceiros", "Histórias que ajudamos a contar".
- Nunca inventar números, depoimentos ou parceiros. Todo dado com fonte.
- WhatsApp: `https://wa.me/5551991006411?text=` + mensagem URL-encoded e contextual.
- Rodapé: CNPJ 24.560.652/0001-49.

## Na página da aula

- Não incluir links de influenciadores; só projetos de divulgação científica.
- O texto da Classe Creator deve ser idêntico ao do site classecreator.com.
- O formulário de presença é da organização do evento (VII Semidiscom · PPGCOM/UFRGS).
