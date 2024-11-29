from fastapi import FastAPI
from .api import restaurant, orders, users

app = FastAPI()

app.include_router(restaurant.router, prefix="/restaurant", tags=["restaurant"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(users.router, prefix="/users", tags=["users"])
