import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
username = os.getenv('PGUSER')
password = os.getenv('PGPASSWORD')
database = os.getenv('PGDATABASE')
host = os.getenv('PGHOST')
# url = os.getenv('url')

# DATABASE_URL = f'{url}'
DATABASE_URL = f'postgresql://{username}:{password}@{host}:5432/{database}'

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BASE = declarative_base()


class Datavar(BASE):
    __tablename__ = 'Datavar'

    id = Column(Integer, primary_key=True, index=True)
    tamanho = Column(Integer)
    quartos = Column(Integer)
    banheiros = Column(Integer)
    vagas = Column(Integer)


def selectDataVar(db=SessionLocal()):
    data = db.query(Datavar).all()
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
    df.to_csv('./data_var.csv', index=False)


if __name__ == '__main__':
    selectDataVar()
