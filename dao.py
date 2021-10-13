class Usuario:
    repositorios = []
    def __init__(self, id, name, username, email, password):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def set_repositorios(self, repositorios):
        self.repositorios = repositorios

class Repositorio:
    def __init__(self, id, name, link, creation_date, analysis_date, analysed, user_id):
        self.id = id
        self.name = name
        self.link = link
        self.creation_date = creation_date
        self.analysis_date = analysis_date
        self.analysed = analysed
        self.user_id = user_id

class RepositorioUsuarios:
    def __init__(self, lista):
        self.lista = lista

    def insere_usuario(self, usuario):
        self.lista.append(usuario)

    def consulta_usuario_por_nome(self, username):
        usuario = None
        for each in self.lista:
            if each.username == username:
                usuario = each
                break
        return usuario

    def consulta_usuario_por_id(self, id):
        usuario = None
        for each in self.lista:
            if each.id == id:
                usuario = each
                break
        return usuario
    
    def lista_todos_os_usuarios(self):
        return self.lista

class RepositorioRepositorios:
    def __init__(self, lista):
        self.lista = lista

    def insere_repositorio(self, repositorio):
        self.lista.append(repositorio)

    def consulta_repositorio_por_nome(self, nome):
        repositorio = None
        for each in self.lista:
            if each.nome == nome:
                repositorio = each
                break
        return repositorio

    def consulta_repositorio_por_id(self, id):
        repositorio = None
        for each in self.lista:
            if each.id == id:
                repositorio = each
                break
        return repositorio
    
    def lista_todos_os_repositorios(self):
        return self.lista

    def consulta_repositorios_por_id_usuario(self, id_usuario):
        lista_reposigorios_usuario = []
        for each in self.lista:
            if each.user_id == id_usuario:
                lista_reposigorios_usuario.append(each)
        return lista_reposigorios_usuario