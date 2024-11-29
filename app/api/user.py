from fastapi import APIRouter
from ..models.user import User
from ..schemas.user import UserCreate

router = APIRouter()

@router.get("/")
async def get_users():
    # Logique pour récupérer tous les utilisateurs
    return {"users": []}

@router.post("/")
async def create_user(user: UserCreate):
    # Logique pour créer un utilisateur
    return {"message": "Utilisateur créé"}
