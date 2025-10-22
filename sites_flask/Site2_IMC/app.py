from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculo_imc():
    resposta = None

    if request.method == "POST":
        p_str = request.form["peso"]
        a_str = request.form["altura"]
        
        p = float(p_str.replace(",", "."))
        a = float(a_str.replace(",", "."))
        imc = p/(a ** 2)
        if imc < 18.5:
            resposta = f"Seu imc está abaixo do peso imc:{imc:.2f}"
        elif imc >= 18.5 and imc <= 24.9:
            resposta = f"Seu imc está estavel imc:{imc:.2f}"
        elif imc >= 25 and imc <= 29.9:
            resposta = f"Seu imc está muito altu imc:{imc:.2f}"
        elif imc >= 30:
            resposta = f"Seu imc indica que você está OBESO imc:{imc:.2f}"
            
    return render_template("index.html", resultado=resposta)


if __name__ == "__main__":
    app.run(debug=True)
    