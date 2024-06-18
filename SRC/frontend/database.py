from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("Name")
password = os.getenv("Password")
database = os.getenv("Database")
host = os.getenv("External_Database_URL")

DATABASE_URL = f"postgresql://{username}:{password}@{host}:5432/{database}"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)

BASE = declarative_base()


class User(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


BASE.metadata.create_all(engine)
print("Tabela criada com sucesso.")


Session = sessionmaker(bind=engine)
session = Session()

user = User(name="John Doe", email="john@example.com")
session.add(user)
session.commit()

print("Usuário inserido com sucesso.")
