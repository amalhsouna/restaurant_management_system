from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.order import Order
from app.schemas.order import OrderCreate
from app.models.users import User
from app.models.menu import Menu


def create_order_service(order: OrderCreate, db: Session) -> Order:
    try:
        user = db.query(User).filter(User.id == 1).first()  #
        menu = db.query(Menu).filter(Menu.id == 1).first()  #

        if not user:
            raise ValueError("User does not exisit.")
        if not menu:
            raise ValueError("Menu does not exisit.")

        # Create and save a new order
        new_order = Order(user_id=user.id, menu_id=menu.id, status="pending")
        print(new_order)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except Exception as e:
        db.rollback()
        print(f"Erreur lors de la création de l'ordre : {e}")
    finally:
        db.close()
