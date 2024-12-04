from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.order import Order
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter()


@router.get("/", response_model=list[OrderResponse])
async def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders


@router.post("/")
async def create_order(order: OrderCreate):
    return {"message": "Commande créée"}
