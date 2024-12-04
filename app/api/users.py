from fastapi import APIRouter, Depends
from ..models.users import User
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user_service

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    API route to create a new user.

    - Validates if the user name already exists.
    - If not, it creates a new menuseru.
    """
    return create_user_service(user, db)
