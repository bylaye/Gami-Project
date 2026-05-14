from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.db.base_class import Base # Ton instance declarative_base

class OfferGroup(Base):
    __tablename__ = "offer_groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    offer_group_name:Mapped[str] = Column(String(50), unique=True, index=True, nullable=False)

    # Relation vers les offres (One-to-Many)
    offers: Mapped[list["Offer"]] = relationship("Offer", back_populates="group")


class OfferStatus(Base):
    __tablename__ = "offer_statuses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    offer_status_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    offers: Mapped[list["Offer"]] = relationship("Offer", back_populates="status")


class OfferGoodsType(Base):
    __tablename__ = "offer_goods_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    offer_goods_name: Mapped[int] = mapped_column(String(50), unique=True, nullable=False)

    offers: Mapped[list["offer"]] = relationship("Offer", back_populates="goods_type")


class Company(Base):
    __tablename__ = "companies"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    company_name: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    company_country: Mapped[str] = mapped_column(String(50), nullable=True)
    company_address: Mapped[str] = mapped_column(String(50), nullable=True)
    company_phone: Mapped[str] = mapped_column(String(50), nullable=True)

    # Une entreprise peut avoir posté plusieurs offres
    offers: Mapped[list["Offer"]] = relationship("Offer", back_populates="company")
