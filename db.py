from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Mensagens(db.Model):
    __tablename__ = 'mensagens'
    id = db.Column (db.Integer, primarykey=True, autoincrement=True)
    conteudo = db.Column (db.String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "conteudo": self.conteudo}