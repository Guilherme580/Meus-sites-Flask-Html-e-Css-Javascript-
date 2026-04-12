from flask import Flask, render_template, redirect, url_for, session, request
from flask_admin import Admin, AdminIndexView, expose
from flask_login import LoginManager, login_required
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
from os import getenv
from usuario import User, Proteger_Admin, db
from seguranca import bp

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("PRIMARY_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db.init_app(app)
login = LoginManager(app)
login.login_view = "seguranca.login"

with app.app_context():
    db.create_all()
    if not User.query.first():
        db.session.add(User(msg='Olá, Mundo!'))
        db.session.commit()

app.register_blueprint(bp)
admin = Admin(app, name="Mensagem_Teste", index_view=Proteger_Admin())
admin.add_view(ModelView(User, db.session))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
@login_required
def mensagem():
    msg = User.query.first()
    return render_template("mensagem.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
