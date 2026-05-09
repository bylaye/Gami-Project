from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    """
    Classe de base pour tous les modèles SQLAlchemy.
    Elle hérite de DeclarativeBase (nouveauté SQLAlchemy 2.0).
    """
    id: Any
    __name__: str

    # Génère automatiquement le nom de la table à partir du nom de la classe
    # Exemple: class User -> __tablename__ = "user"
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
