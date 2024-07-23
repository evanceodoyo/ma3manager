from sqlalchemy.orm import Session, joinedload
from app.models import Vehicle
from app.schemas import VehicleCreate, VehicleUpdate


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(Vehicle).options(joinedload(Vehicle.location)).filter(
        Vehicle.id == vehicle_id).first()


def get_vehicles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Vehicle).offset(skip).limit(limit).all()


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(**vehicle.model_dump())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def update_vehicle(db: Session, vehicle: VehicleUpdate, vehicle_id: int):
    db_vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    for key, value in vehicle.model_dump(exclude_unset=True).items():
        setattr(db_vehicle, key, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle
