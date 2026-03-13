from sqlalchemy import Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.user import User
from app.db.models.show import Show
from app.db.models.booking_seat import BookingSeat
from app.db.models.payment import Payment

class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id"))

    status: Mapped[str] = mapped_column(String(50))

    total_price: Mapped[float] = mapped_column(DECIMAL(10,2))

    created_at: Mapped[Date] = mapped_column(Date)

    user: Mapped["User"] = relationship(back_populates="bookings")
    show: Mapped["Show"] = relationship(back_populates="bookings")

    seats: Mapped[list["BookingSeat"]] = relationship(back_populates="booking")

    payment: Mapped["Payment"] = relationship(back_populates="booking")