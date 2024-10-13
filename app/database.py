from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
print("Environment variables loaded.")


# Create an engine
DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL is None:
    print("DATABASE_URL not found in environment.")
else:
    print(DATABASE_URL)
    
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()