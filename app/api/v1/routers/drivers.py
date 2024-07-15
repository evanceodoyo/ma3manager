from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Driver])
def read_drivers(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(
        deps.get_db)):
    drivers = crud.driver.get_drivers(db, skip=skip, limit=limit)
    return drivers


@router.post("/", response_model=schemas.Driver)
def create_driver(
    driver: schemas.DriverCreate,
    db: Session = Depends(
        deps.get_db)):
    return crud.driver.create_driver(db=db, driver=driver)


@router.put("/{driver_id}", response_model=schemas.Driver)
def update_driver(
    driver_id: int,
    driver: schemas.DriverUpdate,
    db: Session = Depends(
        deps.get_db)):
    db_driver = crud.driver.get_driver(db, driver_id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return crud.driver.update_driver(db=db, driver_id=driver_id, driver=driver)


@router.delete("/{driver_id}", response_model=schemas.Driver)
def delete_driver(driver_id: int, db: Session = Depends(deps.get_db)):
    db_driver = crud.driver.get_driver(db, driver_id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return crud.driver.delete_driver(db=db, driver_id=driver_id)
