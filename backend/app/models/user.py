import enum
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    TRANSPORTER = "transporter"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[int] = mapped_column(Boolean, default=False) 
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole), default=UserRole.TRANSPORTER, nullable=False
    )
    transporter_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("transporters.id", ondelete="CASCADE"), nullable=False
    )
