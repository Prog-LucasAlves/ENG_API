from sqlalchemy.orm import Session

from . import actions
from .database import SessionLocal


def Acessdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def Collectdata(db: Session = Acessdb):
    data = actions.selectDataVar(db=db)
    data.to_csv('./data_var.csv', index=False)
