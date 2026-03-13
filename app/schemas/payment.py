from pydantic import BaseModel
from datetime import datetime

class PaymentCreate(BaseModel):
    booking_id: int
    amount: float
    payment_method: str
    status: str

class PaymentResponse(BaseModel):
    id: int
    booking_id: int
    amount: float
    payment_method: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}