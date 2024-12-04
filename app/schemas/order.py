from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    dish_id: int
    status: str

    class Config:
        from_attributes = True
