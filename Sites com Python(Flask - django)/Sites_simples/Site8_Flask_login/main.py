from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, login_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash
from objetos import Usuarios, Protetor_admin, db

app = Flask(__name__)
app.config["SECRET_KEY"] = "minha_chave"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco_dados.db"
db.init_app(app)

login = LoginManager(app)
login.login_view = "login"

@login.user_loader
def load_user(user_id):
     return Usuarios.query.get(int(user_id))

admin = Admin(app, index_view=Protetor_admin())
admin.add_view(ModelView(Usuarios, db.session))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
       senha = request.form["password"] 
       usuario = request.form["user"]
       
       user = Usuarios.query.filter_by(nome_usuario=usuario).first()
       if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for("admin.index"))
    
    return """
        <form method="POST">
            <input type="text" name="user" placeholder="Usuário" required>
            <input type="password" name="password" placeholder="Senha" required>
            <button type="submit">Entrar</button>
        </form>
    """

@app.route("/")
def main():
    return "<a href='/admin'>Clique aqui para ir para a rota do admin</a>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Usuarios.query.first():
            novo = Usuarios(
                nome_usuario="guilherme",
                senha=generate_password_hash("123")
            )
            db.session.add(novo)
            db.session.commit()
    app.run(debug=True)
    