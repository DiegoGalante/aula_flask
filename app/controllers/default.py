from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/index")
@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
       return redirect(url_for('login'))

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:
                login_user(user,  remember=form.remember_me.data)
                return redirect(url_for("index"))
        
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


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
    r = User.query.filter_by(username='diego').first()
    print(r)

    #UPDATE
    #r = User.query.filter_by(username='diego').first()
    #print(r)
    #é bem semelhante ao insert.
    #quando trouxer o resultado da query, é só trocar o valor do campo, adicionar na session e dar commit
    #r.name = "Diego Galante"
    #db.session.add(r)
    #db.session.commit()

    #DELETE
    # r = User.query.filter_by(username='diego').first()
    # print(r)
    # db.session.delete(r)
    # db.session.commit()
    return "OK"

