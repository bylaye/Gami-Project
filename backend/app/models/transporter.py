from sqlalchemy import String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.base_class import Base

class Transporter(Base):
    __tablename__ = "transporters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    society: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    country: Mapped[str | None] = mapped_column(String(50), nullable=True)
    base_town: Mapped[str | None] = mapped_column(String(50), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    is_suspend: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )

    # --- Relations ---
    
    # Lien vers l'utilisateur (Authentification)
    #user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), unique=True)
    #user = relationship("User", back_populates="transporter")

    # Un transporteur possède plusieurs camions
    #trucks = relationship("Truck", back_populates="transporter", cascade="all, delete-orphan")
    #trucks = relationship("Truck", back_populates="transporter")
