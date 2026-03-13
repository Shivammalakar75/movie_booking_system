from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    user_id: int
    show_id: int
    total_price: float
    status: str

class BookingResponse(BaseModel):
    id: int
    user_id: int
    show_id: int
    total_price: float
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}