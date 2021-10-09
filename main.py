from flask import Flask
from flask import render_template, request, url_for, redirect, flash, session

import datetime
from . import dao

app = Flask(__name__)
app.secret_key = "chavedaminhaaplicacao"

repositorioUsuarios = dao.RepositorioUsuarios([])

@app.route('/')
def index_page():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%y %H:%M:%S")
    my_content = f'Hora do sevidor {now}'

    return render_template('index.html', my_message=my_content)

@app.route('/home')
def home_page():
    if session['user_id'] is None:
        return redirect(url_for("login_page"))

    usuario_logado = repositorioUsuarios.consulta_usuario_por_id(session["user_id"])
    
    return render_template('home.html', usuarios=repositorioUsuarios.lista_todos_os_usuarios(), usuario_logado=usuario_logado)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirma_password = request.form["confirma_password"]
        name = request.form["name"]
        email = request.form["email"]

        id_usuario = len(repositorioUsuarios.lista_todos_os_usuarios()) + 1
        usuario = dao.Usuario(id=id_usuario, username=username, name=name, email=email, password=password)

        # Checa se o usuário já existe no sistema, caso não exista cria um novo usário
        # se o usuário não existe insere na lista e redireciona para a página de login
        if (repositorioUsuarios.consulta_usuario_por_nome(username) is None):  
            repositorioUsuarios.insere_usuario(usuario)      
            return redirect(url_for("login_page"))
        else:
            flash(f"User {username} is already registered.")
        
    return render_template("register.html")

def valida_login(username, password):
    usuario = repositorioUsuarios.consulta_usuario_por_nome(username)
    if usuario is None:
        return False
    else:
        if (usuario.password == password):
            return True

    return False

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if valida_login(username, password):
            usuario = repositorioUsuarios.consulta_usuario_por_nome(username)
            session["user_id"] = usuario.id
            # carrega a página principal da aplicacao
            return redirect(url_for('home_page'))
        else:
            flash('Invalid username/password')

    return render_template('login.html')

@app.route('/logout')
def logout_page():
    if session is not None:
        session.clear()
    return redirect(url_for("login_page"))