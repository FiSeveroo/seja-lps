// Autores do blog. A bio é a do "Sobre o autor" enviada com os posts.
export const autores = {
  'filipe-severo': {
    nome: 'Filipe Severo',
    nomeCompleto: 'Filipe Machado Leal Severo',
    frase: 'Estratégia e pesquisa',
    cargo: 'Pesquisador em comunicação e plataformas digitais',
    bio: 'Filipe Severo é pesquisador e mestre em Comunicação Social pela PUCRS. Há dez anos trabalha com conteúdo para plataformas digitais e hoje se dedica à divulgação científica. Fundou a Classe Creator, que estuda e forma quem trabalha na produção cultural das plataformas.',
    // Página de autor no site (aparece nos posts e nos dados estruturados)
    pagina: '/autor/filipe-severo/' as string | undefined,
    foto: '/assets/filipe-severo.webp',
    links: [
      'http://lattes.cnpq.br/1675366659630964',
      'https://www.linkedin.com/in/filipe-severo/',
      'https://www.instagram.com/severo_filipe/',
    ],
  },
  'igor-da-silva': {
    nome: 'Igor da Silva',
    nomeCompleto: undefined,
    frase: 'Criação e tecnologia',
    cargo: 'Criação e tecnologia',
    bio: 'Formado em Tecnologia da Informação. Construiu o maior canal de Vasco do Brasil, o Atenção, Vascaínos!',
    pagina: undefined as string | undefined,
    foto: '/assets/igor-silva.webp',
    links: [] as string[],
  },
} as const;

export type AutorId = keyof typeof autores;
