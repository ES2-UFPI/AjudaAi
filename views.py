import facade
from flask import *
from aplicacao import aplicacao

usuario_padrao = 1
visualizar_lista = 0

def login_usuario(url_seguinte):
    return redirect(url_for('login', proxima_pagina=url_for(url_seguinte)))


@aplicacao.route('/')
def index():
    return render_template('index.html')


@aplicacao.route('/nova_demanda')
def nova_demanda():
#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
#         return login_usuario('nova_demanda')
    return render_template('nova_demanda.html', tags=facade.listagem_tags())


@aplicacao.route('/criar_demanda', methods=['GET', 'POST'])
def criar_demanda():
    tags = list()
    titulo = request.form['titulo']
    tipo = request.form['tipo-demanda']
    descricao = request.form['descricao-demanda']

    for i in range(4):
        tag_id = request.form[f'select_tag{i}']
        if tag_id:
            tags.append(tag_id)

    facade.salvar_demanda(titulo, tipo, descricao, tags, codUsuario=usuario_padrao)
    flash('Demanda criada com sucesso!', category='success')
    return redirect(url_for('index'))


@aplicacao.route('/novo_topico')
def novo_topico():
	#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
	#         return login_usuario('nova_demanda')
    return render_template('CadastrarDuvida.html')


@aplicacao.route('/criar_topico', methods=['GET', 'POST'])
def criar_topico():
	titulo = request.form['titulo']
	descricao = request.form['descricao-pergunta']
	facade.salvar_topico_forum(titulo, descricao, usuario_padrao)
	return redirect(url_for('forum'))


@aplicacao.route('/comentar', methods=['GET', 'POST'])
def comentar():
	id_topico = request.form['id_topico']
	comentario = request.form['comentario']

	# print(id_topico, comentario)

	facade.salvar_comentario_topico(id_topico, comentario, usuario_padrao)
	return redirect(url_for('forum'))


@aplicacao.route('/forum')
def forum():
 	return render_template('Forum.html', topicos=facade.listagem_topicos_forum())


@aplicacao.route('/lista_demandas')
def lista_demandas():
    global visualizar_lista
    visualizar_lista = 1
    return render_template('lista_demandas.html', demandas=facade.listagem_demandas())


@aplicacao.route('/minhas_demandas')
def minhas_demandas():
    global visualizar_lista
    visualizar_lista = 0

#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
#         return login_usuario('nova_demanda')
    return render_template('minhas_demandas.html', demandas=facade.listagem_demandas(1))


@aplicacao.route('/retorna_lista')
def retorna_lista():
    global visualizar_lista
    if visualizar_lista: # lista geral
        return redirect(url_for('lista_demandas'))
    else:
        return redirect(url_for('minhas_demandas'))


@aplicacao.route('/visualizar_topico/<int:id_topico>')
def visualizar_topico(id_topico):
    return render_template('topicoForum.html', topico=facade.info_topico(id_topico))


@aplicacao.route('/visualizar_demanda/<int:cod>')
def visualizar_demanda(cod):
    demanda = facade.busca_demanda_id(cod)[1]
    return render_template('visualizar_demanda.html', demanda=demanda)


@aplicacao.route('/apagar_demanda/<int:cod>')
def apagar_demanda(cod):
    demanda = facade.apaga_demanda(cod)
    return redirect(url_for('retorna_lista'))


@aplicacao.route('/login')
def login():
    proxima = request.args.get('proxima_pagina')
    return render_template('login.html', proxima=proxima)


@aplicacao.route('/autenticar', methods=['POST'])
def autenticar():
    # busca o usuario no banco
    
#     usuario = usuario_dao.buscar_por_id(request.form['usuario'])

    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(f'Bem vindo, {usuario.nome}!', category='success')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Senha incorreta, tente novamente!', category='danger')
            return redirect(url_for('login'))
    else:
        flash('Usuário não cadastrado!', category='danger')
        return redirect(url_for('login'))


@aplicacao.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Até mais! ;)', category='info')
    return redirect(url_for('index'))


@aplicacao.route('/entrar')
def entrar():
    flash('Em breve será necessário efetuar o login. Por enquanto, fique a vontade!', category='info')
    return redirect(url_for('index'))


@aplicacao.route('/sobre')
def sobre():
    flash('Em breve!', category='info')
    return redirect(url_for('index'))


@aplicacao.route('/contato')
def contato():
    flash('Em breve!', category='info')
    return redirect(url_for('index'))