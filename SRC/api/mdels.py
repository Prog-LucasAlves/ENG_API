from sqlalchemy import Column, INTEGER
from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy import String


class User(Base):
    __tablename__ = "Dadapredict"

    id = Column(INTEGER, primary_key=True, index=True)
    tamanho = Column(String)
    quartos = Column(String, unique=True, index=True)
    vagas = Column(String)

    items = relationship("Item", back_populates="owner")
