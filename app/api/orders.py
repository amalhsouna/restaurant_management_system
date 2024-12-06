from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.order import Order
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import create_order_service

router = APIRouter()


@router.get("/", response_model=list[OrderResponse])
async def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders


@router.post("/")
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """
    API route to create a new order.

    - Validates if the order name already exists.
    - If not, it creates a new menu.
    """
    return create_order_service(order, db)
