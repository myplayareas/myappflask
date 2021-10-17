from sysrepository import app, forms
from flask import render_template, request, redirect, url_for, flash, session
import datetime
from sysrepository import dao
from sysrepository import forms
from flask_login import login_user, logout_user, login_required, current_user

repositorioUsuarios = dao.RepositorioUsuarios()
repositorioRepositorios = dao.RepositorioRepositorios()

@app.route('/')
def index_page():
    now = datetime.datetime.now()
    return render_template('index.html', mensagens=now)

# Dashboard do usuario logado
@app.route('/home')
@login_required
def home_page():
    try: 
        repositorios_do_usuario = repositorioRepositorios.consulta_repositorios_por_id_usuario(current_user.get_id())
        return render_template('home.html', repositorios=repositorios_do_usuario)
    except Exception as e:
        print(f'Erro: {e}')
        return redirect(url_for("login_page"))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = forms.RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirma_password = form.confirma_password.data

        if repositorioUsuarios.consulta_usuario_por_nome(username) is None:
            usuario = dao.Usuario(name=name, username=username, email=email, password=password)
            repositorioUsuarios.insere_usuario(usuario)
            flash(f'Usuario {usuario.username} inserido com sucesso!', category='success')
            return redirect(url_for('login_page'))
        flash(f'Usuário {username} já existe!', category='danger')
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

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
    form = forms.LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if valida_login(username, password):        
            usuario = repositorioUsuarios.consulta_usuario_por_nome(username)
            login_user(usuario)
            flash(f'Usuário {usuario.username} logado com sucesso!', category='success')
            print(f'Name: {usuario.name}, Username: {usuario.username}, logou as: {datetime.datetime.now()}')
            return redirect(url_for('home_page'))
        # se as informacoes forem invalidas devolve mensagem de erro.
        flash('Usuário ou senha inválida!', category='danger')

    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with user login: {err_msg}', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f'Usuário deslogado com sucesso!', category='success')

    return redirect(url_for('login_page'))

def repositorio_ja_existe(name, link, lista):
    checa = False
    if len(lista) > 0:
        for each in lista:
            if each.name == name or each.link == link:
                checa = True
    return checa

@app.route('/repository', methods=['GET', 'POST'])
@login_required
def repository_page():
    form = forms.RepositoryForm()

    if form.validate_on_submit():
        name = form.name.data
        link = form.link.data

        lista_repositorios_do_usuario = repositorioRepositorios.consulta_repositorios_por_id_usuario(current_user.get_id())
        # se o repositorio ainda não existe na lista de repositorios do usuario logado insere na lista de repositorios do usuario logado
        if not repositorio_ja_existe(name, link, lista_repositorios_do_usuario):
            repositorio = dao.Repositorio(name=name, link=link, creation_date=datetime.datetime.now(), 
                                            analysis_date=None, analysed=0, owner=current_user.get_id())
            repositorioRepositorios.insere_repositorio(repositorio)
            flash(f'Repositório {repositorio.name} inserido com sucesso!', category='success')

            return redirect(url_for('home_page'))

        flash('Repositório já existe!', category='danger')

    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with new repository: {err_msg}', category='danger')

    return render_template('repository.html', form=form)