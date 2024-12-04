from fastapi import APIRouter, Depends
from ..models.users import User
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/")
async def create_user(user: UserCreate):
    return {"message": "User created ! "}
