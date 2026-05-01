from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class OfferBase(BaseModel):
    transporter_id: Optional[int]
    offer_group_id: Optional[int]
    tonnage: float = Field(..., gt=0, description="poid total en tonne")
    budget: float = Field(..., gt=0, description="Budget total offre")
    offer_date: Optional[datetime] = None

class OfferCreate(OfferBase):
    type_id: int
    status_id: int
    goods_id: int
    company_id: int
    offer_from: str
    offer_to: str

class OfferRead(OfferCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class OfferUpdate(OfferBase):
    pass
