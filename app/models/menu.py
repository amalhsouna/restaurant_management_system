from sqlalchemy import Column, String, Integer
from app.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)




