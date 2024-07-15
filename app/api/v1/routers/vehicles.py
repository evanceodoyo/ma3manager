from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Vehicle])
def read_vehicles(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(
        deps.get_db)):
    vehicles = crud.vehicle.get_vehicles(db, skip=skip, limit=limit)
    return vehicles


@router.post("/", response_model=schemas.Vehicle)
def create_vehicle(
    vehicle: schemas.VehicleCreate,
    db: Session = Depends(
        deps.get_db)):
    return crud.vehicle.create_vehicle(db=db, vehicle=vehicle)


@router.put("/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(
    vehicle_id: int,
    vehicle: schemas.VehicleUpdate,
    db: Session = Depends(
        deps.get_db)):
    db_vehicle = crud.vehicle.get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud.vehicle.update_vehicle(
        db=db, vehicle_id=vehicle_id, vehicle=vehicle)


@router.delete("/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(deps.get_db)):
    db_vehicle = crud.vehicle.get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud.vehicle.delete_vehicle(db=db, vehicle_id=vehicle_id)
