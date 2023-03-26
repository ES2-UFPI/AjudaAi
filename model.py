demandas = [
    {
        'codDemanda': 1,
        'titulo': 'Monitoria sobre Bioquímica',
        'tags': 'BIOLOGIA - Bioquímica; BIOLOGIA - Biologia I',
        'tipo': 'Aberto a membros',
        'descricao': 'Gostaria de alguém para me auxiliar sobre estrutura e função metabólica de componentes celulares.',
        'status': 'Em aberto',
        'codUsuario': 3,
        'associados': [],
        'ajudante': 0
    },
    {
        'codDemanda': 2,
        'titulo': 'Revisão do Abstract',
        'tags': 'INGLÊS: A1; INGLÊS: Gramática; INGLÊS: Revisão abstract',
        'tipo': 'Individual',
        'descricao': 'Possuo conhecimento básico de inglês e procuro monitoria para revisar comigo o abstract do meu artigo.',
        'status': 'Em aberto',
        'codUsuario': 5,
        'associados': [],
        'ajudante': 0
    },
    {
        'codDemanda': 3,
        'titulo': 'Monitoria de programação',
        'tags': 'COMPUTAÇÃO: Algoritmo; COMPUTAÇÃO: Programação Estruturada; COMPUTAÇÃO: Linguagem C',
        'tipo': 'Aberto a membros',
        'descricao': 'Sou estudante de bioinformática e preciso aprender scripts em python, mas possuo dificuldade em lógica de programação.',
        'status': 'Aceita',
        'codUsuario': 1,
        'associados': [2,3,4,5],
        'ajudante': 7
    },
    {
        'codDemanda': 4,
        'titulo': 'Monitoria sobre Cálculo',
        'tags': 'CÁLCULO: Derivadas; CÁLCULO: Integrais',
        'tipo': 'Individual',
        'descricao': 'Gostaria de alguém para me auxiliar na parte derivadas e integrais. Estou com muita dificuldade.',
        'status': 'Aceita',
        'codUsuario': 1,
        'associados': [2,3,4,5],
        'ajudante': 8
    },
]

tags = [
        {'nome': 'COMPUTAÇÃO - Programação Estruturada', 'id': 1},
        {'nome': 'COMPUTAÇÃO - Banco de Dados', 'id': 2},
        {'nome': 'ESTATÍSTICA - Análise Combinatória', 'id': 3},
        {'nome': 'FÍSICA - Leis de Newton', 'id': 4},
        {'nome': 'LETRAS INGLÊS - Confecção de Abstract', 'id': 5},
        {'nome': 'LETRAS INGLÊS - Tempos Verbais', 'id': 6}
    ]

usuarios = [
    {
        'codUsuario': 1,
        'nome': 'Caio Feitosa',
        'email': 'caiofeitosa@ufpi.edu.br',
        'tags': [
            'COMPUTAÇÃO - Programação Estruturada',
            'COMPUTAÇÃO - Banco de Dados',
            'LETRAS INGLÊS - Confecção de Abstract',
            '#programacao'
        ],
        'avaliacao': 2,
        'ultimo_comentario_recebido': 'Aceitou a demanda mas simplesmente não apareceu depois.'
    },
    {
        'codUsuario': 2,
        'nome': 'João Victor',
        'email': 'jaovctr@ufpi.edu.br',
        'tags': [
            'COMPUTAÇÃO - Banco de Dados',
            'LETRAS INGLÊS - Confecção de Abstract',
            '#programacao'
        ],
        'avaliacao': 3,
        'ultimo_comentario_recebido': ''
    },
    {
        'codUsuario': 3,
        'nome': 'Ana Letícia',
        'email': 'let0210@ufpi.edu.br',
        'tags': [
            'ESTATÍSTICA - Análise Combinatória',
            'FÍSICA - Leis de Newton',
            'LETRAS INGLÊS - Confecção de Abstract',
            'LETRAS INGLÊS - Tempos Verbais',
            '#programacao'
        ],
        'avaliacao': 4,
        'ultimo_comentario_recebido': 'Muito atenciosa, didática e pontual.'
    },
    {
        'codUsuario': 4,
        'nome': 'Maria Clara',
        'email': 'mariaclaraacoelho@ufpi.edu.br',
        'tags': [
            'ESTATÍSTICA - Análise Combinatória',
            'LETRAS INGLÊS - Confecção de Abstract',
            'LETRAS INGLÊS - Tempos Verbais',
            '#programacao'
        ],
        'avaliacao': 3,
        'ultimo_comentario_recebido': 'Ensina bem, mas poderia melhorar na questão da pontualidade.'
    },
    {
        'codUsuario': 5,
        'nome': 'Anderson',
        'email': 'andersonpereira@ufpi.edu.br',
        'tags': [
            'COMPUTAÇÃO - Banco de Dados',
            'FÍSICA - Leis de Newton',
            'LETRAS INGLÊS - Confecção de Abstract',
            '#programacao'
        ],
        'avaliacao': 3,
        'ultimo_comentario_recebido': ''
    },
    {
        'codUsuario': 6,
        'nome': 'Marcelo Carvalho',
        'email': 'marcelocarvalho@ufpi.edu.br',
        'tags': [],
        'avaliacao': 1,
        'ultimo_comentario_recebido': 'Atrasou a entrega e não respondeu às mensagens.'
    },
    {
        'codUsuario': 7,
        'nome': 'Sara Eduarda',
        'email': 'saraeduarda@ufpi.edu.br',
        'tags': [],
        'avaliacao': 3,
        'ultimo_comentario_recebido': 'Boa tutora.'
    },
    {
        'codUsuario': 8,
        'nome': 'Larissa Silva',
        'email': 'larissasilva@ufpi.edu.br',
        'tags': [],
        'avaliacao': 5,
        'ultimo_comentario_recebido': ''
    }
]

