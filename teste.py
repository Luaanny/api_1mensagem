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

for mensagem in mensagens:
    if mensagem['id'] == 3:
       mensagens.remove(mensagem)
