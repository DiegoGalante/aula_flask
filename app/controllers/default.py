#Vai receber um arquivo html e vai renderizá-lo
from flask import render_template
from app import app

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('base.html')
    