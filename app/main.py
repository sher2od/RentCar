from fastapi import FastAPI
from app.db import inital_db

app = FastAPI(title="Rent Car Api")

inital_db()