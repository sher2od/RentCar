from typing import List

from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status




from app.models.car import Car

def get_all_cars(db:Session)-> List[Car]:
    cars = db.query(Car).all()
    return cars

def get_one_car(db:Session,car_id:int)-> Car | None:
    car = db.query(Car).filter_by(id = car_id).first()

    if car:
        return car
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bunday car mavjud emas")


def delete_car(db:Session,car_id:int) -> Car | None:
    car = db.query(Car).filter_by(id = car_id).first()

    if car:
        db.delete(car)
        db.commit()

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Car ochirildi")