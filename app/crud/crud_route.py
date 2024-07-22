from sqlalchemy.orm import Session
from app.models import Route
from app.schemas import RouteCreate, RouteUpdate


def get_route(db: Session, route_id: int):
    return db.query(Route).filter(Route.id == route_id).first()


def get_routes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Route).offset(skip).limit(limit).all()


def create_route(db: Session, route: RouteCreate):
    db_route = Route(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route


def update_route(db: Session, route: RouteUpdate, route_id: int):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    for key, value in route.dict().items():
        setattr(db_route, key, value)
    db.commit()
    db.refresh(db_route)
    return db_route


def delete_route(db: Session, route_id: int):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    db.delete(db_route)
    db.commit()
    return db_route
