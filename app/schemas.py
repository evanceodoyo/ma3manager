from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, List
from enum import Enum


class UserRole(str, Enum):
    admin = 'admin'
    manager = 'manager'
    driver = 'driver'


class VehicleStatus(str, Enum):
    on_road = 'on road'
    in_garage = 'in garage'
    stalled = 'stalled'


class BaseSchema(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserBase(BaseSchema):
    name: Optional[str]
    email: EmailStr
    role: UserRole
    id_number: str
    dob: Optional[date]
    phone_number: Optional[str]
    driving_license_number: Optional[str]
    location_id: Optional[int]


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    location: Optional['LocationResponse']


class VehicleBase(BaseSchema):
    plate_number: str
    name: Optional[str]
    engine_capacity: str
    buying_value: float
    projected_return_per_day: float
    status: VehicleStatus
    location_id: Optional[int]


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(VehicleBase):
    pass


class VehicleResponse(VehicleBase):
    location: Optional['LocationResponse']


class LocationBase(BaseSchema):
    name: str
    address: Optional[str]


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass


class LocationResponse(LocationBase):
    users: List[UserResponse] = []
    vehicles: List[VehicleResponse] = []


class RouteBase(BaseSchema):
    name: str


class RouteCreate(RouteBase):
    pass


class RouteUpdate(RouteBase):
    pass


class RouteResponse(RouteBase):
    vehicles: List['VehicleRouteResponse'] = []


class VehicleDriverBase(BaseSchema):
    user_id: int
    vehicle_id: int
    start_date: date
    end_date: Optional[date]


class VehicleDriverCreate(VehicleDriverBase):
    pass


class VehicleDriverUpdate(VehicleDriverBase):
    pass


class VehicleDriverResponse(VehicleDriverBase):
    user: Optional[UserResponse]
    vehicle: Optional[VehicleResponse]


class MaintenanceBase(BaseSchema):
    vehicle_id: int
    cost: float
    description: str
    date: date


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceUpdate(MaintenanceBase):
    pass


class MaintenanceResponse(MaintenanceBase):
    vehicle: Optional[VehicleResponse]


class RemittanceBase(BaseSchema):
    vehicle_id: int
    amount: float
    date: date


class RemittanceCreate(RemittanceBase):
    pass


class RemittanceUpdate(RemittanceBase):
    pass


class RemittanceResponse(RemittanceBase):
    vehicle: Optional[VehicleResponse]


class VehicleRouteBase(BaseSchema):
    vehicle_id: int
    route_id: int
    date_assigned: date


class VehicleRouteCreate(VehicleRouteBase):
    pass


class VehicleRouteUpdate(VehicleRouteBase):
    pass


class VehicleRouteResponse(VehicleRouteBase):
    vehicle: Optional[VehicleResponse]
    route: Optional[RouteResponse]
