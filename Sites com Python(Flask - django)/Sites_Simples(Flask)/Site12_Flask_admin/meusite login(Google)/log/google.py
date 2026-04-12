from flask import Flask, redirect, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config["SECRET_KEY"] = "x"

auto = OAuth(app) #autorização 

google = auto.register(
    name="google",
    cliente_id="SEU_ID",
    cliente_secret="SEU_SECRET",
    cliente_kwargs={"scope": "openid email"}
)

@app.route("/")
def