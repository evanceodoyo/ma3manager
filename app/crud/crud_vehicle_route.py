from sqlalchemy.orm import Session
from app.models import VehicleRoute
from app.schemas import VehicleRouteCreate, VehicleRouteUpdate


def get_vehicle_route(db: Session, vehicle_route_id: int):
    return db.query(VehicleRoute).filter(
        VehicleRoute.id == vehicle_route_id).first()


def get_vehicle_routes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(VehicleRoute).offset(skip).limit(limit).all()


def create_vehicle_route(db: Session, vehicle_route: VehicleRouteCreate):
    db_vehicle_route = VehicleRoute(**vehicle_route.model_dump())
    db.add(db_vehicle_route)
    db.commit()
    db.refresh(db_vehicle_route)
    return db_vehicle_route


def update_vehicle_route(
        db: Session,
        vehicle_route: VehicleRouteUpdate,
        vehicle_route_id: int):
    db_vehicle_route = db.query(VehicleRoute).filter(
        VehicleRoute.id == vehicle_route_id).first()
    for key, value in vehicle_route.model_dump(exclude_unset=True).items():
        setattr(db_vehicle_route, key, value)
    db.commit()
    db.refresh(db_vehicle_route)
    return db_vehicle_route


def delete_vehicle_route(db: Session, vehicle_route_id: int):
    db_vehicle_route = db.query(VehicleRoute).filter(
        VehicleRoute.id == vehicle_route_id).first()
    db.delete(db_vehicle_route)
    db.commit()
    return db_vehicle_route
