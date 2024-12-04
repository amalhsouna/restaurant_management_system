from fastapi import FastAPI
from app.api import menu, users, orders


app = FastAPI()

app.include_router(menu.router, prefix="/menus", tags=["menu"])
app.include_router(users.router, prefix="/users", tags=["user"])
app.include_router(orders.router, prefix="/orders", tags=["order"])
