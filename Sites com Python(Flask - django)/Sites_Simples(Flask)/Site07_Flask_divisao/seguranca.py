from flask import Blueprint, render_template , redirect, url_for, request, session
from flask_login import login_user
from dotenv import load_dotenv 
from os import getenv
from usuario import User

load_dotenv()

bp = Blueprint("seguranca", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        senha = request.form["password"]
        if senha == getenv("SENHA"):
            usuario = User.query.first()
            login_user(usuario)
            return redirect("/")
        else:
            return "[ERRO]"
    return render_template("login.html")


@bp.route("/logar", methods=["GET", "POST"])
def logar():
    if request.method == "POST":
        if request.form.get("password") == "123":
            session["logado"] = True # Cria o "carimbo" de acesso
            return redirect(url_for('admin.index'))
        return redirect(url_for('erro'))
    
    return '''
        <form method="post">
            <h2>Senha do Painel:</h2>
            <input type="password" name="password">
            <button type="submit">Entrar</button>
        </form>
    '''
