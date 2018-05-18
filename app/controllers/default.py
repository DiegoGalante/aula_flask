#Vai receber um arquivo html e vai renderizá-lo
from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.remember_me.data)
        pass
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route("/teste", defaults={"info": None})
@app.route("/teste/<info>")
def teste(info):
    #INSERT
    #i = User("diego", "1234", "Diego Galante", "email@teste.com");
    #db.session.add(i)
    #db.session.commit()

    #SELECT
    #.all()
    #.first()
    ## olhar a documentação para ver os demais tipos de query
    #r = User.query.filter_by(username='diego').first()
    #print(r)

    #UPDATE
    #r = User.query.filter_by(username='diego').first()
    #print(r)
    #é bem semelhante ao insert.
    #quando trouxer o resultado da query, é só trocar o valor do campo, adicionar na session e dar commit
    #r.name = "Diego Galante"
    #db.session.add(r)
    #db.session.commit()

    #DELETE
    r = User.query.filter_by(username='diego').first()
    print(r)
    db.session.delete(r)
    db.session.commit()
    return "OK"

