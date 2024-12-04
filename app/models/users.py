from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
