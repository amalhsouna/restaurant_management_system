from fastapi import APIRouter
from ..models.users import User
from ..schemas.user import UserCreate

router = APIRouter()

@router.get("/")
async def get_users():
    return {"users": []}

@router.post("/")
async def create_user(user: UserCreate):
    return {"message": "User created ! "}
