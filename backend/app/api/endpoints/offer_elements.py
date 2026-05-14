from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.db.session import get_db
from app.api import deps
from app.models.user import User
from app.models.offer_element import OfferStatus
from app.models.offer_element import OfferGroup
from app.models.offer_element import OfferGoodsType
from app.models.offer_element import Company
from app.schemas.offer_element import OfferStatusCreate
from app.schemas.offer_element import OfferStatusRead
from app.schemas.offer_element import OfferGroupCreate
from app.schemas.offer_element import OfferGroupRead
from app.schemas.offer_element import CompanyCreate
from app.schemas.offer_element import CompanyRead
from app.schemas.offer_element import OfferGoodsCreate
from app.schemas.offer_element import OfferGoodsRead

router = APIRouter()

@router.post("/group/add", response_model=OfferGroupRead)
def add_offer_group(
    offer_group_in: OfferGroupCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_admin),
):
    db_obj = OfferGroup(**offer_group_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.post("/status/add", response_model=OfferStatusRead)
def add_offer_status(
    offer_status_in: OfferStatusCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_admin),
):
    db_obj = OfferStatus(**offer_status_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.post("/type/add", response_model=OfferGoodsRead)
def add_offer_goods_type(
    offer_goods_in: OfferGoodsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_admin),
):
    db_obj = OfferGoodsType(**offer_goods_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.post("/company/add", response_model=CompanyRead)
def add_company(
        company_in: CompanyCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(deps.get_current_admin),
    ):
    db_obj = Company(**company_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/company/get/all", response_model=list[CompanyRead], summary="La liste des compagnies partenaires")
def read_company(
        db: Session = Depends(get_db), 
        current_user: User = Depends(deps.get_current_admin)
    ):
    status = db.query(Company).all()
    return status




