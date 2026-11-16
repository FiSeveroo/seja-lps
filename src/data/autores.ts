// Autores do blog. Bios iguais às da home (seção "Feito por").
export const autores = {
  'filipe-severo': {
    nome: 'Filipe Severo',
    frase: 'Estratégia e pesquisa',
    bio: 'Pesquisador, mestre em comunicação social e pós-graduado em influência digital, com 10 anos atuando como criador de conteúdo.',
    foto: '/assets/filipe-severo.jpg',
    links: ['https://www.instagram.com/severo_filipe/'],
  },
  'igor-da-silva': {
    nome: 'Igor da Silva',
    frase: 'Criação e tecnologia',
    bio: 'Formado em Tecnologia da Informação. Construiu o maior canal de Vasco do Brasil, o Atenção, Vascaínos!',
    foto: '/assets/igor-silva.jpg',
    links: [] as string[],
  },
} as const;

export type AutorId = keyof typeof autores;
