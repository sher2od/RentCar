from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import inital_db
from app.routers.users import router as user_router
from app.routers.cars import router as cars_router

app = FastAPI(
    title="Rent Car Api",
    version = "1.0.0",
    description="API for managing car rentals"
    
    )

inital_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(user_router)
app.include_router(cars_router)