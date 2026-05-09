from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base # Ton instance declarative_base

class OfferGroup(Base):
    __tablename__ = "offer_groups"

    id = Column(Integer, primary_key=True, index=True)
    offer_group_name = Column(String(50), unique=True, index=True, nullable=False)

    # Relation vers les offres (One-to-Many)
    offers = relationship("Offer", back_populates="group")


class OfferStatus(Base):
    __tablename__ = "offer_statuses"

    id = Column(Integer, primary_key=True, index=True)
    offer_status_name = Column(String(50), unique=True, nullable=False)

    offers = relationship("Offer", back_populates="status")


class OfferGoodsType(Base):
    __tablename__ = "offer_goods_types"

    id = Column(Integer, primary_key=True, index=True)
    offer_goods_name = Column(String(50), unique=True, nullable=False)

    offers = relationship("Offer", back_populates="goods_type")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(50), index=True, nullable=False)
    company_country = Column(String(50), nullable=True)
    company_address = Column(String(50), nullable=True)
    company_phone = Column(String(50), nullable=True)

    # Une entreprise peut avoir posté plusieurs offres
    offers = relationship("Offer", back_populates="company")