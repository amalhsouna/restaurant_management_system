from pydantic import BaseModel


class OrderResponse(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    user_id: int
    menu_id: int
    status: str

    class Config:
        from_attributes = True
