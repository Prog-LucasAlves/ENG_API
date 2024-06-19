from sqlalchemy.orm import Session
from . import models, schemas


def insertData(db: Session, data: schemas.DataPredcit):
    db_item = models.User(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
