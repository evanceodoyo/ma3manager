from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime, date
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
    model_config = ConfigDict(from_attributes=True)


class UserCommon(BaseSchema):
    name: Optional[str] = None
    role: Optional[UserRole] = None
    id_number: Optional[str] = None
    dob: Optional[date] = None
    phone_number: Optional[str] = None
    driving_license_number: Optional[str] = None
    location_id: Optional[int] = None


class UserBase(UserCommon):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCommon):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime


class VehicleBase(BaseSchema):
    plate_number: str
    name: Optional[str] = None
    engine_capacity: str
    buying_value: float
    projected_return_per_day: float
    status: VehicleStatus
    location_id: Optional[int]


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(BaseSchema):
    plate_number: Optional[str] = None
    name: Optional[str] = None
    engine_capacity: Optional[str] = None
    buying_value: Optional[float] = None
    projected_return_per_day: Optional[float] = None
    status: Optional[VehicleStatus] = None
    location_id: Optional[int] = None


class VehicleResponse(VehicleBase):
    location: Optional['LocationResponse'] = None
    id: int
    created_at: datetime
    updated_at: datetime


class LocationBase(BaseSchema):
    name: str
    address: Optional[str] = None


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseSchema):
    name: Optional[str] = None
    address: Optional[str] = None


class LocationResponse(LocationBase):
    id: int
    created_at: datetime
    updated_at: datetime


class RouteBase(BaseSchema):
    name: str


class RouteCreate(RouteBase):
    pass


class RouteUpdate(BaseSchema):
    name: Optional[str] = None


class RouteResponse(RouteBase):
    vehicles: List['VehicleRouteResponse'] = []
    id: int
    created_at: datetime
    updated_at: datetime


class VehicleDriverBase(BaseSchema):
    user_id: int
    vehicle_id: int
    start_date: datetime
    end_date: Optional[datetime] = None


class VehicleDriverCreate(VehicleDriverBase):
    pass


class VehicleDriverUpdate(BaseSchema):
    user_id: Optional[int] = None
    vehicle_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class VehicleDriverResponse(VehicleDriverBase):
    user: Optional[UserResponse] = None
    vehicle: Optional[VehicleResponse] = None
    id: int
    created_at: datetime
    updated_at: datetime


class MaintenanceBase(BaseSchema):
    vehicle_id: int
    cost: float
    description: str
    done_at: datetime


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceUpdate(BaseSchema):
    vehicle_id: Optional[int] = None
    cost: Optional[float] = None
    description: Optional[str] = None
    done_at: Optional[datetime] = None


class MaintenanceResponse(MaintenanceBase):
    vehicle: Optional[VehicleResponse] = None
    id: int
    created_at: datetime
    updated_at: datetime


class RemittanceBase(BaseSchema):
    vehicle_id: int
    amount: float
    remitted_at: datetime


class RemittanceCreate(RemittanceBase):
    pass


class RemittanceUpdate(BaseSchema):
    vehicle_id: Optional[int] = None
    amount: Optional[float] = None
    remitted_at: Optional[datetime] = None


class RemittanceResponse(RemittanceBase):
    vehicle: Optional[VehicleResponse] = None
    id: int
    created_at: datetime
    updated_at: datetime


class VehicleRouteBase(BaseSchema):
    vehicle_id: int
    route_id: int
    date_assigned: datetime


class VehicleRouteCreate(VehicleRouteBase):
    pass


class VehicleRouteUpdate(BaseSchema):
    vehicle_id: Optional[int] = None
    route_id: Optional[int] = None
    date_assigned: Optional[datetime] = None


class VehicleRouteResponse(VehicleRouteBase):
    id: int
    created_at: datetime
    updated_at: datetime
