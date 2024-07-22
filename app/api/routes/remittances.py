from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.RemittanceResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_remittance(
        remittance: schemas.RemittanceCreate,
        db: Session = Depends(get_db)):
    return crud.crud_remittance.create_remittance(db=db, remittance=remittance)


@router.get("/",
            response_model=List[schemas.RemittanceResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_remittances(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    remittances = crud.crud_remittance.get_remittances(
        db, skip=skip, limit=limit)
    return remittances


@router.get("/{remittance_id}",
            response_model=schemas.RemittanceResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_remittance(remittance_id: int, db: Session = Depends(get_db)):
    db_remittance = crud.crud_remittance.get_remittance(
        db, remittance_id=remittance_id)
    if db_remittance is None:
        raise HTTPException(status_code=404, detail="Remittance not found")
    return db_remittance


@router.put("/{remittance_id}",
            response_model=schemas.RemittanceResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_remittance(
        remittance_id: int,
        remittance: schemas.RemittanceUpdate,
        db: Session = Depends(get_db)):
    db_remittance = crud.crud_remittance.get_remittance(
        db, remittance_id=remittance_id)
    if db_remittance is None:
        raise HTTPException(status_code=404, detail="Remittance not found")
    return crud.crud_remittance.update_remittance(
        db=db, remittance=remittance, remittance_id=remittance_id)


@router.delete("/{remittance_id}",
               response_model=schemas.RemittanceResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_remittance(remittance_id: int, db: Session = Depends(get_db)):
    db_remittance = crud.crud_remittance.get_remittance(
        db, remittance_id=remittance_id)
    if db_remittance is None:
        raise HTTPException(status_code=404, detail="Remittance not found")
    return crud.crud_remittance.delete
