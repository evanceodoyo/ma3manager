from sqlalchemy.orm import Session, joinedload
from app.models import Remittance
from app.schemas import RemittanceCreate, RemittanceUpdate


def get_remittance(db: Session, remittance_id: int):
    return db.query(Remittance).options(
        joinedload(
            Remittance.vehicle)).filter(
        Remittance.id == remittance_id).first()


def get_remittances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Remittance).offset(skip).limit(limit).all()


def create_remittance(db: Session, remittance: RemittanceCreate):
    db_remittance = Remittance(**remittance.model_dump())
    db.add(db_remittance)
    db.commit()
    db.refresh(db_remittance)
    return db_remittance


def update_remittance(
        db: Session,
        remittance: RemittanceUpdate,
        remittance_id: int):
    db_remittance = db.query(Remittance).filter(
        Remittance.id == remittance_id).first()
    for key, value in remittance.model_dump(exclude_unset=True).items():
        setattr(db_remittance, key, value)
    db.commit()
    db.refresh(db_remittance)
    return db_remittance


def delete_remittance(db: Session, remittance_id: int):
    db_remittance = db.query(Remittance).filter(
        Remittance.id == remittance_id).first()
    db.delete(db_remittance)
    db.commit()
    return db_remittance
