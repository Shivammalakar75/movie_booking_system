from pydantic import BaseModel

class BookingSeatCreate(BaseModel):
    booking_id: int
    seat_id: int

class BookingSeatResponse(BaseModel):
    id: int
    booking_id: int
    seat_id: int

    model_config = {"from_attributes": True}