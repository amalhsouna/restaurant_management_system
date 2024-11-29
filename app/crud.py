from sqlalchemy.orm import Session
from app import schemas
from app.models import order

def get_menu(db: Session, menu_id: int):
    return db.query(order.Menu).filter(order.Menu.id == menu_id).first()

def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = order.Menu(name=menu.name, description=menu.description, price=menu.price)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu
