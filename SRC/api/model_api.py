from http import HTTPStatus

import joblib
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import actions, models, schemas
from .database import SessionLocal, engine

models.BASE.metadata.create_all(bind=engine)

app = FastAPI()

modelo = joblib.load('model.pkl')


def Acessdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', status_code=HTTPStatus.OK, response_model=schemas.DataMessage)
def index():
    return {'message': 'API is running'}


@app.post('/predict', status_code=HTTPStatus.CREATED)
def predict(data: schemas.DataPredcit, db: Session = Depends(Acessdb)):
    input_data = [[data.tamanho, data.quartos, data.banheiros, data.vagas]]
    actions.insertDataVar(db=db, data=data)
    predicition = modelo.predict(input_data)
    actions.selectDataVar(db=db)
    return {'prediction': predicition[0]}
