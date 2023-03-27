import math
import notifica
import notifica_gestao
from model import *


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
        chat.append({
            'codDemanda': prox_id_demanda(),
            'mensagens': []
        })
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


def aceita_demanda(cod, usuario):
    
    print(demandas[0])
    
    pos = busca_demanda_id(cod)[0]
    demanda = demandas[pos]
    demanda['status'] = 'Aceita'
    demanda['ajudante'] = usuario
    
    print(demandas[0])

    
def fecha_demanda(id_demanda):
    pos = busca_demanda_id(id_demanda)[0]
    demanda = demandas[pos]
    demanda['status'] = 'Fechada'
    
    if demanda['ajudante'] != 0:
        usuarios = [busca_usuario_id(id_usuario) for id_usuario in demanda['associados']]
        usuarios_envio = set([usuario['email'] for usuario in usuarios])
        usuarios_envio.add(busca_usuario_id(demanda['codUsuario'])['email'])

        assunto_email = f"A demanda {demanda['titulo']} foi fechada!"
        corpo_email = f'A demanda "{demanda["titulo"]}", que você participou, foi fechada!'\
                        + " Fique a vontade para avaliar quem te ajudou."\
                        + f'<br><br><a href="http://127.0.0.1:5000/avaliar-monitor/{demanda["ajudante"]}" style="color:#213951; text-decoration:none; border:2px solid #213951; padding:5px 7px; text-align: center; border-radius:5px; width:25%; display: block; margin:auto;">Avaliar</a>'

        notifica.enviar_emails(assunto_email, usuarios_envio, corpo_email)


def ranqueamento_usuarios():
    aux = usuarios.copy()
    aux = sorted(aux, key=lambda k: k['avaliacao'], reverse=True)
    
    for i in range(len(aux)):
        aux[i]['avaliacao'] = math.floor(aux[i]['avaliacao'])
    return aux, fotos_perfil


def gera_relatorio():

    def calcula_porcentagem(dados_gerais: list):
        resumo = list()
        
        for dado in set(dados_gerais):
            quant_total = len(dados_gerais)
            ocorrencias = dados_gerais.count(dado)
            resumo.append({
                'info': dado,
                'porcentagem': round((ocorrencias / quant_total) * 100, 2)
            })
        
        return resumo
    
    def topicos_maior_interesse():
        tags = list()
        
        for u in usuarios:
            tags += u['tags']
            
        lista = calcula_porcentagem(tags)
        return sorted(lista, key=lambda k: k['porcentagem'], reverse=True)[:3]
    
    def topicos_mais_procurados():
        tags = list()
        
        for d in demandas:
            tags += [tag.strip() for tag in d['tags'].split(';')]
        for t in topicos_forum:
            tags += t['tags']
            
        lista = calcula_porcentagem(tags)
        return sorted(lista, key=lambda k: k['porcentagem'], reverse=True)[:3]
    
    def usuarios_destaque():
        return [u['nome'] for u in ranqueamento_usuarios()[0][:3]]
    
    dados = {
        'maior_interesse': topicos_maior_interesse(),
        'mais_procurados': topicos_mais_procurados(),
        'destaques': usuarios_destaque()
    }
    
    assunto_email = 'Estatísticas do AjudaAí!'
    usuarios_envio = [u['email'] for u in usuarios[:5]] #integrantes do grupo
    notifica_gestao.enviar_emails(assunto_email, usuarios_envio, dados)
    

def pos_chat(id):
    for i in range(len(chat)):
        if chat[i]['codDemanda'] == id:
            return i


def mensagens_chat(cod_demanda):
    conversa = chat[pos_chat(cod_demanda)]
    return conversa['mensagens']


def enviar_mensagem_chat(mensagem, cod_demanda, cod_usuario):
    conversa = chat[pos_chat(cod_demanda)]
    conversa['mensagens'].append({
        'codUsuario': cod_usuario,
        'texto': mensagem
    })
























# def editar_demanda(codDemanda, titulo, tipo, descricao, tags):
#     global demandas

#     demanda = busca_demanda_id(id)
#     salvar_demanda(titulo, tipo, descricao, tags, codDemanda)