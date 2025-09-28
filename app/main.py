from fastapi import FastAPI

from app.db import inital_db
from app.routers.users import router as user_router

app = FastAPI(title="Rent Car Api")

inital_db()
app.include_router(user_router)