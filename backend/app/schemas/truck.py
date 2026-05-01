from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class TruckBase(BaseModel):
    truck_type_id: int
    truck_status_id: int
    transporter_id: int
    registered: str
    truck_pv: float = Field(..., gt=0, description="poid camion vide")
    truck_ptac: float = Field(..., gt=0, description="poid camion max")

class TruckCreate(TruckBase):
    pass

class TruckRead(TruckCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

