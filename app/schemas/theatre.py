from pydantic import BaseModel

class TheatreCreate(BaseModel):
    name: str
    location: str
    city: str
    owner_id: int

class TheatreResponse(BaseModel):
    id: int
    name: str
    location: str
    city: str
    owner_id: int

    model_config = {"from_attributes":True}
    