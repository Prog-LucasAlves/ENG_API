from sqlalchemy import Column, Integer

from .database import BASE


class Datavar(BASE):
    __tablename__ = 'Datavar'

    id = Column(Integer, primary_key=True, index=True)
    tamanho = Column(Integer)
    quartos = Column(Integer)
    banheiros = Column(Integer)
    vagas = Column(Integer)
