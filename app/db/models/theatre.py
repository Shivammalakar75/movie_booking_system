from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.screen import Screen

class Theatre(Base):
    __tablename__ = "theatres"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    location: Mapped[str] = mapped_column(String(150))
    city: Mapped[str] = mapped_column(String(100))

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    screens: Mapped[list["Screen"]] = relationship(back_populates="theatre")