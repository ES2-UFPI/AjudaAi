demandas = [
    {
        'codDemanda': 1,
        'titulo': 'Monitoria sobre Bioquímica',
        'tags': 'BIOLOGIA - Bioquímica; BIOLOGIA - Biologia I',
        'tipo': 'Aberto a membros',
        'descricao': 'Gostaria de alguém para me auxiliar sobre estrutura e função metabólica de componentes celulares.',
        'status': 'Em aberto',
        'codUsuario': 3
    },
    {
        'codDemanda': 2,
        'titulo': 'Revisão do Abstract',
        'tags': 'INGLÊS: A1; INGLÊS: Gramática; INGLÊS: Revisão abstract',
        'tipo': 'Individual',
        'descricao': 'Possuo conhecimento básico de inglês e procuro monitoria para revisar comigo o abstract do meu artigo.',
        'status': 'Em aberto',
        'codUsuario': 1
    },
    {
        'codDemanda': 3,
        'titulo': 'Monitoria de programação',
        'tags': 'COMPUTAÇÃO: Algoritmo; COMPUTAÇÃO: Programação Estruturada; COMPUTAÇÃO: Linguagem C',
        'tipo': 'Aberto a membros',
        'descricao': 'Sou estudante de bioinformática e preciso aprender scripts em python, mas possuo dificuldade em lógica de programação.',
        'status': 'Finalizado',
        'codUsuario': 1
    },
    {
        'codDemanda': 4,
        'titulo': 'Monitoria sobre Cálculo',
        'tags': 'CÁLCULO: Derivadas; CÁLCULO: Integrais',
        'tipo': 'Individual',
        'descricao': 'Gostaria de alguém para me auxiliar na parte derivadas e integrais. Estou com muita dificuldade.',
        'status': 'Em aberto',
        'codUsuario': 5
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
        ]
    },
    {
        'codUsuario': 2,
        'nome': 'João Victor',
        'email': 'jaovctr@ufpi.edu.br',
        'tags': [
            'COMPUTAÇÃO - Banco de Dados',
            'LETRAS INGLÊS - Confecção de Abstract',
            '#programacao'
        ]
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
        ]
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
        ]
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
        ]
    },
    {
        'codUsuario': 6,
        'nome': 'Marcelo Carvalho',
        'email': 'marcelocarvalho@ufpi.edu.br',
        'tags': []
    },
    {
        'codUsuario': 7,
        'nome': 'Sara Eduarda',
        'email': 'saraeduarda@ufpi.edu.br',
        'tags': []
    },
    {
        'codUsuario': 8,
        'nome': 'Larissa Silva',
        'email': 'larissasilva@ufpi.edu.br',
        'tags': []
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


def prox_id_demanda():
    return demandas[-1]['codDemanda'] + 1


def prox_id_topico():
    return topicos_forum[-1]['id'] + 1


def prox_id_comentario():
    return comentarios[-1]['id'] + 1