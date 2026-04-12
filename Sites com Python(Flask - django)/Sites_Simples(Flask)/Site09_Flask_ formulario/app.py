from flask import Flask, render_template, request

 # -------
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"


db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    
 # -------
class LoginForm(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    botao = SubmitField("Enviar")

adnin = Admin(app)
adnin.add_view(ModelView(Users, db.session))
    
with app.app_context():
    db.create_all()

 # -------
@app.route("/", methods=["GET", "POST"])
def main():
    formulario = LoginForm()
    if formulario.validate_on_submit(): 
        novo = Users(
            nome = formulario.nome.data
        )
        db.session.add(novo)
        db.session.commit()
        
        return f"Sucesso! {formulario.nome.data} salvo no banco."

    return render_template("index.html", form=formulario)
    


app.run(debug=True)
