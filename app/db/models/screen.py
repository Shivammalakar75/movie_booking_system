from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.theatre import Theatre
from app.db.models.show import Show
from app.db.models.seat import Seat

class Screen(Base):
    __tablename__ = "screens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    theatre_id: Mapped[int] = mapped_column(ForeignKey("theatres.id"))
    name: Mapped[str] = mapped_column(String(100))
    total_seats: Mapped[int] = mapped_column(Integer)

    theatre: Mapped["Theatre"] = relationship(back_populates="screens")
    shows: Mapped[list["Show"]] = relationship(back_populates="screen")
    seats: Mapped[list["Seat"]] = relationship(back_populates="screen")