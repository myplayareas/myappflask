from sysrepository import app
from sysrepository import db, banco_de_dados
from sysrepository.dao import Usuario, Repositorio

CRIA_BANCO_VAZIO = False

try:
    if CRIA_BANCO_VAZIO:
        # Cria um banco vazio
        db.drop_all()
        db.create_all()
        print(f'Banco {banco_de_dados} criado com sucesso!')
except Exception as e:
    print(f'Erro ao criar o Banco {banco_de_dados} - {e}')

if __name__ == '__main__':
    app.run(debug=True)