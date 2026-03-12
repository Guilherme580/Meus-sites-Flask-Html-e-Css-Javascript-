from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import  EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_admin import AdminIndexView
from flask_login import UserMixin, current_user

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    tarefas = db.relationship("Tarefa", backref="usuario", lazy=True)
    

class Formulario(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired()])
    senha = PasswordField("Senha: ", validators=[DataRequired()])
    nome = StringField("Nome: ", validators=[DataRequired()])
    botao = SubmitField("ENVIAR")
    

class Proteger_admin(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("seguranca.login_admin"))
    
    
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    descricao = db.Column(db.Text)
    status = db.Column(db.String(20))
    usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"))
