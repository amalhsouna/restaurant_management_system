from fastapi import APIRouter
from ..models.order import Order
from ..schemas.order import OrderCreate

router = APIRouter()

@router.get("/")
async def get_orders():
    # Logique pour récupérer toutes les commandes
    return {"orders": []}

@router.post("/")
async def create_order(order: OrderCreate):
    # Logique pour créer une commande
    return {"message": "Commande créée"}
