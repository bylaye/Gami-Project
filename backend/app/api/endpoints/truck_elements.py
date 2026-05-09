from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.db.session import get_db
from app.api import deps
from app.models.user import User
from app.models.truck_element import TruckStatus
from app.models.truck_element import TruckType
from app.schemas.truck_element import TruckStatusCreate
from app.schemas.truck_element import TruckStatusRead
from app.schemas.truck_element import TruckTypeCreate
from app.schemas.truck_element import TruckTypeRead

router = APIRouter()

@router.post("/types", response_model=TruckTypeRead, summary="Ajouter le type de Camion")
def create_truck_type(
        truck_type_in: TruckTypeCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(deps.get_current_admin),
    ):
    db_obj = TruckType(**truck_type_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

@router.post("/status", response_model=TruckStatusRead, summary="Ajouter le status de camion")
def create_truck_status(
        truck_status_in: TruckStatusCreate,
        db: Session = Depends(get_db)
    ):
    db_obj = TruckStatus(**truck_status_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

