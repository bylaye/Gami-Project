from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.base_class import Base

class TruckType(Base):
    __tablename__ = "truck_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    truck_type_name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    #trucks = relationship("Truck", back_populates="truck_type")


class TruckStatus(Base):
    __tablename__ = "truck_statuses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    truck_status_name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    #trucks = relationship("Truck", back_populates="truck_status")
