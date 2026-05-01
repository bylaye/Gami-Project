from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

class Truck(Base):
    __tablename__ = "trucks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    registered: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    
    # Poids (PV et PTAC)
    truck_pv: Mapped[float] = mapped_column(Float, nullable=False)
    truck_ptac: Mapped[float] = mapped_column(Float, nullable=False)

    # --- Clés Étrangères ---
    
    # Lien vers le transporteur (Propriétaire)
    transporter_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("transporters.id", ondelete="CASCADE"), nullable=False
    )
    
    # Liens vers les référentiels (Type et Statut)
    truck_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("truck_types.id"), nullable=False
    )
    truck_status_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("truck_statuses.id"), nullable=False
    )

    # --- Relations ---
    
    transporter = relationship("Transporter", back_populates="trucks")
    truck_type = relationship("TruckType", back_populates="trucks")
    truck_status = relationship("TruckStatus", back_populates="trucks")
    
    # Un camion peut être impliqué dans plusieurs chargements (Loading)
    loadings = relationship("LoadingOfferTruck", back_populates="truck")
