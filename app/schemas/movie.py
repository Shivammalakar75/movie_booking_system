from pydantic import BaseModel
from datetime import date

class MovieCreate(BaseModel):
    tittle: str
    duration: int
    genre: str
    language: str
    release_date: date

class MovieResponse(BaseModel):
    id: int
    tittle: str
    duration: int
    genre: str
    language: str
    release_date: date

    model_config = {"from_attributes":True}
    