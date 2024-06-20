from pydantic import BaseModel


class DataPredcit(BaseModel):
    tamanho: int
    quartos: int
    vagas: int


class DataPredcitResponse(BaseModel):
    preco_estimado: float
