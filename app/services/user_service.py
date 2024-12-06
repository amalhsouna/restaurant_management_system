from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.users import User
from app.schemas.user import UserCreate


def create_user_service(user: UserCreate, db: Session) -> User:
    # Check if a user with the same username already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="User with this username already exists."
        )

    # Create and save a new user
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
