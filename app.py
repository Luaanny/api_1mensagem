from flask import Flask, request, jsonify
from db import db, Mensagem
from http import HTTPStatus

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'hello world'

@app.route('/mensagens',  methods=['POST'])
def criar_mensagens():
    data = request.get_json()
    nova = Mensagem(conteudo=data.get('conteudo'))

    db.session.add(nova)
    db.session.commit()

    return jsonify(nova.to_dict()), HTTPStatus.CREATED

@app.route("/mensagens", methods=["GET"])
def ler_mensagens():
    mensagens = Mensagem.query.all()
    return jsonify([m.to_dict() for m in mensagens])

@app.route("/mensagens/<int:id>", methods=['PUT'])
def update_mensagem(id):
    data = request.get_json()
    mensagem = Mensagem.query.get(id)

    if mensagem:
        mensagem.conteudo = data.get('conteudo', mensagem.conteudo)
        db.session.commit()
        return jsonify(mensagem.to_dict()), HTTPStatus.OK
    
    return jsonify({'erro': 'id não encontrado'}), HTTPStatus.NOT_FOUND

@app.route("/mensagens/<int:id>", methods=['DELETE'])
def delete_mensagens(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        db.session.delete(mensagem)
        db.session.commit()
        return jsonify(mensagem.to_dict()), HTTPStatus.OK        

    return jsonify({'erro': 'id não encontrado'}), HTTPStatus.NOT_FOUND

@app.route('/mensagens/<int:id>', methods=['GET'])
def retornar_mensagem(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
            return jsonify(mensagem.to_dict()), HTTPStatus.OK
    
    return jsonify({'mensagem': 'o id não foi encontrado'}), HTTPStatus.NOT_FOUND



if __name__ == '__main__':
    app.run(debug=True)
