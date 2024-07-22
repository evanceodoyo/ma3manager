from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.deps import auth
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.RouteResponse,
             dependencies=[Depends(auth.admin_or_manager)])
def create_route(route: schemas.RouteCreate, db: Session = Depends(get_db)):
    return crud.crud_route.create_route(db=db, route=route)


@router.get("/",
            response_model=List[schemas.RouteResponse],
            dependencies=[Depends(auth.admin_or_manager)])
def read_routes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    routes = crud.crud_route.get_routes(db, skip=skip, limit=limit)
    return routes


@router.get("/{route_id}", response_model=schemas.RouteResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def read_route(route_id: int, db: Session = Depends(get_db)):
    db_route = crud.crud_route.get_route(db, route_id=route_id)
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return db_route


@router.put("/{route_id}", response_model=schemas.RouteResponse,
            dependencies=[Depends(auth.admin_or_manager)])
def update_route(
        route_id: int,
        route: schemas.RouteUpdate,
        db: Session = Depends(get_db)):
    db_route = crud.crud_route.get_route(db, route_id=route_id)
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return crud.crud_route.update_route(db=db, route=route, route_id=route_id)


@router.delete("/{route_id}",
               response_model=schemas.RouteResponse,
               dependencies=[Depends(auth.admin_or_manager)])
def delete_route(route_id: int, db: Session = Depends(get_db)):
    db_route = crud.crud_route.get_route(db, route_id=route_id)
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return crud.crud_route.delete_route(db=db, route_id=route_id)
