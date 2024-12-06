from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)

    # Relations
    orders = relationship("Order", back_populates="menu")

    def __repr__(self):
        return f"<Menu(id={self.id}, name={self.name}, description={self.description})>"
