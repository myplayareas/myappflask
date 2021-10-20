from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

banco_de_dados = 'sysrepository.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + banco_de_dados
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from sysrepository import main
