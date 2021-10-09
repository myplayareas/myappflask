class Usuario: 
    def __init__(self, id, username, name, email, password):
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        self.password = password

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