import pandas as pd
from sqlalchemy.orm import Session

from . import models, schemas


def insertDataVar(db: Session, data: schemas.DataPredcit):
    db_item = models.Datavar(**data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def selectDataVar(db: Session):
    data = db.query(models.Datavar).all()
    select_data = [
        {
            'tamanho': item.tamanho,
            'quartos': item.quartos,
            'banheiros': item.banheiros,
            'vagas': item.vagas,
        }
        for item in data
    ]
    df = pd.DataFrame(select_data)
    csv_file_path = 'data_var.csv'
    df.to_csv(csv_file_path, index=False)
