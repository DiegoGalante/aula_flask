from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

db = SQLAlchemy(app)
#instancia o Migrate
#E o migrate cuida das migrações e pra isso ele precisa receber, tanto a aplicação quanto o banco de dados
migrate = Migrate(app, db)

#Manager vai cuidar dos comandos que vou usar na aplicação
#por padrão o primeiro dela sé o runserver que é o comando de execução da aplicação
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
#from app.models import tables