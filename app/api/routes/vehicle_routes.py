from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.crud import crud_vehicle_route
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.VehicleRouteResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_vehicle_route(
        vehicle_route: schemas.VehicleRouteCreate,
        db: Session = Depends(get_db)):
    return crud_vehicle_route.create_vehicle_route(
        db=db, vehicle_route=vehicle_route)


@router.get("/",
            response_model=List[schemas.VehicleRouteResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_vehicle_routes(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    vehicle_routes = crud_vehicle_route.get_vehicle_routes(
        db, skip=skip, limit=limit)
    return vehicle_routes


@router.get("/{vehicle_route_id}",
            response_model=schemas.VehicleRouteResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_vehicle_route(vehicle_route_id: int, db: Session = Depends(get_db)):
    db_vehicle_route = crud_vehicle_route.get_vehicle_route(
        db, vehicle_route_id=vehicle_route_id)
    if db_vehicle_route is None:
        raise HTTPException(status_code=404, detail="Vehicle route not found")
    return db_vehicle_route


@router.put("/{vehicle_route_id}",
            response_model=schemas.VehicleRouteResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_vehicle_route(
        vehicle_route_id: int,
        vehicle_route: schemas.VehicleRouteUpdate,
        db: Session = Depends(get_db)):
    db_vehicle_route = crud_vehicle_route.get_vehicle_route(
        db, vehicle_route_id=vehicle_route_id)
    if db_vehicle_route is None:
        raise HTTPException(status_code=404, detail="Vehicle route not found")
    return crud_vehicle_route.update_vehicle_route(
        db=db, vehicle_route=vehicle_route, vehicle_route_id=vehicle_route_id)


@router.delete("/{vehicle_route_id}",
               response_model=schemas.VehicleRouteResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_vehicle_route(vehicle_route_id: int, db: Session = Depends(get_db)):
    db_vehicle_route = crud_vehicle_route.get_vehicle_route(
        db, vehicle_route_id=vehicle_route_id)
    if db_vehicle_route is None:
        raise HTTPException(status_code=404, detail="Vehicle route not found")
    return crud_vehicle_route.delete_vehicle_route(
        db=db, vehicle_route_id=vehicle_route_id)
