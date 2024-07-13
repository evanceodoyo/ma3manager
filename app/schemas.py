from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DriverBase(BaseModel):
    name: str
    id_number: str
    dob: date
    phone_number: str


class DriverCreate(DriverBase):
    pass


class DriverUpdate(DriverBase):
    pass


class Driver(DriverBase, BaseSchema):
    location_id: int


class LocationBase(BaseModel):
    name: str
    address: str


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass


class Location(LocationBase, BaseSchema):
    pass


class MaintenanceBase(BaseModel):
    vehicle_id: int
    cost: float
    description: str
    date: date


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceUpdate(MaintenanceBase):
    pass


class Maintenance(MaintenanceBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True


class RemittanceBase(BaseModel):
    vehicle_id: int
    amount: float
    date: date


class RemittanceCreate(RemittanceBase):
    pass


class RemittanceUpdate(RemittanceBase):
    pass


class Remittance(RemittanceBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True


class MonthlyReport(BaseModel):
    year: int
    month: int
    total_earnings: float
    total_expenses: float


class RouteBase(BaseModel):
    name: str


class RouteCreate(RouteBase):
    pass


class RouteUpdate(RouteBase):
    pass


class Route(RouteBase, BaseSchema):
    pass


class VehicleBase(BaseModel):
    plate_number: str
    name: str
    engine_capacity: str
    buying_value: float
    projected_return_per_day: float
    status: str


class VehicleCreate(VehicleBase):
    location_id: int


class VehicleUpdate(VehicleBase):
    location_id: Optional[int] = None


class Vehicle(VehicleBase, BaseSchema):
    location_id: int


class VehicleDriverBase(BaseModel):
    driver_id: int
    start_date: date
    end_date: Optional[date] = None


class VehicleDriverCreate(VehicleDriverBase):
    vehicle_id: int


class VehicleDriverUpdate(VehicleDriverBase):
    vehicle_id: Optional[int] = None


class VehicleDriver(VehicleDriverBase, BaseSchema):
    vehicle_id: int


class VehicleRouteBase(BaseModel):
    vehicle_id: int
    route_id: int
    date_assigned: date


class VehicleRouteCreate(VehicleRouteBase):
    pass


class VehicleRouteUpdate(VehicleRouteBase):
    pass


class VehicleRoute(VehicleRouteBase, BaseSchema):
    pass
