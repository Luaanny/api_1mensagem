from flask import Flask, request, jsonify
from db import db, Mensagem
from http import HTTPStatus

app = Flask (__name__)
app.config['SQLALCHMY_DATABASE_URI'] = 'sqlalchemy://banco_mensagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/mensagens', methods=['POST'])
def criar_mensagens():
    data = request.get_json()
    nova = Mensagem(conteudo=data.get('conteudo'))

    db.session(nova)
    db.session.commit()

    return jsonify(nova .to_dict(), HTTPStatus.CREATED)

@app.route("/mensagens", methods=["GET"])
def ler_mensagens():
    return {"mensagens": mensagens}

@app.route("/mensagens/<int:id>", methods=['PUT'])
def update_mensagens(id):
    data = request.json
    for message in mensagens:
        if message['id'] == id:
            message['conteudo'] = data.get('conteudo')
            return message
    
    return jsonify({'erro': 'id não encontrado'}), 404

@app.route("/mensagens/<int:id>", methods=['DELETE'])
def delete_mensagens(id):
    for message in mensagens:
        if message['id'] == id:
            mensagens.remove(message)
            return message            

    return jsonify({'erro': 'id não encontrado'}), 404

@app.route('/mensagens/<int:id>', methods=['GET'])
def retornar_mensagem(id):
    for message in mensagens:
        if message['id'] == id:
            return message
    
    return jsonify({'mensagem': 'o id não foi encontrado'}), 404


    

 
if __name__ == '__main__':
    app.run(debug=True)
