from http import HTTPStatus

import joblib
from fastapi import FastAPI

from . import models, schemas
from .database import engine

models.BASE.metadata.create_all(bind=engine)

app = FastAPI()

modelo = joblib.load('model.pkl')

"""
def Acessdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""


@app.get('/', status_code=HTTPStatus.OK, response_model=schemas.DataMessage)
def index():
    return {'message': 'API is running'}


@app.post('/predict', status_code=HTTPStatus.CREATED)
def predict(data: schemas.DataPredcit):
    input_data = [[data.tamanho, data.quartos, data.vagas]]
    predicition = modelo.predict(input_data)
    return {'prediction': predicition[0]}


"""
@app.post('/predict/', status_code=HTTPStatus.CREATED)
def predict(datavar: schemas.DataPredcit, db: Session = Depends(Acessdb)):
    features = [[datavar.tamanho, datavar.quartos, datavar.vagas]]
    preco_estimado = modelo.predict(features)[0]
    actions.insertDataVar(db=db, data=datavar)
    return {'preco_estimado': round(preco_estimado, 2)}
"""
