from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.VehicleDriverResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_vehicle_driver(
        vehicle_driver: schemas.VehicleDriverCreate,
        db: Session = Depends(get_db)):
    return crud.crud_vehicle_driver.create_vehicle_driver(
        db=db, vehicle_driver=vehicle_driver)


@router.get("/",
            response_model=List[schemas.VehicleDriverResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_vehicle_drivers(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    vehicle_drivers = crud.crud_vehicle_driver.get_vehicle_drivers(
        db, skip=skip, limit=limit)
    return vehicle_drivers


@router.get("/{vehicle_driver_id}",
            response_model=schemas.VehicleDriverResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_vehicle_driver(vehicle_driver_id: int, db: Session = Depends(get_db)):
    db_vehicle_driver = crud.crud_vehicle_driver.get_vehicle_driver(
        db, vehicle_driver_id=vehicle_driver_id)
    if db_vehicle_driver is None:
        raise HTTPException(status_code=404, detail="Vehicle driver not found")
    return db_vehicle_driver


@router.put("/{vehicle_driver_id}",
            response_model=schemas.VehicleDriverResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_vehicle_driver(
        vehicle_driver_id: int,
        vehicle_driver: schemas.VehicleDriverUpdate,
        db: Session = Depends(get_db)):
    db_vehicle_driver = crud.crud_vehicle_driver.get_vehicle_driver(
        db, vehicle_driver_id=vehicle_driver_id)
    if db_vehicle_driver is None:
        raise HTTPException(status_code=404, detail="Vehicle driver not found")
    return crud.crud_vehicle_driver.update_vehicle_driver(
        db=db, vehicle_driver=vehicle_driver, vehicle_driver_id=vehicle_driver_id)


@router.delete("/{vehicle_driver_id}",
               response_model=schemas.VehicleDriverResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_vehicle_driver(
        vehicle_driver_id: int,
        db: Session = Depends(get_db)):
    db_vehicle_driver = crud.crud_vehicle_driver.get_vehicle_driver(
        db, vehicle_driver_id=vehicle_driver_id)
    if db_vehicle_driver is None:
        raise HTTPException(status_code=404, detail="Vehicle driver not found")
    return crud.crud_vehicle_driver.delete_vehicle_driver(
        db=db, vehicle_driver_id=vehicle_driver_id)
