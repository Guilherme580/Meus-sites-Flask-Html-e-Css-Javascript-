from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from flask_admin import AdminIndexView


db = SQLAlchemy()

class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    
class Protetor_admin(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))
    
