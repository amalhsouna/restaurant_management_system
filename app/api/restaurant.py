from fastapi import APIRouter
from ..models.restaurant import Restaurant
from ..schemas.restaurant import RestaurantCreate, RestaurantUpdate

router = APIRouter()

@router.get("/")
async def get_menu():
    # Logique pour récupérer tous les plats
    return {"menu": []}

@router.post("/")
async def add_dish(dish: RestaurantCreate):
    # Logique pour ajouter un plat
    return {"message": "Plat ajouté"}
