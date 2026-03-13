from pydantic import BaseModel

class SeatCreate(BaseModel):
    screen_id: int
    seat_number: str
    row: str

class SeatResponse(BaseModel):
    id: int
    screen_id: int
    seat_number: str
    row: str

    model_config = {"from_attributes":True}
    