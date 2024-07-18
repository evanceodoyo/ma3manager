from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class TimestampMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(
        Date, default=datetime.now(
            timezone.utc), nullable=False)
    updated_at = Column(
        Date,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        nullable=False)


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(
        Enum(
            'admin',
            'manager',
            'driver',
            name='user_roles'),
        nullable=False)
    id_number = Column(String(20), unique=True, nullable=False)
    dob = Column(Date, nullable=True)
    phone_number = Column(String(15), nullable=True)
    driving_license_number = Column(String(20), nullable=True)
    location_id = Column(Integer, ForeignKey('locations.id'))

    location = relationship("Location", back_populates="users")
    vehicles = relationship("VehicleDriver", back_populates="user")


class Vehicle(Base, TimestampMixin):
    __tablename__ = 'vehicles'
    location_id = Column(Integer, ForeignKey('locations.id'))
    plate_number = Column(String(10), unique=True, nullable=False)
    name = Column(String(50), nullable=True)
    engine_capacity = Column(String(20), nullable=False)
    buying_value = Column(Float, nullable=False)
    projected_return_per_day = Column(Float, nullable=False)
    status = Column(
        Enum(
            'on road',
            'in garage',
            'stalled',
            name='vehicle_statuses'),
        nullable=False)

    location = relationship("Location", back_populates="vehicles")
    drivers = relationship("VehicleDriver", back_populates="vehicle")
    maintenances = relationship("Maintenance", back_populates="vehicle")
    remittances = relationship("Remittance", back_populates="vehicle")
    routes = relationship("VehicleRoute", back_populates="vehicle")


class Location(Base, TimestampMixin):
    __tablename__ = 'locations'
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=True)

    users = relationship("User", back_populates="location")
    vehicles = relationship("Vehicle", back_populates="location")


class Route(Base, TimestampMixin):
    __tablename__ = 'routes'
    name = Column(String(50), nullable=False)

    vehicles = relationship("VehicleRoute", back_populates="route")


class VehicleDriver(Base, TimestampMixin):
    __tablename__ = 'vehicle_drivers'
    user_id = Column(Integer, ForeignKey('users.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    user = relationship("User", back_populates="vehicles")
    vehicle = relationship("Vehicle", back_populates="drivers")


class Maintenance(Base, TimestampMixin):
    __tablename__ = 'maintenances'
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    cost = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)

    vehicle = relationship("Vehicle", back_populates="maintenances")


class Remittance(Base, TimestampMixin):
    __tablename__ = 'remittances'
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    amount = Column(Float, nullable=False)

    vehicle = relationship("Vehicle", back_populates="remittances")


class VehicleRoute(Base, TimestampMixin):
    __tablename__ = 'vehicle_routes'
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    date_assigned = Column(Date, nullable=False)

    vehicle = relationship("Vehicle", back_populates="routes")
    route = relationship("Route", back_populates="vehicles")
