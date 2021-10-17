from sysrepository import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    repositories = db.relationship('Repositorio', backref='owned_usuario', lazy=True)

class Repositorio(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    link = db.Column(db.String(length=1024), nullable=False, unique=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    analysis_date = db.Column(db.DateTime, nullable=True, default=None)
    analysed = db.Column(db.Integer(), nullable=True, default=0)
    owner = db.Column(db.Integer(), db.ForeignKey('usuario.id'))

class RepositorioUsuarios:
    def insere_usuario(self, usuario):
        db.session.add(usuario)
        db.session.commit()

    def consulta_usuario_por_nome(self, p_username):
        usuario = Usuario.query.filter_by(username=p_username).first()
        return usuario

    def consulta_usuario_por_id(self, p_id):
        usuario = Usuario.query.filter_by(id=p_id).first()
        return usuario
    
    def lista_todos_os_usuarios(self):
        return Usuario.query.all()

class RepositorioRepositorios:
    def insere_repositorio(self, repositorio):
        db.session.add(repositorio)
        db.session.commit()

    def consulta_repositorio_por_nome(self, nome):
        repositorio = Repositorio.query.filter_by(name=nome).first()
        return repositorio

    def consulta_repositorio_por_id(self, p_id):
        repositorio = Repositorio.query.filter_by(id=p_id).first()
        return repositorio
    
    def lista_todos_os_repositorios(self):
        return Repositorio.query.all()

    def consulta_repositorios_por_id_usuario(self, id_usuario):
        lista_reposigorios_usuario = Repositorio.query.filter_by(owner=id_usuario).all()
        return lista_reposigorios_usuario