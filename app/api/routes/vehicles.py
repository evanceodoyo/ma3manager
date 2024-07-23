from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.crud import crud_vehicle
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.VehicleResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_vehicle(
        vehicle: schemas.VehicleCreate,
        db: Session = Depends(get_db)):
    return crud_vehicle.create_vehicle(db=db, vehicle=vehicle)


@router.get("/",
            response_model=List[schemas.VehicleResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_vehicles(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    vehicles = crud_vehicle.get_vehicles(db, skip=skip, limit=limit)
    return vehicles


@router.get("/{vehicle_id}",
            response_model=schemas.VehicleResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud_vehicle.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle


@router.put("/{vehicle_id}",
            response_model=schemas.VehicleResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_vehicle(
        vehicle_id: int,
        vehicle: schemas.VehicleUpdate,
        db: Session = Depends(get_db)):
    db_vehicle = crud_vehicle.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud_vehicle.update_vehicle(
        db=db, vehicle=vehicle, vehicle_id=vehicle_id)


@router.delete("/{vehicle_id}",
               response_model=schemas.VehicleResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud_vehicle.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud_vehicle.delete_vehicle(db=db, vehicle_id=vehicle_id)
