from app.db.database import Base,engine
from app.models.user import User
from app.models.car import Car,Image,Equipment

def inital_db():
    Base.metadata.create_all(engine)