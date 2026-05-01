from pydantic import BaseModel, ConfigDict
from typing import Optional

class BaseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)


""" Offer Group """
class OfferGroupCreate(BaseModel):
    offer_group_name: str

class OfferGroupRead(OfferGroupCreate, BaseRead):
    id: int

class OfferGroupUpdate(BaseModel):
    offer_group_name: Optional[str] = None


""" Offer Status """
class OfferStatusCreate(BaseModel):
    offer_status_name: str

class OfferStatusRead(OfferStatusCreate, BaseRead):
    id: int

class OfferStatusUpdate(BaseModel):
    offer_status_name: Optional[str] = None


""" Offer goods (Merchandises)"""
class OfferGoodsCreate(BaseModel):
    offer_goods_name: str

class OfferGoodsRead(OfferGoodsCreate, BaseRead):
    id: int

class OfferGoodsUpdate(BaseModel):
    offer_goods_name: Optional[str] = None


""" Company offer """
class CompanyBase(BaseModel):
    company_country: Optional[str] = None
    company_address: Optional[str] = None
    company_phone: Optional[str] = None

class CompanyCreate(CompanyBase):
    company_name: str

class CompanyRead(CompanyCreate, BaseRead):
    id: int

class CompanyUpdate(CompanyBase):
    company_name: Optional[str] = None
