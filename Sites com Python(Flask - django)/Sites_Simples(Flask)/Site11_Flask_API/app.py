from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:usuario_id>', methods=['GET'])
def obter_usuario(usuario_id):
    banco_de_dados = {
        1: {"nome": "Joao", "idade": 30},
        2: {"nome": "Maria", "idade": 25},
    }
    
    usuatio = banco_de_dados.get(usuario_id)
    if usuatio:
        return jsonify(usuatio)
    else:
        return jsonify({"message": "Nenhum usuário encontrado"}), 404
    
    
if __name__ == '__main__':
    app.run(debug=True)
