from flask import Blueprint, url_for

# você cria as rotas blueprint com ("NOME", __name__)
app_bp = Blueprint("site", __name__)

# o sistema de rotas funciona igual ao Flask
@app_bp.route("/blueprint_01")
def simples():
    link_voltar = url_for('main') 
    return f'Olá, essa é uma rota blueprint!</h1>Você está em uma rota <a href="{link_voltar}">BLUEPRINT</a>'
