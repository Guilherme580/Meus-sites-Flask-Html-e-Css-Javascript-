from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.DataFrame({
        "idade":[18, 19, 20, 21, 22, 23, 24],
        "grupo":["A", "A", "B", "B", "A", "B", "A"]
    })

    fig = px.histogram(
        df,
        x='idade',
        color="grupo",
        title="Distribuição de Idades."
    )
    
    grafico_html = fig.to_html(full_html=False)
    tabela_html = df.to_html()
    
    return render_template("index.html", grafico=grafico_html, tabela=tabela_html)

app.run(debug=True)
