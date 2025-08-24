from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, DateTime, Boolean,Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=True)
    dob = Column(Date)
    profile_pic = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)

    children = relationship("Child", back_populates="parent", cascade="all, delete-orphan")


class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    dob = Column(Date)
    condition = Column(String)  # dropdown selection
    notes = Column(Text, nullable=True)

    parent = relationship("User", back_populates="children")
    progress_logs = relationship("ProgressLog", back_populates="child", cascade="all, delete-orphan")
    incident_logs = relationship("IncidentLog", back_populates="child", cascade="all, delete-orphan")


class ProgressLog(Base):
    __tablename__ = "progress_logs"
    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey("children.id"))
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, nullable=True)
    completed_tasks = Column(Integer, default=0)
    total_tasks = Column(Integer, default=0)

    child = relationship("Child", back_populates="progress_logs")


class IncidentLog(Base):
    __tablename__ = "incident_logs"
    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey("children.id"))
    date = Column(DateTime, default=datetime.utcnow)
    description = Column(Text, nullable=False)
    tag = Column(String, nullable=False)  # behavior/status tag
    resolved = Column(Boolean, default=False)

    child = relationship("Child", back_populates="incident_logs")


class NearbyEmergencyResource(Base):
    __tablename__ = "nearby_emergency_resources"
    id = Column(Integer, primary_key=True, index=True)
    resource_type = Column(String, nullable=False)  # e.g., "ambulance", "medical_store", "doctor"
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    availability = Column(String, nullable=True)  # e.g., "24/7", "9am-5pm"
    notes = Column(Text, nullable=True)  # extra info


