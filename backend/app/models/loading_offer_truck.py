from sqlalchemy import Float, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.base_class import Base

class LoadingOfferTruck(Base):
    __tablename__ = "loading_offer_trucks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Données métier du chargement
    charge: Mapped[float] = mapped_column(Float, nullable=False) # Poids effectif chargé
    is_unloaded: Mapped[bool] = mapped_column(Boolean, default=False) # Statut de livraison

    # --- Clés Étrangères ---
    
    # Lien vers l'offre
    offer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("offers.id", ondelete="CASCADE"), nullable=False
    )
    
    # Lien vers le camion
    truck_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("trucks.id", ondelete="CASCADE"), nullable=False
    )

    # --- Timestamps ---
    
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    update_at: Mapped[datetime | None] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )

    # --- Relations ---
    
    offer = relationship("Offer", back_populates="loadings")
    truck = relationship("Truck", back_populates="loadings")