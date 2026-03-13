from sqlalchemy import Integer, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.movie import Movie
from app.db.models.screen import Screen
from app.db.models.booking import Booking
from app.db.models.show_seat import ShowSeat

class Show(Base):
    __tablename__ = "shows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id"))

    start_time: Mapped[DateTime] = mapped_column(DateTime)
    end_time: Mapped[DateTime] = mapped_column(DateTime)

    price: Mapped[float] = mapped_column(DECIMAL(10,2))

    movie: Mapped["Movie"] = relationship(back_populates="shows")
    screen: Mapped["Screen"] = relationship(back_populates="shows")

    bookings: Mapped[list["Booking"]] = relationship(back_populates="show")
    show_seats: Mapped[list["ShowSeat"]] = relationship(back_populates="show")