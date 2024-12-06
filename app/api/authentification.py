from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.auth import create_access_token, decode_access_token
from app.models.users import User
from app.schemas.token import Token, TokenData
from bcrypt import checkpw
from fastapi.security import OAuth2PasswordBearer
import logging

router = APIRouter()


# Schéma pour le login
class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/token", response_model=Token)
async def login_for_access_token(
    login_data: LoginRequest, db: Session = Depends(get_db)
):
    # Recherche de l'utilisateur dans la base de données
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Vérification du mot de passe haché
    if not checkpw(login_data.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Création du token JWT
    access_token = create_access_token(data={"sub": user.username})
    logging.debug(f"Access token created for user: {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}


# Dépendance pour vérifier le token JWT
def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token")),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return TokenData(username=user.username)


# Route protégée
@router.get("/protected")
async def protected_route(current_user: TokenData = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}, this is a protected route!"}
