from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.transaction_schemas import TransactionCreate, TransactionResponse
from app.crud.transaction_crud import get_transactions, get_transaction, create_transaction, update_transaction, delete_transaction

router = APIRouter()


@router.get("/transactions/", response_model=List[TransactionResponse])
def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of transactions from the database.

    Parameters:
    skip (int): The number of records to skip for pagination. Default is 0.
    limit (int): The maximum number of records to return. Default is 10.
    db (Session): The database session dependency.

    Returns:
    List[TransactionResponse]: A list of transaction records.
    """
    return get_transactions(db, skip=skip, limit=limit)

@router.get("/transactions/", response_model=List[TransactionResponse])
def read_transactions_by_user_id(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of transactions from the database for a specific user.

    Parameters:
    user_id (int): The ID of the user whose transactions to retrieve.
    db (Session): The database session dependency.

    Returns:
    List[TransactionResponse]: A list of transaction records for the given user.
    """
    return get_transactions(db, user_id=user_id)

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
    return get_transaction(db, transaction_id=transaction_id)

@router.post("/transactions/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    """
    Create a new transaction in the database.

    Parameters:
    transaction (TransactionCreate): The transaction data to create.
    db (Session): The database session dependency.

    Returns:
    TransactionResponse: The created transaction record.
    """
    return create_transaction(db, transaction=transaction)

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
    return update_transaction(db, transaction_id=transaction_id, transaction=transaction)

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
    return delete_transaction(db, transaction_id=transaction_id)