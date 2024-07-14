from sqlalchemy.orm import Session
from app.models import Driver
from app.schemas import DriverCreate, DriverUpdate


def get_driver(db: Session, driver_id: int):
    return db.query(Driver).filter(Driver.id == driver_id).first()


def get_drivers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Driver).offset(skip).limit(limit).all()


def create_driver(db: Session, driver: DriverCreate):
    db_driver = Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def update_driver(db: Session, driver_id: int, driver: DriverUpdate):
    db_driver = get_driver(db, driver_id)
    if not db_driver:
        return None
    for key, value in driver.dict(exclude_unset=True).items():
        setattr(db_driver, key, value)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def delete_driver(db: Session, driver_id: int):
    db_driver = get_driver(db, driver_id)
    if not db_driver:
        return None
    db.delete(db_driver)
    db.commit()
    return db_driver
