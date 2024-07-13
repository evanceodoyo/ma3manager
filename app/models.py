from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey
from datetime import datetime
from enum import Enum as PyEnum
from app.db.session import Base


class StatusEnum(PyEnum):
    ON_ROAD = "on road"
    IN_GARAGE = "in garage"
    STALLED = "stalled"


class TimestampMixin:
    created_at = Column(Date, default=datetime.now(), nullable=False)
    updated_at = Column(
        Date,
        default=datetime.now(),
        nullable=False,
        onupdate=datetime.now())


class Driver(Base, TimestampMixin):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    id_number = Column(String(10), unique=True)
    dob = Column(Date)
    phone_number = Column(String(12))
    location_id = Column(Integer, ForeignKey("locations.id"))


class Location(Base, TimestampMixin):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    address = Column(String(250))


class Vehicle(Base, TimestampMixin):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    plate_number = Column(String(20), unique=True)
    name = Column(String(250))
    engine_capacity = Column(String(20))
    buying_value = Column(Float)
    projected_return_per_day = Column(Float)
    status = Column(Enum(StatusEnum), default=StatusEnum.ON_ROAD)


class Maintenance(Base, TimestampMixin):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    cost = Column(Float)
    description = Column(String(250))
    date = Column(Date)


class Remittance(Base, TimestampMixin):
    __tablename__ = "remittances"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    date = Column(Date)


class Route(Base, TimestampMixin):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))


class VehicleDriver(Base, TimestampMixin):
    __tablename__ = "vehicle_drivers"

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))


class VehicleRoute(Base, TimestampMixin):
    __tablename__ = "vehicle_routes"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))
    date_assigned = Column(Date)
