from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from app.db.session import get_db
from app.api import deps
from app.models.user import User
from app.models.transporter import Transporter
from app.schemas.transporter import TransporterCreate
from app.schemas.transporter import TransporterRead

router = APIRouter()

@router.post("/create", response_model=TransporterRead, summary="Add new Transporter")
def create_transporter(
    transporter_in: TransporterCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_user),
):
    
    #db_obj = Transporter(
    #        society=transporter_in.society,
    #        country=transporter_in.country,
    #        base_town = transporter_in.base_town,
    #        phone = transporter_in.phone,
    #    )
    existing_society = db.query(Transporter).filter(
        Transporter.society == transporter_in.society
    ).first()

    if existing_society:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Society {transporter_in.society} already exist",
        )
    
    db_obj = Transporter(**transporter_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/get/all", response_model=list[TransporterRead], summary="Admin: Liste de tous les transporteurs")
def read_transporters(
    db: Session = Depends(get_db),
    skip: int=0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_admin),
):
    """
        Restriction Administrateur
    """
    transporters = db.query(Transporter).offset(skip).limit(limit).all()
    return transporters

@router.get("/get", response_model=TransporterRead, summary="un transporteur")
def read_transporter(
    transporter_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_user),
):

    db_transporter = db.query(Transporter).filter(Transporter.id == transporter_id).first()
    if not db_transporter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transporter not found",
        )
    if current_user.transporter_id != transporter_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Pas droit de consulter ce transporteur",
        )
    return db_transporter
