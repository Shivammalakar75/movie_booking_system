
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.base import Base
from app.db.models.user import User
from app.db.models.role import Role

class UserRole(Base):
    __tablename__ = "user_roles"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)

    user: Mapped["User"] = relationship(back_populates="roles")
    role: Mapped["Role"] = relationship(back_populates="users")