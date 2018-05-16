#importa o Flask
from flask import Flask

#cria a instancia do flask. 
#toda a aplicação está contida na variavel app.
app = Flask(__name__)

#decorator
#o .Route faz com que defina rotas 
#no caso de "/" é a rota raiz!
@app.route("/")
#é chamada de index por representar a página principal
#mas pode ser cahamdo como quiser
def index():
    return "Hello World";
    pass

if __name__ == "__main__":
    app.run()
    pass