from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import Bootstrap4Theme

admin_theme = Bootstrap4Theme(swatch="superhero")

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db = SQLAlchemy(app)

class Proteger_admin(AdminIndexView):
    @expose("/")
    def index(self):
        if not session.get("logado"):
            return redirect("/login")
        return super(Proteger_admin, self).index()    
    
class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.String(100))
    servico = db.Column(db.String(50))
    dia = db.Column(db.String(50))
    horario = db.Column(db.String(50))
    status = db.Column(db.String(50))

    
admin = Admin(app, name="Painel de Agendamento", theme=admin_theme, index_view=Proteger_admin())
admin.add_view(ModelView(Agendamento, db.session))

@app.route("/")
def formulario(): 
    return render_template("formulario.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        senha = request.form["password"]
        if senha == "123":
            session["logado"] = True
            return redirect(url_for('admin.index'))
        else:
            return """
                  <style>
                        div{
                            text-align: center;
                            margin: auto;
                        }
                  </style>
                  <div>
                      <h1>Senha Errada!</h1>
                      <a href="/login"><button>Tente novamente</button></a>
                  </div>"""
    else:
        return"""
        <style>
            form{
                text-align: center;
                margin: auto;
            }
        </style>
        <form action="/login" method="POST">
            <h2>Senha do Painel:</h2>
            <input type="password" name="password">
            <button type="submit">Entrar</button>
        </form>
    """

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    db.create_all()
    novo = Agendamento(
        nome = request.form["nome"],
        idade = request.form["idade"],
        servico = request.form["servico"],
        dia = request.form["dia"],
        horario = request.form["horario"],
        status = "Em Análise"
    )
    db.session.add(novo)
    db.session.commit()
    
    return redirect(f"/status/{novo.id}")

@app.route("/status/<int:id>")
def status(id):
    # pessoa = Agendamento.query.get(id)
    pessoa = db.session.get(Agendamento, id)
    return render_template("status.html", pessoa=pessoa)
    
if __name__ == "__main__":
    app.run(debug=True)
    