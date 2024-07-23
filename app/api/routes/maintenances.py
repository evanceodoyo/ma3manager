from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.crud import crud_maintenance
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.MaintenanceResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_maintenance(
        maintenance: schemas.MaintenanceCreate,
        db: Session = Depends(get_db)):
    return crud_maintenance.create_maintenance(
        db=db, maintenance=maintenance)


@router.get("/",
            response_model=List[schemas.MaintenanceResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_maintenances(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    maintenances = crud_maintenance.get_maintenances(
        db, skip=skip, limit=limit)
    return maintenances


@router.get("/{maintenance_id}",
            response_model=schemas.MaintenanceResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    db_maintenance = crud_maintenance.get_maintenance(
        db, maintenance_id=maintenance_id)
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return db_maintenance


@router.put("/{maintenance_id}",
            response_model=schemas.MaintenanceResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_maintenance(
        maintenance_id: int,
        maintenance: schemas.MaintenanceUpdate,
        db: Session = Depends(get_db)):
    db_maintenance = crud_maintenance.get_maintenance(
        db, maintenance_id=maintenance_id)
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return crud_maintenance.update_maintenance(
        db=db, maintenance=maintenance, maintenance_id=maintenance_id)


@router.delete("/{maintenance_id}",
               response_model=schemas.MaintenanceResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    db_maintenance = crud_maintenance.get_maintenance(
        db, maintenance_id=maintenance_id)
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return crud_maintenance.delete_maintenance(
        db=db, maintenance_id=maintenance_id)
