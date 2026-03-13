from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.booking import Booking
from app.db.models.user_role import UserRole

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[Date] = mapped_column(Date)

    bookings: Mapped[list["Booking"]] = relationship(back_populates="user")
    roles: Mapped[list["UserRole"]] = relationship(back_populates="user")