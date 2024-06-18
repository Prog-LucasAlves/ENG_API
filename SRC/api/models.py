from sqlalchemy import Column, Integer
from .database import Base


class User(Base):
    __tablename__ = "Dadapredict"

    id = Column(Integer, primary_key=True, index=True)
    tamanho = Column(Integer)
    quartos = Column(Integer)
    vagas = Column(Integer)
