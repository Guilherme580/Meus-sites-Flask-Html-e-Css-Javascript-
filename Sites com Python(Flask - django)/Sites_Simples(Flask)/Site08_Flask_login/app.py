from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "chave_secreta"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = "login"

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100))
    senha = db.Column(db.String(100))

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(100))
        


@login.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Protetor_admin(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))

    
    
admin = Admin(app, index_view=Protetor_admin())
admin.add_view(ModelView(Usuario, db.session))
admin.add_view(ModelView(Mensagem, db.session))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = Usuario.query.filter_by(nome_usuario=username).first()
        if user and check_password_hash(user.senha, password) :   
            login_user(user)
            return redirect(url_for('admin.index'))
        
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Usuário" required>
            <input type="password" name="password" placeholder="Senha" required>
            <button type="submit">Entrar</button>
        </form>
    '''
    
with app.app_context():
    db.create_all()
    if not Usuario.query.first():
        novo_usuario = Usuario(
            nome_usuario="gui",
            senha=generate_password_hash("123")
            )
        db.session.add(novo_usuario)
        db.session.commit()    

if __name__ == "__main__":
    app.run(debug=True)
