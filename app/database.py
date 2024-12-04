from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


url_object = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
)

# URL connexion with dataBase
DATABASE_URL = url_object

engine = create_engine(DATABASE_URL)

# Create dataBase to modules
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to get a session from the DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
