from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.menu import Menu
from app.schemas.menu import MenuResponse, MenuCreate
from app.services.menu_service import create_menu_service

router = APIRouter()

@router.get("/", response_model=list[MenuResponse])
async def get_menus(db: Session = Depends(get_db)):
    menus = db.query(Menu).all()
    return menus

@router.post("/", response_model=MenuResponse)
async def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    """
    API route to create a new menu.

    - Validates if the menu name already exists.
    - If not, it creates a new menu.
    """
    return create_menu_service(menu, db)