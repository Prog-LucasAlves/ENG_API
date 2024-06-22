from sqlalchemy.orm import Session

from . import models, schemas


def insertDataVar(db: Session, data: schemas.DataPredcit):
    db_item = models.Datavar(**data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def insertDatapred(db: Session, data: schemas.DataPredcitResponse):
    db_item = models.Datapred(**data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
