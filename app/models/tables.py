#da pasta app, importa o db
from app import db


#db.Model é uma classe do sqlalchemy padrão
#a User herda a db.Model
class User(db.Model)
    __tablename__ = "users"
    #unique significa que não pode existir outro usuario com o mesmo nome
    #tipo um só e-mail na base de dados, etc
    #db.String é possível passar o tamanho da string, assim db.String[120], se deixar sem tamanho, vai ser atribuido o tamanho maximo permitido praquele banco
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    #construtor
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    #significa representação.
    #é o jeito que a classe vai aparecer quando fizer uma pesquisa no banco de dados
    def __repr__(self):
        return "<User %r>" % self.username
        

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #poderia ser qualquer nome, ao invés de 'user'
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)