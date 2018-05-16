from flask import Flask

app = Flask(__name__)

#importando a página default
#no python3 é necessário colocar o caminho completo do import e não mais o caminnho relativo igual era no python2
from app.controllers import default

