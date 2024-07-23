from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.crud import crud_location
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.LocationResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_location(
        location: schemas.LocationCreate,
        db: Session = Depends(get_db)):
    return crud_location.create_location(db=db, location=location)


@router.get("/",
            response_model=List[schemas.LocationResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_locations(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    locations = crud_location.get_locations(db, skip=skip, limit=limit)
    return locations


@router.get("/{location_id}",
            response_model=schemas.LocationResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud_location.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.put("/{location_id}",
            response_model=schemas.LocationResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_location(
        location_id: int,
        location: schemas.LocationUpdate,
        db: Session = Depends(get_db)):
    db_location = crud_location.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return crud_location.update_location(
        db=db, location=location, location_id=location_id)


@router.delete("/{location_id}",
               response_model=schemas.LocationResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud_location.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return crud_location.delete_location(db=db, location_id=location_id)
