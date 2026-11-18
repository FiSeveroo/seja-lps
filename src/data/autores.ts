// Autores do blog. A bio é a do "Sobre o autor" enviada com os posts.
export const autores = {
  'filipe-severo': {
    nome: 'Filipe Severo',
    nomeCompleto: 'Filipe Machado Leal Severo',
    frase: 'Estratégia e pesquisa',
    cargo: 'Pesquisador em comunicação e plataformas digitais',
    bio: 'Pesquisador, mestre em Comunicação Social pela PUCRS e membro fundador da Classe Creator. Trabalha há dez anos com conteúdo para plataformas digitais e é sócio da Seja Creator, especializada em divulgação científica digital.',
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
    foto: '/assets/igor-silva.webp',
    links: [] as string[],
  },
} as const;

export type AutorId = keyof typeof autores;
