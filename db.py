from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declative_base

db = create_engine("sqlalchemy://banco_mensagens.db")
Session = sessionmaker(bind=db)
Session = Session()

Modelo = declative_base()

#tabelas
class mensagem(Modelo):
    id = Column("id", Integer, primary_key= True)
    conteudo = Column("conteudo", String)
