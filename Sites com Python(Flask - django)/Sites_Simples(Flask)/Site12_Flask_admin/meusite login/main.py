# serve para importar as blibliotecas 
# necessarias para criar um sistema de login
from flask import Flask, request, redirect, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required

# criar app e chave secreta
app = Flask(__name__)
app.secret_key = "x"

login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin):
    id = "1"

@login_manager.user_loader
def load_user(uid):
    return User()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        senha = request.form["password"]
        if senha == "123":
            login_user(User())
            return redirect("/index")
        else:
            return redirect("/erro")
    return """
<form action="/login" method="POST">
    <input type="password" name="password">
    <button type="submit">Entrar</button>
</form>
"""

@app.route("/index")
@login_required
def index():
    return render_template("main.html")
    
@app.route("/erro")
def erro():
    return render_template("erro.html")

app.run(debug=True)
