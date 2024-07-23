from sqlalchemy.orm import Session, joinedload
from app.models import Maintenance
from app.schemas import MaintenanceCreate, MaintenanceUpdate


def get_maintenance(db: Session, maintenance_id: int):
    return db.query(Maintenance).options(
        joinedload(
            Maintenance.vehicle)).filter(
        Maintenance.id == maintenance_id).first()


def get_maintenances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Maintenance).offset(skip).limit(limit).all()


def create_maintenance(db: Session, maintenance: MaintenanceCreate):
    db_maintenance = Maintenance(**maintenance.model_dump())
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance


def update_maintenance(
        db: Session,
        maintenance: MaintenanceUpdate,
        maintenance_id: int):
    db_maintenance = db.query(Maintenance).filter(
        Maintenance.id == maintenance_id).first()
    for key, value in maintenance.model_dump(exclude_unset=True).items():
        setattr(db_maintenance, key, value)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance


def delete_maintenance(db: Session, maintenance_id: int):
    db_maintenance = db.query(Maintenance).filter(
        Maintenance.id == maintenance_id).first()
    db.delete(db_maintenance)
    db.commit()
    return db_maintenance
