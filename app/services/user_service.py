from random import randint

from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status




from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.password import get_hash_password


def create_user(db:Session,user:UserCreate) -> User:
    if db.query(User).filter_by(email=user.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="this is aloready exists")
    
    verification_code = randint(1000,9999)

    new_user = User(
        email=user.email,
        hash_password=get_hash_password(user.password),
        name=user.name, 
        phone=user.phone,
        verification_code = verification_code
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user