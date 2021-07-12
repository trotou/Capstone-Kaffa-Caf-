from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class OperadorModel(db.Model):
    id: int
    nome: str
    cpf: str

    __tablename__ = "operadores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)

    lista_caixas = relationship("CaixaModel", backref=backref("lista_operadores"), secondary="operador_caixa")