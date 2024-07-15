from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional


class TimestampMixin(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str = Field(..., max_length=50)
    email: EmailStr
    role: str
    id_number: str = Field(..., max_length=20)
    dob: Optional[date] = None
    phone_number: Optional[str] = Field(None, max_length=15)
    driving_license_number: Optional[str] = Field(None, max_length=20)
    location_id: int


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=8)


class User(TimestampMixin, UserBase):
    pass


class VehicleBase(BaseModel):
    location_id: int
    plate_number: str = Field(..., max_length=10)
    name: Optional[str] = Field(None, max_length=50)
    engine_capacity: str = Field(..., max_length=20)
    buying_value: float
    projected_return_per_day: float
    status: str


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(VehicleBase):
    pass


class Vehicle(TimestampMixin, VehicleBase):
    pass


class LocationBase(BaseModel):
    name: str = Field(..., max_length=50)
    address: Optional[str] = Field(None, max_length=100)


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass


class Location(TimestampMixin, LocationBase):
    pass


class RouteBase(BaseModel):
    name: str = Field(..., max_length=50)


class RouteCreate(RouteBase):
    pass


class RouteUpdate(RouteBase):
    pass


class Route(TimestampMixin, RouteBase):
    pass


class VehicleDriverBase(BaseModel):
    user_id: int
    vehicle_id: int
    start_date: date
    end_date: Optional[date] = None


class VehicleDriverCreate(VehicleDriverBase):
    pass


class VehicleDriverUpdate(VehicleDriverBase):
    pass


class VehicleDriver(TimestampMixin, VehicleDriverBase):
    pass


class MaintenanceBase(BaseModel):
    vehicle_id: int
    cost: float
    description: str = Field(..., max_length=255)
    date: date


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceUpdate(MaintenanceBase):
    pass


class Maintenance(TimestampMixin, MaintenanceBase):
    pass


class RemittanceBase(BaseModel):
    vehicle_id: int
    amount: float


class RemittanceCreate(RemittanceBase):
    pass


class RemittanceUpdate(RemittanceBase):
    pass


class Remittance(TimestampMixin, RemittanceBase):
    pass


class VehicleRouteBase(BaseModel):
    vehicle_id: int
    route_id: int
    date_assigned: date


class VehicleRouteCreate(VehicleRouteBase):
    pass


class VehicleRouteUpdate(VehicleRouteBase):
    pass


class VehicleRoute(TimestampMixin, VehicleRouteBase):
    pass
