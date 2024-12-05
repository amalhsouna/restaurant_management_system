from pydantic import BaseModel, EmailStr


# schema to validate user
class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


# add id to get user
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    hashed_password: str
