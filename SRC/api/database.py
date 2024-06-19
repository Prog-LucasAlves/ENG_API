from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("Name")
password = os.getenv("Password")
database = os.getenv("Database")
host = os.getenv("External_Database_URL")
url = os.getenv("url")

DATABASE_URL = f"{url}"
# DATABASE_URL = f"postgresql://{username}:{password}@{host}:5432/{database}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BASE = declarative_base()
