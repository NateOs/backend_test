import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List, Dict
from datetime import date

from app.redis_client import redis_client
from app.database import get_db
from app.crud.transaction_crud import get_transactions

router = APIRouter()

def calculate_user_analytics(user_id: int, transactions):
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
    
    # Convert the highest_day to a string
    highest_day_str = highest_day.isoformat() if highest_day else None
    
    return {
        "average_transaction_value": average_value,
        "day_with_most_transactions": highest_day_str,
        "total_transaction_count": len(transactions)
    }

@router.get("/analytics/{user_id}", response_model=Dict[str, Any])
def get_user_analytics(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve user analytics based on transaction data.

    This function fetches transaction data for a given user, calculates analytics,
    and caches the result in Redis for future requests.
    
    Analytics are worked together as one object to improve performance.

    Parameters:
    user_id (int): The ID of the user for whom analytics are being retrieved.
    db (Session): The database session used to query transaction data.

    Returns:
    Dict[str, Any]: A dictionary containing the user's analytics, including
    average transaction value, the day with the most transactions, and the total
    transaction count.
    """
    cache_key = f"user_analytics:{user_id}"
    cached_result = redis_client.get(cache_key)

    if cached_result:
        return json.loads(cached_result)

    transactions = get_transactions(db, user_id=user_id)
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for the user")

    analytics = calculate_user_analytics(user_id, transactions)

    redis_client.setex(cache_key, 3600, json.dumps(analytics))

    return analytics