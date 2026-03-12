from flask import Flask, render_template, redirect, url_for, request, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import Bootstrap4Theme
from flask_login import LoginManager, login_required, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Formulario, Proteger_admin, Tarefa, db
from blueprint import bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("chave")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("link")

login_manager = LoginManager(app)
login_manager.login_view = "login"

app.register_blueprint(bp)
db.init_app(app)

with app.app_context():
    db.create_all()

    # cria um admin se não existir nenhum usuário
    if not User.query.first():
        admin = User(
            email=os.getenv("email"),
            nome=os.getenv("nome_admin"),
            senha=generate_password_hash(os.getenv("senha_admin"))
        )

        db.session.add(admin)
        db.session.commit()
 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/registro", methods=["GET", "POST"])
def registro():
    formulario = Formulario()
    if request.method == "POST": 

        usuario = User.query.filter((User.email == formulario.email.data) | (User.nome == formulario.nome.data)).first()

        if usuario is None:
            novo_usuario = User(
                email=formulario.email.data.strip(),
                senha=generate_password_hash(formulario.senha.data.strip()),
                nome=formulario.nome.data.strip()
            )
            db.session.add(novo_usuario)
            db.session.commit()
            
            login_user(novo_usuario) 
            return redirect("/usuario")
        
        return redirect("/registro")
        
    return render_template("registro.html", form=formulario)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip()
        senha = request.form["senha"].strip()
        username = request.form["username"].strip()
           
        usuario = User.query.filter_by(email=email, nome=username).first()
        if usuario is not None  and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for("usuario"))
    
    return render_template("login.html")
        
       

@app.route("/usuario", methods=["GET", "POST"])
@login_required
def usuario():   
    if request.method == "POST":
        dados = request.get_json()  
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        status = dados.get("statusSelecionado")

        nova_tarefa = Tarefa(
            titulo = titulo,
            descricao = descricao,
            status = status,
            usuario_id=current_user.id
        )
        db.session.add(nova_tarefa)
        db.session.commit()
        return {"ok": True}  
    return render_template("usuario.html", dados=current_user)

@app.route("/tarefas_usuario", methods=["GET"])
@login_required
def tarefas_usuario():
    tarefas = Tarefa.query.filter_by(usuario_id=current_user.id).all()
    lista = [{"titulo": t.titulo, "descricao": t.descricao, "status": t.status} for t in tarefas]
    return render_template("tarefas_usuario.html", lista=lista)

tema = Bootstrap4Theme(swatch="darkly")

admin = Admin(app, theme=tema, index_view=Proteger_admin())
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Tarefa, db.session))


if __name__ == "__main__":
    app.run(debug=True)
    