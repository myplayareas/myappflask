from sysrepository import app
from flask import render_template, request, redirect, url_for, flash, session
import datetime
from sysrepository import dao

repositorioUsuarios = dao.RepositorioUsuarios()
repositorioRepositorios = dao.RepositorioRepositorios()

@app.route('/')
def index_page():
    now = datetime.datetime.now()
    return render_template('index.html', mensagens=now)

# Dashboard do usuario logado
@app.route('/home')
def home_page():
    try: 
        usuario_logado = repositorioUsuarios.consulta_usuario_por_id(session['user_id'])
        if usuario_logado is None:
            return redirect(url_for("logout"))

        repositorios_do_usuario = repositorioRepositorios.consulta_repositorios_por_id_usuario(session['user_id'])

        return render_template('home.html', repositorios=repositorios_do_usuario, usuario_logado=usuario_logado)
    except Exception as e:
        print(f'Erro: {e}')
        return redirect(url_for("login_page"))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirma_password = request.form['confirma_password']

        if repositorioUsuarios.consulta_usuario_por_nome(username) is None:
            usuario = dao.Usuario(name=name, username=username, email=email, password=password)
            repositorioUsuarios.insere_usuario(usuario)
            flash(f'Usuario {usuario.username} inserido com sucesso!', category='success')
            return redirect(url_for('login_page'))

        flash('Usuário já existe!', category='danger')

    return render_template('register.html')

def valida_login(username, password):
    usuario = repositorioUsuarios.consulta_usuario_por_nome(username)
    if usuario is None:
        return False
    else: 
        if (usuario.password == password):
            return True
        else: 
            return False

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if valida_login(username, password):        
            usuario = repositorioUsuarios.consulta_usuario_por_nome(username)
            session['user_id'] = usuario.id
            flash(f'Usuário {usuario.username} logado com sucesso!', category='success')
            print(f'Name: {usuario.name}, Username: {usuario.username}, logou as: {datetime.datetime.now()}')
            return redirect(url_for('home_page'))
        # se as informacoes forem invalidas devolve mensagem de erro.
        flash('Usuário ou senha inválida!', category='danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    usuario = repositorioUsuarios.consulta_usuario_por_id(session['user_id'])
    if usuario is not None: 
        if session is not None:
            session.clear()
            flash(f'Usuário {usuario.username} deslogado com sucesso!', category='success')

    return redirect(url_for('login_page'))

def repositorio_ja_existe(name, link, lista):
    checa = False
    if len(lista) > 0:
        for each in lista:
            if each.name == name or each.link == link:
                checa = True
    return checa

@app.route('/repository', methods=['GET', 'POST'])
def repository_page():
    if request.method == 'POST':
        name = request.form['name']
        link = request.form['link']

        lista_repositorios_do_usuario = repositorioRepositorios.consulta_repositorios_por_id_usuario(session['user_id'])
        # se o repositorio ainda não existe na lista de repositorios do usuario logado insere na lista de repositorios do usuario logado
        if not repositorio_ja_existe(name, link, lista_repositorios_do_usuario):
            repositorio = dao.Repositorio(name=name, link=link, creation_date=datetime.datetime.now(), 
                                            analysis_date=None, analysed=0, owner=session['user_id'])
            
            repositorioRepositorios.insere_repositorio(repositorio)

            flash(f'Repositório {repositorio.name} inserido com sucesso!', category='success')

            return redirect(url_for('home_page'))

        flash('Repositório já existe!', category='danger')

    return render_template('repository.html')