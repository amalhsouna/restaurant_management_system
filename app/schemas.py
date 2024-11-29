from pydantic import BaseModel

class MenuCreate(BaseModel):
    name: str
    description: str
    price: float

class OrderCreate(BaseModel):
    customer_name: str
    menu_id: int
    quantity: int
