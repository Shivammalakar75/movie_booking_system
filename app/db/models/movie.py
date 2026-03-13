from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.show import Show

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    duration: Mapped[int] = mapped_column(Integer)
    genre: Mapped[str] = mapped_column(String(100))
    language: Mapped[str] = mapped_column(String(50))
    release_date: Mapped[Date] = mapped_column(Date)

    shows: Mapped[list["Show"]] = relationship(back_populates="movie")