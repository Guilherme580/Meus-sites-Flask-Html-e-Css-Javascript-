from flask import redirect, session
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import AdminIndexView, expose

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(100))



class Proteger_Admin(AdminIndexView):
    @expose("/")
    def index(self):
        if not session.get("logado"):
            return redirect("/logar")
        return super(Proteger_Admin, self).index()
