from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    
with app.app_context():
    db.create_all()
    if not Cliente.query.first():
        cliente = Cliente(
        nome = "carlos",
        telefone = "85 9 9956-2432",
        email = "camillog461@gmail.com")
        db.session.add(cliente)
        db.session.commit()
        
admin = Admin(app, name="Painel")     
admin.add_view(ModelView(Cliente, db.session))
 
 
@app.route("/")
def clientes():
    clientes = Cliente.query.all()
    return render_template("index.html", clientes=clientes)

if __name__ == "__main__":
    app.run(debug=True)
    
    