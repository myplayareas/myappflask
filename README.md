# myappflask
Aplicação Flask de exemplo

Aplicação flask exemplo 1

1. Esta aplicação de exemplo deverá ter seguintes funcionalidades.

1.1 A aplicação deve exibir uma tela pública com as opções de registro e login de usuário.

1.2 A aplicação deve salvar os usuários registrados.

1.3 A aplicação deverá exibir um formulário de registro para registrar novos usuários.

1.4 A aplicação deverá exbir um formulário de login para o login dos usuários.

1.5 Cada usuário poderá cadastrar seus próprios repositórios.

1.6 O usário logado poderá visualizar uma lista de todos os seus repositórios cadastrados.

2. Estrutura da aplicação 

```bash
.
├── README.md
├── run.py (6)
├── setvariables.sh (4)
└── sysrepository
    ├── __init__.py (1)
    ├── dao.py (3)
    ├── main.py (2)
    ├── sysrepository.db
    └── templates (5)
        ├── home.html
        ├── index.html
        ├── login.html
        ├── register.html
        └── repository.html
```

(1) Responsável por definir a estrutura de pacotes da aplicação

(2) Responsável pelas rotas para cada uma das views 

(3) Módulo que contem as classes Usuario, Repositorio, RepositorioUsuarios e RepositorioRepositorios

(4) Script bash que configura as variáveis de ambiente FLASK_APP e FLASK_ENV

(5) Diretório que contem as views (.html) da aplicação, neste caso os arquivos html carregam o jQuery e o Bootstrap via CDN (Content delivery network)

(6) Responsável por inicializar a aplicação (app)

3. Módulos usados nesta aplicação

Os seguintes módulos são usados para auxiliar o gerenciamento das chamadas das rotas, devolução de suas respostas e controle de sessão do usuário: 
[render_template](https://flask.palletsprojects.com/en/2.0.x/api/#flask.render_template), [request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.request), 
[redirect](https://flask.palletsprojects.com/en/2.0.x/api/#flask.redirect), [url_for](https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for), 
[flash](https://flask.palletsprojects.com/en/2.0.x/patterns/flashing), [session](https://flask.palletsprojects.com/en/2.0.x/api/#flask.session) e [flask_sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

Mais detalhes no [wiki](https://github.com/myplayareas/myappflask/wiki)
