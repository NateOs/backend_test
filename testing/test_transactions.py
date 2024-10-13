import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

client = TestClient(app)

def test_create_transaction():
    response = client.post(
        "/transactions/",
        json={
            "user_id": 1,
            "full_name": "John Doe",
            "transaction_date": "2023-10-01",
            "transaction_amount": 100.0,
            "transaction_type": "credit"
        }
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == 1
    assert response.json()["transaction_amount"] == 100.0

def test_get_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)[pytest]
