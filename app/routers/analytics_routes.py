from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List, Dict
from datetime import date

from app.database import get_db
from app.crud.transaction_crud import get_transactions

router = APIRouter()

@router.get("/analytics/{user_id}", response_model=Dict[str, Any])
def get_user_analytics(user_id: int, db: Session = Depends(get_db)):
    transactions = get_transactions(db, user_id=user_id)
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for the user")
    
    # Calculate average transaction value
    total_value = sum(transaction.transaction_amount for transaction in transactions)
    average_value = total_value / len(transactions) if transactions else 0
    
    # Calculate the day with the highest number of transactions
    transaction_count_by_day = {}
    for transaction in transactions:
        day = transaction.transaction_date.date()
        if day not in transaction_count_by_day:
            transaction_count_by_day[day] = 0
        transaction_count_by_day[day] += 1
    
    highest_day = max(transaction_count_by_day, key=transaction_count_by_day.get) if transaction_count_by_day else None
    
    return {
        "average_transaction_value": average_value,
        "day_with_most_transactions": highest_day,
        "total_transaction_count": len(transactions)}


