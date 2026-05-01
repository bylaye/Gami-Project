from pydantic import BaseModel, ConfigDict

class BaseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)


""" Type Truck """
class TruckTypeCreate(BaseModel):
    truck_type_name: str

class TruckTypeRead(TruckTypeCreate, BaseRead):
    id: int

class TruckTypeUpdate(TruckTypeCreate):
    pass


""" Truck status """
class TruckStatusCreate(BaseModel):
    truck_status_name: str

class TruckStatusRead(TruckStatusCreate, BaseRead):
    id: int

class TruckStatusUpdate(TruckStatusCreate):
    pass
