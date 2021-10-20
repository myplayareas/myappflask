from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

banco_de_dados = 'sysrepository.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + banco_de_dados
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

db = SQLAlchemy(app)

from sysrepository import main
