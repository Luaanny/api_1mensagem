from flask import Flask, request, jsonify

app = Flask (__name__)

mensagens = []

@app.route('/mensagens', methods=['POST'])
def criar_mensagens():
    nova_mensagem = request.get_json()
    mensagens.append(nova_mensagem)
    return jsonify ({'mensagem': 'Mensagem criada'}), 201



 
if __name__ == '__main__':
    app.run(debug=True)
