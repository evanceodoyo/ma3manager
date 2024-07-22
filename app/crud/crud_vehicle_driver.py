from sqlalchemy.orm import Session
from app.models import VehicleDriver
from app.schemas import VehicleDriverCreate, VehicleDriverUpdate


def get_vehicle_driver(db: Session, vehicle_driver_id: int):
    return db.query(VehicleDriver).filter(
        VehicleDriver.id == vehicle_driver_id).first()


def get_vehicle_drivers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(VehicleDriver).offset(skip).limit(limit).all()


def create_vehicle_driver(db: Session, vehicle_driver: VehicleDriverCreate):
    db_vehicle_driver = VehicleDriver(**vehicle_driver.model_dump())
    db.add(db_vehicle_driver)
    db.commit()
    db.refresh(db_vehicle_driver)
    return db_vehicle_driver


def update_vehicle_driver(
        db: Session,
        vehicle_driver: VehicleDriverUpdate,
        vehicle_driver_id: int):
    db_vehicle_driver = db.query(VehicleDriver).filter(
        VehicleDriver.id == vehicle_driver_id).first()
    for key, value in vehicle_driver.model_dump(exclude_unset=True).items():
        setattr(db_vehicle_driver, key, value)
    db.commit()
    db.refresh(db_vehicle_driver)
    return db_vehicle_driver


def delete_vehicle_driver(db: Session, vehicle_driver_id: int):
    db_vehicle_driver = db.query(VehicleDriver).filter(
        VehicleDriver.id == vehicle_driver_id).first()
    db.delete(db_vehicle_driver)
    db.commit()
    return db_vehicle_driver
