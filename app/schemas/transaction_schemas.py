from pydantic import BaseModel
from datetime import datetime


class TransactionCreate(BaseModel):
    user_id: int
    full_name: str
    transaction_date: datetime = datetime.now()
    transaction_amount: float
    transaction_type: str # 'credit' or 'debit'
    
class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        orm_mode = True