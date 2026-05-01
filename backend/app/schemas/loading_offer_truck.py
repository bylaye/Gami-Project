from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime 

class LoadingOfferTruckBase(BaseModel):
    offer_id: int
    truck_id: int
    is_unloaded: bool = False

class LoadingOfferTruckCreate(LoadingOfferTruckBase):
    charge: float = Field(..., gt=0, description="Poids charge en tonnes")

class LoadingOfferTruckUpdate(BaseModel):
    is_unloaded: Optional[bool] = None

class LoadingOfferTruckRead(LoadingOfferTruckBase):
    id: int
    charge: float
    create_at: datetime
    update_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)



