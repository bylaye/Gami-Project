from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from app.db.session import get_db
from app.api import deps
from app.models.user import User
from app.models.offer import Offer
from app.schemas.offer import OfferCreate
from app.schemas.offer import OfferRead

router = APIRouter()

@router.post("/offer/add", response_model=OfferRead, summary="ajouter une offre")
def create_offer(
    offer_in: OfferCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_admin),
):
    db_obj = Offer(**offer_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


