#Vai receber um arquivo html e vai renderizá-lo
from flask import render_template
from app import app

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
    
