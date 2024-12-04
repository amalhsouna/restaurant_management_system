from fastapi import FastAPI
from app.api import menu, users


app = FastAPI()

app.include_router(menu.router, prefix="/menu", tags=["menu"])
app.include_router(users.router, prefix="/user", tags=["user"])
