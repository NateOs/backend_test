from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.transaction_schemas import TransactionCreate, TransactionResponse
from app.crud.transaction_crud import (
    get_transactions,
    get_transaction,
    create_transaction as create_transaction_crud,
    update_transaction as update_transaction_crud, 
    delete_transaction as delete_transaction_crud
)
router = APIRouter()


@router.get("/transactions/", response_model=List[TransactionResponse])
def read_transactions(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of transactions from the database for a specific user.

    Parameters:
    user_id (int): The ID of the user whose transactions to retrieve.
    db (Session): The database session dependency.

    Returns:
    List[TransactionResponse]: A list of transaction records for the given user.
    """
    return get_transactions(db, user_id=user_id)

from app.redis_client import redis_client
import json
@router.get("/transactions/", response_model=List[TransactionResponse])
def read_transactions_by_user_id(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of transactions from the database for a specific user.
    Transactions are cached for 1 hour to improve performance.
    Parameters:
    user_id (int): The ID of the user whose transactions to retrieve.
    db (Session): The database session dependency.

    Returns:
    List[TransactionResponse]: A list of transaction records for the given user.
    """
    cache_key = f"user_transactions:{user_id}"
    cached_transactions = redis_client.get(cache_key)

    if cached_transactions:
        return json.loads(cached_transactions)

    transactions = get_transactions(db, user_id=user_id)
    redis_client.setex(cache_key, 3600, json.dumps([transaction.__dict__ for transaction in transactions]))

    return transactions

@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single transaction from the database by ID.

    Parameters:
    transaction_id (int): The ID of the transaction to retrieve.
    db (Session): The database session dependency.

    Returns:
    TransactionResponse: The transaction record with the given ID.
    """
    transaction = get_transaction(db, transaction_id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    # Manually map the Transaction object to TransactionResponse
    transaction_response = TransactionResponse(
        id=transaction.id,
        user_id=transaction.user_id,
        full_name=transaction.full_name,  # Pass the encrypted name directly
        transaction_date=transaction.transaction_date,
        transaction_amount=transaction.transaction_amount,
        transaction_type=transaction.transaction_type
    )
    
    # Decrypt the full_name before returning
    transaction_response.full_name = transaction_response.decrypt_full_name()
    
    return transaction_response

@router.post("/transactions/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Create a new transaction in the database.

    Parameters:
    transaction (TransactionCreate): The transaction data to create.
    db (Session): The database session dependency.
    background_tasks (BackgroundTasks): The background tasks dependency.

    Returns:
    TransactionResponse: The created transaction record.
    """
    # Encrypt the full_name before creating the transaction
    transaction_data = transaction.model_dump()
    transaction_data['full_name'] = transaction.encrypt_full_name()

    # Create the transaction using the encrypted data
    created_transaction = create_transaction_crud(db, transaction=transaction_data, background_tasks=background_tasks)

    # Return the created transaction
    return TransactionResponse(**created_transaction)

@router.put("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_transaction(transaction_id: int, transaction: TransactionCreate, db: Session = Depends(get_db)):
    """
    Update an existing transaction in the database.

    Parameters:
    transaction_id (int): The ID of the transaction to update.
    transaction (TransactionCreate): The updated transaction data.
    db (Session): The database session dependency.

    Returns:
    TransactionResponse: The updated transaction record.
    """
    return update_transaction_crud(db, transaction_id=transaction_id, transaction=transaction)

@router.delete("/transactions/{transaction_id}", response_model=TransactionResponse)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """
    Delete a transaction from the database by ID.

    Parameters:
    transaction_id (int): The ID of the transaction to delete.
    db (Session): The database session dependency.

    Returns:
    TransactionResponse: The deleted transaction record.
    """
    return delete_transaction_crud(db, transaction_id=transaction_id)