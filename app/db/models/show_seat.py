from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.show import Show
from app.db.models.seat import Seat

class ShowSeat(Base):
    __tablename__ = "show_seats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id"))
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"))

    status: Mapped[str] = mapped_column(String(50))

    show: Mapped["Show"] = relationship(back_populates="show_seats")
    seat: Mapped["Seat"] = relationship(back_populates="show_seats")