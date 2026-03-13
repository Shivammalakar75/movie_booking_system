from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.screen import Screen
from app.db.models.booking_seat import BookingSeat
from app.db.models.show_seat import ShowSeat

class Seat(Base):
    __tablename__ = "seats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id"))

    seat_number: Mapped[str] = mapped_column(String(10))
    row: Mapped[str] = mapped_column(String(5))

    screen: Mapped["Screen"] = relationship(back_populates="seats")

    booking_seats: Mapped[list["BookingSeat"]] = relationship(back_populates="seat")
    show_seats: Mapped[list["ShowSeat"]] = relationship(back_populates="seat")