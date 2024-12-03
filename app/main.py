from fastapi import FastAPI
from app.api import menu

print('fffffffffffff')

app = FastAPI()

app.include_router(menu.router, prefix="/menu", tags=["menu"])

