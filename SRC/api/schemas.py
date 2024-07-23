from pydantic import BaseModel


class DataMessage(BaseModel):
    message: str


class DataPredcit(BaseModel):
    tamanho: int
    quartos: int
    banheiros: int
    vagas: int
