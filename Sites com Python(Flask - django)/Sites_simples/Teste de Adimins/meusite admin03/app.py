from flask import Flask,  render_template, redirect
from db import db 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
    