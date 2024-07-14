from sqlalchemy.orm import Session
from app.models import Remittance
from app.schemas import RemittanceCreate, RemittanceUpdate
from typing import List
from datetime import date


def get_remittance(db: Session, remittance_id: int):
    return db.query(Remittance).filter(Remittance.id == remittance_id).first()


def get_remittances(
        db: Session,
        skip: int = 0,
        limit: int = 10) -> List[Remittance]:
    return db.query(Remittance).offset(skip).limit(limit).all()


def create_remittance(db: Session, remittance: RemittanceCreate):
    db_remittance = Remittance(**remittance.dict())
    db.add(db_remittance)
    db.commit()
    db.refresh(db_remittance)
    return db_remittance


def update_remittance(
        db: Session,
        remittance_id: int,
        remittance: RemittanceUpdate):
    db_remittance = get_remittance(db, remittance_id)
    if not db_remittance:
        return None
    for key, value in remittance.dict(exclude_unset=True).items():
        setattr(db_remittance, key, value)
    db.commit()
    db.refresh(db_remittance)
    return db_remittance


def delete_remittance(db: Session, remittance_id: int):
    db_remittance = get_remittance(db, remittance_id)
    if not db_remittance:
        return None
    db.delete(db_remittance)
    db.commit()
    return db_remittance


def get_total_earnings(db: Session, year: int, month: int) -> float:
    return db.query(Remittance).filter(
        Remittance.date.between(date(year, month, 1), date(year, month + 1, 1))
    ).sum(Remittance.amount)
