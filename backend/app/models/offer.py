from __future__ import annotations
from datetime import datetime
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Offer(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Trajet et logistique
    offer_from: Mapped[str] = mapped_column(String(50), index=True, nullable=False) # Ville départ
    offer_to: Mapped[str] = mapped_column(String(50), index=True, nullable=False)   # Ville arrivée
    tonnage: Mapped[float] = mapped_column(Float, nullable=False)
    budget: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Dates
    offer_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # --- Clés Étrangères (Relations Obligatoires) ---
    
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey("offer_statuses.id"), nullable=False)
    goods_id: Mapped[int] = mapped_column(Integer, ForeignKey("offer_goods_types.id"), nullable=False)
    
    # --- Clés Étrangères (Relations Optionnelles / Evolutives) ---
    
    # Un groupe d'offres (ex: Campagne de transport spécifique)
    offer_group_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("offer_groups.id"), nullable=True)
    
    # Le transporteur qui a accepté/été assigné à l'offre
    transporter_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("transporters.id"), nullable=True)

    # --- Relations ORM ---
    
    company: Mapped["Company"] = relationship("Company", back_populates="offers")
    status: Mapped["OffeStatus"] = relationship("OfferStatus", back_populates="offers")
    goods_type: Mapped["OfferGoodsType"] = relationship("OfferGoodsType", back_populates="offers")
    group: Mapped["OfferGroup | None"] = relationship("OfferGroup", back_populates="offers")
    #transporter = relationship("Transporter", back_populates="offers")
    
    # Relation vers les camions chargés pour cette offre
    #loadings = relationship("LoadingOfferTruck", back_populates="offer")
