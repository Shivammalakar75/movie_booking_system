from pydantic import BaseModel

class ShowSeatCreate(BaseModel):
    show_id: int
    seat_id: int
    status: str

class ShowSeatResponse(BaseModel):
    id: int
    show_id: int
    seat_id: int
    status: str

    model_config = {"from_attributes": True}