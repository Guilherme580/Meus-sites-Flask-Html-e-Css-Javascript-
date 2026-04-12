from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    resultado = None

    if request.method == "POST":
        v1 = float(request.form["valor1"])
        v2 = float(request.form["valor2"])
        resultado = v1 + v2
        
        
    return render_template("index.html", resul=resultado)
                             
if __name__ == "__main__":
    app.run(debug=True)
