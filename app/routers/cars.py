from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends,HTTPException,Path
from sqlalchemy.orm import Session

from app.schemas.car import CarResponse,CarsResponse,CarCreate,CarUpdate
from app.dependencies import get_db
from app.services.car_service import get_all_cars,get_one_car,delete_car
from app.models.car import Car

router = APIRouter(
    prefix='/cars',
    tags=['Cars Endpoints']
)

# TODO Barcha carlarni chiqqarib berish
@router.get('/',response_model=CarsResponse)
async def get_cars(db: Annotated[Session, Depends(get_db)]):
    return CarsResponse(cars=get_all_cars(db))
    

# TODO 1 ta carni chiqarish
@router.get('/{car_id}',response_model=CarResponse)
async def get_one_cars(car_id:Annotated[int,Path(gt=0)], db:Annotated[Session,Depends(get_db)]):
    return get_one_car(db,car_id)



@router.post('/',response_model=CarResponse)
async def add_car(car_data:CarCreate,db:Annotated[Session,Depends(get_db)]):
    new_car = Car(
        model=car_data.model,
        brand=car_data.brand,
        price=car_data.price,
        engine_type=car_data.engine_type,
        doors=car_data.doors,
        fuel_type=car_data.fuel_type,
        air_condition=car_data.air_condition,
        shape_type=car_data.shape_type,
        distance=car_data.distance,
        is_available=car_data.is_available
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return CarResponse(
        id=new_car.id,
        model=new_car.model,
        brand=new_car.brand,
        price=new_car.price,
        engine_type=new_car.engine_type,
        doors=new_car.doors,
        fuel_type=new_car.fuel_type,
        air_condition=new_car.air_condition,
        shape_type=new_car.shape_type,
        distance=new_car.distance,
        is_available=new_car.is_available,
        images=[img.url for img in new_car.images],
        equipments=[eq.name for eq in new_car.equipments],
    )


@router.delete('{car_id}')
async def delete_cars(car_id:int,db:Annotated[Session,Depends(get_db)]):
    delete_car(db,car_id)
  