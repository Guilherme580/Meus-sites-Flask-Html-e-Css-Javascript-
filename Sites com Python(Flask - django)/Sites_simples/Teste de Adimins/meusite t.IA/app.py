from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# cria banco e dados iniciais
conn = sqlite3.connect("data.db")
conn.execute("CREATE TABLE IF NOT EXISTS itens (id INTEGER, label TEXT, valor TEXT)")
if conn.execute("SELECT COUNT(*) FROM itens").fetchone()[0] == 0:
    conn.execute("INSERT INTO itens VALUES (1,'Dia','Sexta')")
    conn.execute("INSERT INTO itens VALUES (2,'Mês','29')")
    conn.execute("INSERT INTO itens VALUES (3,'Bitcoin','57000')")
conn.commit()
conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect("data.db")
    itens = conn.execute("SELECT * FROM itens").fetchall()
    conn.close()
    return render_template("index.html", itens=itens)

@app.route("/admin", methods=["GET","POST"])
def admin():
    conn = sqlite3.connect("data.db")
    if request.method == "POST":
        for id in [1,2,3]:
            v = request.form.get(f"i{id}")
            conn.execute("UPDATE itens SET valor=? WHERE id=?", (v,id))
        conn.commit()
        conn.close()
        return redirect("/")
    itens = conn.execute("SELECT * FROM itens").fetchall()
    conn.close()
    return render_template("admin.html", itens=itens)

app.run(debug=True)