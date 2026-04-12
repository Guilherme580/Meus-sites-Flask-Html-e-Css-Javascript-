from flask import Flask, url_for
from blueprint import app_bp

app = Flask(__name__)
app.register_blueprint(app_bp)

@app.route("/")
def main():
    link = url_for("site.simples")
    return f'Essa é uma rota <a href="{link}">FLASK</a>'


app.run(debug=True)
