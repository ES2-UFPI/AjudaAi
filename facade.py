from model import *
import notifica

def listagem_tags():
    return tags


def busca_tag_id(id):
    return [t['nome'] for t in tags if t['id'] == id][0]


def busca_demanda_id(id):
    for indice, demanda in enumerate(demandas):
        if demanda['codDemanda'] == id:
            return indice, demanda


def busca_usuario_id(id):
    return [u for u in usuarios if u['codUsuario'] == id][0]


def busca_topico_id(id):
    return [t for t in topicos_forum if t['id'] == id][0]
    

def listagem_topicos_forum():
    aux = topicos_forum.copy()
    for t in aux:
        t['usuario'] = busca_usuario_id(t['codUsuario'])

    return aux


def listagem_demandas(id_usuario=0):
    if id_usuario:
        return [d for d in demandas if d['codUsuario'] == id_usuario]
    else:
        return demandas


def apaga_demanda(id):
    global demandas
    pos = busca_demanda_id(id)[0]
    demandas = demandas[:pos] + demandas[pos+1:]


def notifica_usuarios(nome_tags: list, tipo: str):
    usuarios_envio = set()

    if not nome_tags:
        return

    for t in nome_tags:
        for u in usuarios:
            if t in u['tags']:
                usuarios_envio.add(u['email'])

    if tipo == 'nova demanda':
        assunto = 'Nova demanda cadastrada! ;)'
        corpo = 'Ei, ajuda aí! Uma nova demanda foi cadastrada'\
                + ' com uma de suas tags de interesse!'
    else:
        assunto = 'Nova dúvida cadastrada no fórum! ;)'
        corpo = 'Ei, ajuda aí! Um novo tópico acaba de ser criado'\
                + ' no fórum com um tema de seu interesse!'

    notifica.enviar_emails(assunto, usuarios_envio, corpo)


def salvar_comentario_topico(id_topico, comentario, codUsuario):
    global comentarios
    comentarios.append({
        'id': prox_id_comentario(),
        'texto': comentario,
        'codTopico': id_topico,
        'codUsuario': codUsuario
    })


def info_topico(id_topico):
    topico = busca_topico_id(id_topico)
    topico['usuario'] = busca_usuario_id(topico['codUsuario'])
    topico['comentarios'] = [c for c in comentarios if c['codTopico'] == topico['id']]


    # print(topico['comentarios'])


    for c in topico['comentarios']:
        c['usuario'] = busca_usuario_id(c['codUsuario'])

    return topico


def salvar_topico_forum(titulo, descricao, codUsuario):
    global topicos_forum

    tags = ['#' + tag.strip() for tag in descricao.split('#')[1:]]
    descricao = descricao.split('#')[0]

    notifica_usuarios(tags, 'novo topico')
    topicos_forum.append({
        'id': prox_id_topico(),
        'titulo': titulo,
        'texto': descricao.strip(),
        'tags': tags,
        'codUsuario': codUsuario
    })


def salvar_demanda(titulo, tipo, descricao, tags, codDemanda=0, codUsuario=0):
    global demandas

    lista = [busca_tag_id(int(id)) for id in tags]
    tags = '; '.join(lista)

    if codDemanda:
        pos = busca_demanda_id(id)[0]
        demandas[pos]['descricao'] = descricao
        demandas[pos]['titulo'] = titulo
        demandas[pos]['tipo'] = tipo
        demandas[pos]['tags'] = tags
    else:
        notifica_usuarios(tags.split('; '), 'nova demanda')
        demandas.append({
            'codDemanda': prox_id_demanda(),
            'titulo': titulo,
            'tags': tags,
            'tipo': tipo,
            'descricao': descricao,
            'status': 'Em aberto',
            'codUsuario': codUsuario,
            'associados': [],
            'ajudante': 0
        })

    return True


def avaliacao_usuario(id_usuario, pontos, comentario):
    def pos_usuario(id):
        for i in range(len(usuarios)):
            if usuarios[i]['codUsuario'] == id:
                return i

    usuario = usuarios[pos_usuario(id_usuario)]
    usuario['avaliacao'] = (usuario['avaliacao'] + pontos) / 2
    usuario['ultimo_comentario_recebido'] = comentario
    

def fecha_demanda(id_demanda):
    pos = busca_demanda_id(id_demanda)[0]
    demanda = demandas[pos]
    demanda['status'] = 'Fechada'

    usuarios = [busca_usuario_id(id_usuario) for id_usuario in demanda['associados']]
    usuarios_envio = set([usuario['email'] for usuario in usuarios])
    usuarios_envio.add(busca_usuario_id(demanda['codUsuario'])['email'])

    assunto_email = f"A demanda {demanda['titulo']} foi fechada!"
    corpo_email = f'A demanda "{demanda["titulo"]}", que você participou, foi fechada!'\
                    + " Fique a vontade para avaliar quem te ajudou."\
                    + f'<br><br><a href="http://127.0.0.1:5000/avaliar-monitor/{demanda["ajudante"]}" style="color:#213951; text-decoration:none; border:2px solid #213951; padding:5px 7px; text-align: center; border-radius:5px; width:25%; display: block; margin:auto;">Avaliar</a>'

    notifica.enviar_emails(assunto_email, usuarios_envio, corpo_email)


# fecha_demanda(3)

# def editar_demanda(codDemanda, titulo, tipo, descricao, tags):
#     global demandas

#     demanda = busca_demanda_id(id)
#     salvar_demanda(titulo, tipo, descricao, tags, codDemanda)