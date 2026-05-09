from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.db.session import get_db
from app.models.transporter import Transporter
from app.schemas.transporter import TransporterCreate
from app.schemas.transporter import TransporterRead

router = APIRouter()

@router.post("/create", response_model=TransporterRead, summary="Add new Transporter")
def create_transporter(
        transporter_in: TransporterCreate,
        db: Session = Depends(get_db)
        ):
    
    #db_obj = Transporter(
    #        society=transporter_in.society,
    #        country=transporter_in.country,
    #        base_town = transporter_in.base_town,
    #        phone = transporter_in.phone,
    #    )
    
    db_obj = Transporter(**transporter_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

