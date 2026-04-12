from flask_sqlalchemy import SQLAlchemy 
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
class MeuUsuario(ModelView): # isso é para personalizar a interface do admin
    column_searchable_list = ['nome', 'email']
    