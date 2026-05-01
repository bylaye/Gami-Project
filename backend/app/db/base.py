# app/db/base.py

# Import de la classe de base
from app.db.base_class import Base  # noqa

# Import de tous les modèles pour qu'ils soient enregistrés par SQLAlchemy
from app.models.offer_element import OfferGroup # noqa
from app.models.offer_element import OfferStatus  # noqa
from app.models.offer_element import OfferGoodsType  # noqa
from app.models.offer_element import Company  # noqa
from app.models.truck_element import TruckType, TruckStatus  # noqa
from app.models.transporter import Transporter  # noqa
from app.models.truck import Truck  # noqa
from app.models.offer import Offer  # noqa
from app.models.loading_offer_truck import LoadingOfferTruck  # noqa

