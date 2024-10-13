from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.transaction_schemas import decrypt_name, encrypt_name
from unittest.mock import patch


client = TestClient(app)

# Create a Transaction Record
# Primary Cases:

# Successfully create a transaction with valid data.

def test_create_transaction_valid_data():
    response = client.post(
        "/transactions/",
        json={
            "user_id": 1,
            "transaction_type": "credit",
            "transaction_amount": 1000,
            "full_name": "John Doe"
        }
    )
    assert response.status_code == 200
    decrypted_full_name = decrypt_name(response.json()["full_name"])
    assert decrypted_full_name == "John Doe"
    assert response.json()["transaction_type"] == "credit"
    assert response.json()["transaction_amount"] == 1000



# Edge Cases:

# Attempt to create a transaction with missing required fields.
def test_create_transaction_missing_required_fields():
    response = client.post(
        "/transactions/",
        json={
            "user_id": 1,
            "transaction_type": "credit",
            "transaction_amount": 1000
        }
    )
    assert response.status_code == 422
    


# Create a transaction with an invalid transaction_type.
def test_create_transaction_invalid_transaction_type():
    response = client.post(
        "/transactions/",
        json={
            "user_id": 1,
            "transaction_type": "invalid",
            "transaction_amount": 1000,
            "full_name": "John Doe"
        }
    )
    assert response.status_code == 422



# Create a transaction with a negative transaction_amount.
def test_create_transaction_negative_transaction_amount():
    response = client.post(
        "/transactions/",
        json={
            "user_id": 1,
            "transaction_type": "credit",
            "transaction_amount": -1000,
            "full_name": "John Doe"
        }
    )
    assert response.status_code == 422


# Retrieve transaction history for a user with no transactions.
def test_retrieve_transaction_history_with_transactions():
    # Create sample transactions
    transactions = [
        {
            "user_id": 1,
            "transaction_type": "credit",
            "transaction_amount": 1000,
            "full_name": "John Doe"
        },
        {
            "user_id": 1,
            "transaction_type": "debit",
            "transaction_amount": 500,
            "full_name": "John Doe"
        }
    ]

    for transaction in transactions:
        response = client.post("/transactions/", json=transaction)
        assert response.status_code == 200

    # Retrieve transaction history for user_id 1
    response = client.get("/transactions/?user_id=1")
    assert response.status_code == 200
    retrieved_transactions = response.json()
    assert len(retrieved_transactions) > 1
# Edge Cases:

# Retrieve transaction history with a large number of transactions to test performance.


# Update a Transaction Record

# Successfully update an existing transaction with valid data.

# Update only specific fields of a transaction.


# Edge Cases:

# Attempt to update a non-existent transaction.

# Update a transaction with invalid data (e.g., invalid transaction_type).


# Delete a Transaction Record
# Primary Cases:

# Successfully delete an existing transaction.

# Attempt to delete a transaction and verify it no longer exists.


# Edge Cases:

# Attempt to delete a non-existent transaction.

# Delete a transaction and ensure related data (e.g., cached data) is also updated.


# Transaction Analytics Endpoint
# Primary Cases:

# Successfully retrieve analytics for a user with multiple transactions.

# Retrieve analytics for a user with a single transaction.


# Edge Cases:

# Attempt to retrieve analytics for a non-existent user.

# Retrieve analytics for a user with no transactions.

# Test performance with a large dataset.