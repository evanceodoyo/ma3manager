from sqlalchemy.orm import Session
from app.models import Vehicle
from app.schemas import VehicleCreate, VehicleUpdate
from typing import List


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()


def get_vehicles(db: Session, skip: int = 0, limit: int = 10) -> List[Vehicle]:
    return db.query(Vehicle).offset(skip).limit(limit).all()


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def update_vehicle(db: Session, vehicle_id: int, vehicle: VehicleUpdate):
    db_vehicle = get_vehicle(db, vehicle_id)
    if not db_vehicle:
        return None
    for key, value in vehicle.dict(exclude_unset=True).items():
        setattr(db_vehicle, key, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = get_vehicle(db, vehicle_id)
    if not db_vehicle:
        return None
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle
