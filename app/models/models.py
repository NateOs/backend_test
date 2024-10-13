
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    transaction_date = Column(DateTime(timezone=True), server_default=func.now())
    transaction_amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)  # This will store 'credit' or 'debit'
