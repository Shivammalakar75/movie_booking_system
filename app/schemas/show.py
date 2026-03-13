from pydantic import BaseModel
from datetime import datetime

class ShowCreate(BaseModel):
    movie_id: int
    screen_id: int
    start_time: datetime
    end_time: datetime
    price: float

class ShowResponse(BaseModel):
    id: int
    movie_id: int
    screen_id: int
    start_time: datetime
    end_time: datetime
    price: float

    model_config = {"from_attributes":True}
