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

@router.post("/types/add", response_model=TruckTypeRead, summary="Ajouter le type de Camion")
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

@router.get("/types/get/all", response_model=list[TruckTypeRead], summary="Les types de Camion")
def read_truck_types(db: Session = Depends(get_db)):
    types = db.query(TruckType).all()
    return types




@router.post("/status/add", response_model=TruckStatusRead, summary="Ajouter le status de camion")
def create_truck_status(
        truck_status_in: TruckStatusCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(deps.get_current_admin),
    ):
    db_obj = TruckStatus(**truck_status_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

@router.get("/status/get/all", response_model=list[TruckStatusRead], summary="Les differents etats des Camion")
def read_truck_status(db: Session = Depends(get_db)):
    status = db.query(TruckStatus).all()
    return status
