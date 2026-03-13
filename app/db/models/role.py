
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.db.models.user_role import UserRole
from app.db.models.role_permission import RolePermission

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    users: Mapped[list["UserRole"]] = relationship(back_populates="role")
    permissions: Mapped[list["RolePermission"]] = relationship(back_populates="role")