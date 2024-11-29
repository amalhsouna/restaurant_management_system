from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    dish_id = Column(Integer, ForeignKey('restaurants.id'))
    status = Column(String, default='pending')

    user = relationship('User', back_populates='orders')
    dish = relationship('Restaurant')

    def __repr__(self):
        return f"<Order(user_id={self.user_id}, dish_id={self.dish_id}, status={self.status})>"
