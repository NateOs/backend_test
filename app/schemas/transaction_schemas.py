from pydantic import BaseModel, Field
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_name(name: str) -> str:
    encrypted_name = cipher_suite.encrypt(name.encode())
    return encrypted_name.decode()

def decrypt_name(encrypted_name: str) -> str:
    decrypted_name = cipher_suite.decrypt(encrypted_name.encode())
    return decrypted_name.decode()

class TransactionCreate(BaseModel):
    user_id: int
    full_name: str
    transaction_date: datetime = datetime.now()
    transaction_amount: float
    transaction_type: str # 'credit' or 'debit'
    
    def encrypt_full_name(self) -> str:
        return encrypt_name(self.full_name)

    class Config:
        orm_mode = True

    def model_dump(self):
        data = super().model_dump()
        # Encrypt full_name before dumping to dictionary
        data['full_name'] = self.encrypt_full_name()
        return data
    
class TransactionResponse(BaseModel):
    id: int
    user_id: int
    full_name: str
    transaction_date: datetime
    transaction_amount: float
    transaction_type: str

    def decrypt_full_name(self) -> str:
        try:
            return decrypt_name(self.full_name)
        except InvalidToken:
            raise ValueError("Decryption failed. Invalid token or corrupted data.")

    class Config:
        orm_mode = True

    def model_dump(self):
        data = super().model_dump()
        # Decrypt full_name before returning the response
        data['full_name'] = self.decrypt_full_name()
        return data