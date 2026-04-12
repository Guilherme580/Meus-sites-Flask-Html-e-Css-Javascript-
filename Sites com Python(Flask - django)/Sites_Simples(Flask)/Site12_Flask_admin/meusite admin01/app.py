from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db = SQLAlchemy(app)


# Modelo que guarda o texto da 
class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200))
 
# Criar banco e mensagem inicial
with app.app_context():
    db.create_all()
    if not Mensagem.query.first():
        db.session.add(Mensagem(texto='Olá Mundo'))
        db.session.commit()

# Painel Flask-Admin
admin = Admin(app, name='Painel') # Removed template_mode
admin.add_view(ModelView(Mensagem, db.session))

# Página principal que usa render_template
@app.route('/')
def index():
    frase = Mensagem.query.first().texto
    return render_template('index.html', frase=frase)

app.run(debug=True)