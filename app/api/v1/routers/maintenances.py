from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Maintenance])
def read_maintenances(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(
        deps.get_db)):
    maintenances = crud.maintenance.get_maintenances(
        db, skip=skip, limit=limit)
    return maintenances


@router.post("/", response_model=schemas.Maintenance)
def create_maintenance(
    maintenance: schemas.MaintenanceCreate,
    db: Session = Depends(
        deps.get_db)):
    return crud.maintenance.create_maintenance(db=db, maintenance=maintenance)


@router.put("/{maintenance_id}", response_model=schemas.Maintenance)
def update_maintenance(
    maintenance_id: int,
    maintenance: schemas.MaintenanceUpdate,
    db: Session = Depends(
        deps.get_db)):
    db_maintenance = crud.maintenance.get_maintenance(db, maintenance_id)
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return crud.maintenance.update_maintenance(
        db=db, maintenance_id=maintenance_id, maintenance=maintenance)


@router.delete("/{maintenance_id}", response_model=schemas.Maintenance)
def delete_maintenance(
    maintenance_id: int,
    db: Session = Depends(
        deps.get_db)):
    db_maintenance = crud.maintenance.get_maintenance(db, maintenance_id)
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return crud.maintenance.delete_maintenance(
        db=db, maintenance_id=maintenance_id)
