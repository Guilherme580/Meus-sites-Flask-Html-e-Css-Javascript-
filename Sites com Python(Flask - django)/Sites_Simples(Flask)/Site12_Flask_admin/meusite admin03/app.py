from flask import Flask,  render_template, redirect, request
from db import db, Usuario, MeuUsuario 
from flask_admin import Admin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db.init_app(app)

with app.app_context():
    db.create_all()

admin = Admin(app, name="Painel")
admin.add_view(MeuUsuario(Usuario, db.session)) # anote isso

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        
        return render_template("dados_usuario.html", usuario=novo_usuario)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    