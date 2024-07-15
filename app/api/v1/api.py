from fastapi import APIRouter
from app.api.v1.routers import drivers, locations, maintenances, remittances, routes, vehicles, vehicle_drivers, vehicle_routes, auth

api_router = APIRouter()
api_router.include_router(drivers.router, prefix="/drivers", tags=["drivers"])
api_router.include_router(
    locations.router,
    prefix="/locations",
    tags=["locations"])
api_router.include_router(
    maintenances.router,
    prefix="/maintenances",
    tags=["maintenances"])
api_router.include_router(
    remittances.router,
    prefix="/remittances",
    tags=["remittances"])
api_router.include_router(routes.router, prefix="/routes", tags=["routes"])
api_router.include_router(
    vehicles.router,
    prefix="/vehicles",
    tags=["vehicles"])
api_router.include_router(
    vehicle_drivers.router,
    prefix="/vehicle_drivers",
    tags=["vehicle_drivers"])
api_router.include_router(
    vehicle_routes.router,
    prefix="/vehicle_routes",
    tags=["vehicle_routes"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
