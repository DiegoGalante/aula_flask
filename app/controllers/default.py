from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello World"

@app.route("/test", defaults={'name':None})
@app.route("/test/<name>")
def test(name):
    print(type(name))
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuario!"

#@app.route("/teste/<int:id>")
@app.route("/teste/", methods=['GET'])
def teste():
    return "Oi!"
