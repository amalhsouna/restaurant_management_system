from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.menu import Menu
from app.schemas.menu import MenuCreate


def create_menu_service(menu: MenuCreate, db: Session) -> Menu:
    # Check if a menu with the same name already exists
    existing_menu = db.query(Menu).filter(Menu.name == menu.name).first()
    if existing_menu:
        raise HTTPException(
            status_code=400, detail="Menu with this name already exists."
        )

    # Create and save a new menu
    new_menu = Menu(
        name=menu.name,
        description=menu.description,
    )
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu
