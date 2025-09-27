from app.db.database import Base,engine
from app.models.user import User

def inital_db():
    Base.metadata.create_all(engine)