from pydantic import BaseModel, ConfigDict
from typing import Optional

class BaseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)


""" Offer Group """
class OfferGroupCreate(BaseModel):
    offer_group_name: str

class OfferGroupRead(OfferGroupCreate, BaseRead):
    id: int

class OfferGroupUpdate(OfferGroupCreate):
    pass


""" Offer Status """
class OfferStatusCreate(BaseModel):
    offer_status_name: str

class OfferStatusRead(OfferStatusCreate, BaseRead):
    id: int

class OfferStatusUpdate(OfferStatusCreate):
    pass


""" Offer goods (Merchandises)"""
class OfferGoodsCreate(BaseModel):
    offer_goods_name: str

class OfferGoodsRead(OfferGoodsCreate, BaseRead):
    id: int

class OfferGoodsUpdate(OfferGoodsCreate):
    pass


""" Company offer """
class CompanyCreate(BaseModel):
    company_name: str
    company_country: Optional[str] = None
    company_address: Optional[str] = None
    company_phone: Optional[str] = None

class CompanyRead(CompanyCreate, BaseRead):
    id: int

class CompanyUpdate(CompanyCreate):
    pass

