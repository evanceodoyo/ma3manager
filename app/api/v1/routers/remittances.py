from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Remittance])
def read_remittances(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(
        deps.get_db)):
    remittances = crud.remittance.get_remittances(db, skip=skip, limit=limit)
    return remittances


@router.post("/", response_model=schemas.Remittance)
def create_remittance(
    remittance: schemas.RemittanceCreate,
    db: Session = Depends(
        deps.get_db)):
    return crud.remittance.create_remittance(db=db, remittance=remittance)


@router.put("/{remittance_id}", response_model=schemas.Remittance)
def update_remittance(
    remittance_id: int,
    remittance: schemas.RemittanceUpdate,
    db: Session = Depends(
        deps.get_db)):
    db_remittance = crud.remittance.get_remittance(db, remittance_id)
    if db_remittance is None:
        raise HTTPException(status_code=404, detail="Remittance not found")
    return crud.remittance.update_remittance(
        db=db, remittance_id=remittance_id, remittance=remittance)


@router.delete("/{remittance_id}", response_model=schemas.Remittance)
def delete_remittance(remittance_id: int, db: Session = Depends(deps.get_db)):
    db_remittance = crud.remittance.get_remittance(db, remittance_id)
    if db_remittance is None:
        raise HTTPException(status_code=404, detail="Remittance not found")
    return crud.remittance.delete_remittance(
        db=db, remittance_id=remittance_id)
