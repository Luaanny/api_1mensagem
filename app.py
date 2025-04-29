from flask import Flask, request, jsonify

app = Flask (__name__)

mensagens = [
    {
    "id": 1,
    "conteudo": "baesse vs vicente"
    },
     {
    "id": 2,
    "conteudo": "baesse vs vicente"
    },
     {
    "id": 3,
    "conteudo": "baesse vs vicente"
    }
]

print(f'mensagens: {mensagens}')
for message in mensagens:
    print(message['id'])
@app.route('/mensagens', methods=['POST'])
def criar_mensagens():
    nova_mensagem = request.get_json()
    mensagens.append(nova_mensagem)
    return jsonify({'mensagem': 'Mensagem criada'}), 201

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
