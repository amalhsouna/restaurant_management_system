from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"))
    status = Column(String, default="pending")

    # Relations
    user = relationship("User", back_populates="orders")
    menu = relationship("Menu", back_populates="orders")

    def __repr__(self):
        return f"<Order(user_id={self.user_id}, menu_id={self.menu_id}, status={self.status})>"
