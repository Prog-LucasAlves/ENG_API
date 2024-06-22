from sqlalchemy import Column, Float, Integer

from .database import BASE

class Datavar(BASE):
    __tablename__ = 'Datavar'

    id = Column(Integer, primary_key=True, index=True)
    tamanho = Column(Integer)
    quartos = Column(Integer)
    vagas = Column(Integer)


class Datapred(BASE):
    __tablename__ = 'Datapred'

    id = Column(Integer, primary_key=True, index=True)
    previsao = Column(Float)
