from flask import *
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def cadastro():
    nome = idade = situacao = None
    if request.method == "POST":
        nome = request.form["nome"]
        aniversario = request.form["aniversario"]
        situacao = request.form["situacao"]
        
        parte = aniversario.split("/")
        ano_ani = int(parte[2])
        ano_atual = date.today().year
        idade = ano_atual - ano_ani
        if nome is not None:
            return render_template("sucesso.html", nome=nome, idade=idade, situacao=situacao)
        else:
            return render_template("cadastro.html")
        
    return render_template("cadastro.html")

@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")


if __name__ == "__main__":
    app.run(debug=True)
