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


@app.post('/predict/', status_code=HTTPStatus.CREATED)
def predict(datavar: schemas.DataPredcit, db: Session = Depends(Acessdb)):
    dados_entrada = [[datavar.tamanho, datavar.quartos, datavar.vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    actions.insertDataVar(db=db, data=datavar)
    return {'preco_estimado': round(preco_estimado, 2)}
