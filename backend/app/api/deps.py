from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose import JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.config import settings
from app.schemas.token import TokenPayload
from app.models.user import User
from app.models.user import UserRole

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
        token:str = Depends(oauth2_schema),
        db: Session = Depends(get_db)
    ) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = payload.get("sub")
        if token_data is None:
            raise HTTPException(
                status_code=status.HTTP_01_UNAUTHORIZED,
                detail="Impossible de valider les identifiants"
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide ou expire",
        )
    user = db.query(User).filter(User.id == token_data).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # verifier si le user est actif
    if  not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User suspendu ou inactif",
        )
    return user


def get_current_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Reserved Only Admin")
    return current_user


def enforce_owner(resource_id: int, current_user: User = Depends(get_current_user)):
    """
    Bloque l'acces si l'utilisateur n'est pas admin,
    et que la ressource ne lui appartient pas.
    """
    print(f"current user id {current_user.role}")
    if current_user.role == UserRole.ADMIN:
        return
    if current_user.transporter_id != resource_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acces Ressource non autorise"
        )