topicos_forum = [
    {
        'id': 1,
        'titulo': 'Como faço para resolver um problema no meu código?',
        'texto': 'Olá pessoal, estou tendo dificuldades em resolver um problema no meu código.'
                + 'Eu estou tentando criar uma função em JavaScript que some dois números,'
                + 'mas não está funcionando. Já tentei várias coisas, mas ainda não consegui'
                + 'encontrar o erro. Alguém pode me ajudar?',
        'tags': ['#programacao', '#javaScript', '#frontend'],
        'codUsuario': 6
    },
    {
        'id': 2,
        'titulo': 'Ajuda em CSS',
        'texto': 'Como fazer um dropdown em CSS?',
        'tags': ['#programacao', '#css', '#frontend'],
        'codUsuario': 7
    },
    {
        'id': 3,
        'titulo': 'Dijkstra em python',
        'texto': 'Considere um grafo não direcionado G com N vértices e M arestas, onde cada'
                + 'aresta tem um peso associado. Escreva uma função em Python que receba G,'
                + 'bem como dois vértices u e v, e retorne o caminho mínimo de u a v em G,'
                + 'usando o algoritmo de Dijkstra. Além disso, a função deve ser capaz de lidar'
                + 'com casos em que u e v não são conectados em G.',
        'tags': ['#programacao', '#python', '#estruturadedados'],
        'codUsuario': 8
    }
]

comentarios = [
    {
        'id': 1,
        'texto': 'Tente verificar se você está passando os argumentos corretamente'
                + 'para a função e se está retornando o valor correto.',
        'codTopico': 1,
        'codUsuario': 1
    },
    {
        'id': 2,
        'texto': 'Verifique se você está declarando a função corretamente'
                + 'e se está usando o operador de adição (+) para somar os números.',
        'codTopico': 1,
        'codUsuario': 5
    },
    {
        'id': 3,
        'texto': 'Se possível, compartilhe seu código para que possamos analisar melhor e te ajudar.',
        'codTopico': 1,
        'codUsuario': 2
    }
]


chat = [
    {
        'codDemanda': 3,
        'mensagens': [
            {
                'codUsuario': 1,
                'texto': 'Olá! Quando podemos marcar uma reunião para a aula?'
            },
            {
                'codUsuario': 7,
                'texto': 'Tenho horários livres às terças e quintas, das 14 às 16.'
            },
            {
                'codUsuario': 1,
                'texto': 'Então vamos marcar para hoje à tarde.'
            },
            {
                'codUsuario': 7,
                'texto': 'Certo!'
            },
            {
                'codUsuario': 7,
                'texto': 'Já criei a sala. Segue o link da reunião pelo meet: https://meet.google.com/wxh-ngzj-ozo. Mais tarde a gente se fala.'
            },
            {
                'codUsuario': 1,
                'texto': 'Tá bom :)'
            }
        ]
    },
    {
        'codDemanda': 4,
        'mensagens': [
            {
                'codUsuario': 1,
                'texto': 'Olá, bom dia!'
            },
        ]
    }
]

fotos_perfil = [
    'icon.png',
    'icon.png',
    'iconboy.png',
    'icon3.png',
    'icon2.png',
    'icon.png',
    'iconboy2.png',
    'icon3.png'
]


def prox_id_demanda():
    return demandas[-1]['codDemanda'] + 1


def prox_id_topico():
    return topicos_forum[-1]['id'] + 1


def prox_id_comentario():
    return comentarios[-1]['id'] + 1