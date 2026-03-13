
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.base import Base
from app.db.models.role_permission import RolePermission
class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    roles: Mapped[list["RolePermission"]] = relationship(back_populates="permission")