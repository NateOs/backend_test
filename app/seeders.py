# app/seeder.py

from sqlalchemy.orm import Session
from app.models.models import Transaction
from app.database import SessionLocal
import datetime
# Sample data to be seeded
initial_data = [
    {
        "user_id": 1,
        "full_name": "John Doe",
        "transaction_date": datetime.datetime.now(),
        "transaction_amount": 100.0,
        "transaction_type": "credit"
    },
    {
        "user_id": 2,
        "full_name": "Jane Smith",
        "transaction_date": datetime.datetime.now(),
        "transaction_amount": 250.5,
        "transaction_type": "debit"
    },
    {
        "user_id": 3,
        "full_name": "Alice Johnson",
        "transaction_date": datetime.datetime.now(),
        "transaction_amount": 300.75,
        "transaction_type": "credit"
    }
]

# Function to seed the database if no data exists
def seed_data(db: Session):
    if not db.query(Transaction).first():  # Check if any data exists
        for data in initial_data:
            transaction = Transaction(**data)
            db.add(transaction)
        db.commit()
        print("Database seeded with initial data")
    else:
        print("Database already contains data, skipping seeding")

# Function to run the seeder on startup
def run():
    db = SessionLocal()
    try:
        seed_data(db)
    finally:
        db.close()

if __name__ == "__main__":
    run()
