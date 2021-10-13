# myappflask
Aplicação Flask de exemplo

Aplicação flask exemplo 1

1. Esta aplicação de exemplo deverá ter seguintes funcionalidades.

1.1 A aplicação deve exibir uma tela pública com as opções de registro e login de usuário.

1.2 A aplicação deve salvar os usuários registrados em uma lista em tempo de memória enquanto a aplicação estiver rodando.

1.3 A aplicação deverá exibir um formulário de registro para registrar novos usuários.

1.4 A aplicação deverá exbir um formulário de login para o login dos usuários.

1.5 Cada usuário poderá cadastrar seus próprios repositórios.

1.6 O usário logado poderá visualizar uma lista de todos os seus repositórios cadastrados.

2. Estrutura da aplicação 

```bash
├── __init__.py (1)
├── main.py (2)
├── dao.py (3)	
├── setvariables.sh (4)
└── templates (5)
    ├── home.html
    ├── index.html
    ├── login.html
    ├── register.html
    └── repository.html
```

(1) Responsável por definir a estrutura de pacotes da aplicação

(2) Responsável por inicializar a aplicação (app), o repositório de usuários e as rotas para cada uma das views 

(3) Módulo que contem as classes Usuario e RepositorioUsuarios

(4) Script bash que configura as variáveis de ambiente FLASK_APP e FLASK_ENV

(5) Diretório que contem as views (.html) da aplicação, neste caso os arquivos html carregam o jQuery e o Bootstrap via CDN (Content delivery network)

3. Módulos usados nesta aplicação

Os seguintes módulos são usados para auxiliar o gerenciamento das chamadas das rotas, devolução de suas respostas e controle de sessão do usuário: 
[render_template](https://flask.palletsprojects.com/en/2.0.x/api/#flask.render_template), [request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.request), 
[redirect](https://flask.palletsprojects.com/en/2.0.x/api/#flask.redirect), [url_for](https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for), 
[flash](https://flask.palletsprojects.com/en/2.0.x/patterns/flashing) e [session](https://flask.palletsprojects.com/en/2.0.x/api/#flask.session)

Mais detalhes no [wiki](https://github.com/myplayareas/myappflask/wiki)
