from flask import Flask, request, redirect, render_template, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = "x"

login = LoginManager(app)
login.login_view = "login"

class User(UserMixin):
    id = "1"

@login.user_loader
def load_user(uid):
    return User()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        senha = request.form["password"]
        if senha == "senhamestre":
            login_user(User())
            return redirect("/painel")
        else:
            return redirect("/erro")  
            
    return """
<form action="/login" method="POST">
    <input type="password" name="password">
    <button type="submit">Entrar</button>
</form>
"""

@app.route("/painel")
@login_required
def painel():
    return """<h1>Acesso Liberado</h1>"""

@app.route("/erro")
def erro():
    return """
<h1>Senha Incorreta</h1>
<form action="/login">
    <button type="submit">Voltar</button>
</form>
"""

app.run(debug=True)
