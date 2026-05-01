from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TransporterBase(BaseModel):
    country: Optional[str] = None
    base_town: Optional[str] = None
    phone: Optional[str] = None

class TransporterCreate(TransporterBase):
    society: str

class TransporterRead(TransporterCreate):
    id: int
    status: bool = False
    model_config = ConfigDict(from_attributes=True)

class TransporterUpdate(TransporterBase):
    society: Optional[str]

class TransporterStatusUpdate(BaseModel):
    status: bool

class TransporterSuspendUpdate(BaseModel):
    is_suspend: bool

