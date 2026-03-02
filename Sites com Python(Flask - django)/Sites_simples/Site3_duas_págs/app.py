from flask import *

app = Flask(__name__)

@app.route("/")
def pagina1():
    return render_template("principal.html")

@app.route("/pagina2")
def pagina2():
    return render_template("secundaria.html")

if __name__ == "__main__":
    app.run(debug=True)