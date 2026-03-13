from sqlalchemy import Integer, ForeignKey, String, Date, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.booking import Booking

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id"))

    amount: Mapped[float] = mapped_column(DECIMAL(10,2))
    status: Mapped[str] = mapped_column(String(50))
    payment_method: Mapped[str] = mapped_column(String(50))

    created_at: Mapped[Date] = mapped_column(Date)

    booking: Mapped["Booking"] = relationship(back_populates="payment")