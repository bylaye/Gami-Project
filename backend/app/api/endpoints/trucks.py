from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.db.session import get_db
from app.models.truck import Truck
from app.schemas.truck import TruckCreate
from app.schemas.truck import TruckRead

router = APIRouter()

@router.post("/add", response_model=TruckRead, summary="Ajout Camion")
def create_truck(
        truck_in: TruckCreate,
        db: Session = Depends(get_db)
    ):
    db_obj = Truck(**truck_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


