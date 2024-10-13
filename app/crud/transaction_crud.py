from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import Transaction
from app.schemas.transaction_schemas import TransactionCreate, TransactionResponse


def get_transactions(db: Session, skip: int = 0, limit: int = 10, user_id: int = None):
    """
    Retrieve a list of transactions from the database.

    Parameters:
    db (Session): The database session dependency.
    skip (int): The number of records to skip for pagination. Default is 0.
    limit (int): The maximum number of records to return. Default is 10.
    user_id (int): The ID of the user whose transactions to retrieve.

    Returns:
    List[TransactionResponse]: A list of transaction records.
    """
    query = db.query(Transaction)

    if user_id:
        query = query.filter(Transaction.user_id == user_id)

    return query.offset(skip).limit(limit).all()


def get_transaction(db: Session, transaction_id: int):
    """
    Retrieve a single transaction from the database by ID.

    Parameters:
    db (Session): The database session dependency.
    transaction_id (int): The ID of the transaction to retrieve.

    Returns:
    TransactionResponse: The transaction record with the given ID.
    """
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def create_transaction(db: Session, transaction: TransactionCreate):
    """
    Create a new transaction in the database.

    Parameters:
    db (Session): The database session dependency.
    transaction (TransactionCreate): The transaction data to create.
    Returns:
    TransactionResponse: The created transaction record.
    """
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def update_transaction(db: Session, transaction_id: int, transaction: TransactionCreate):
    """
    Update an existing transaction in the database.

    Parameters:
    db (Session): The database session dependency.
    transaction_id (int): The ID of the transaction to update.
    transaction (TransactionCreate): The updated transaction data.
    Returns:
    TransactionResponse: The updated transaction record.
    """
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction:
        db_transaction.full_name = transaction.full_name
        db_transaction.transaction_date = transaction.transaction_date
        db_transaction.transaction_amount = transaction.transaction_amount
        db_transaction.transaction_type = transaction.transaction_type
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")
    

def delete_transaction(db: Session, transaction_id: int):
    """
    Delete a transaction from the database by ID.

    Parameters:
    db (Session): The database session dependency.
    transaction_id (int): The ID of the transaction to delete.
    Returns:
    TransactionResponse: The deleted transaction record.
    """
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return db_transaction
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")