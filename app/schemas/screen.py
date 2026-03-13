from pydantic import BaseModel

class ScreenCreate(BaseModel):
    theatre_id: int
    name: str
    total_seats: int

class ScreenResponse(BaseModel):
    id: int
    theatre_id: int
    name: str
    total_seats: int

    model_config = {"from_attributes":True}
    