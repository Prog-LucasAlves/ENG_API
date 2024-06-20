import joblib
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import actions, models, schemas
from .database import SessionLocal, engine

models.BASE.metadata.create_all(bind=engine)

app = FastAPI()

modelo = joblib.load('model.pkl')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/data')
def data(data: schemas.DataPredcit, db: Session = Depends(get_db)):
    return actions.insertData(db=db, data=data)
