from sqlalchemy.orm import Session
from app.models import Maintenance
from app.schemas import MaintenanceCreate, MaintenanceUpdate
from typing import List
from datetime import date


def get_maintenance(db: Session, maintenance_id: int):
    return db.query(Maintenance).filter(
        Maintenance.id == maintenance_id).first()


def get_maintenances(
        db: Session,
        skip: int = 0,
        limit: int = 10) -> List[Maintenance]:
    return db.query(Maintenance).offset(skip).limit(limit).all()


def create_maintenance(db: Session, maintenance: MaintenanceCreate):
    db_maintenance = Maintenance(**maintenance.dict())
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance


def update_maintenance(
        db: Session,
        maintenance_id: int,
        maintenance: MaintenanceUpdate):
    db_maintenance = get_maintenance(db, maintenance_id)
    if not db_maintenance:
        return None
    for key, value in maintenance.dict(exclude_unset=True).items():
        setattr(db_maintenance, key, value)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance


def delete_maintenance(db: Session, maintenance_id: int):
    db_maintenance = get_maintenance(db, maintenance_id)
    if not db_maintenance:
        return None
    db.delete(db_maintenance)
    db.commit()
    return db_maintenance


def get_total_expenses(db: Session, year: int, month: int) -> float:
    return db.query(Maintenance).filter(
        Maintenance.date.between(
            date(
                year,
                month,
                1),
            date(
                year,
                month + 1,
                1))).sum(
        Maintenance.cost)
