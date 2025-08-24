from pydantic import BaseModel, EmailStr,Field
from typing import Optional, List
from datetime import date, datetime


# ---------------- User and Child Schemas ----------------

class ChildCreate(BaseModel):
    name: str
    dob: date
    condition: str
    notes: Optional[str] = None


class ChildOut(ChildCreate):
    id: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    dob: date
    profile_pic: Optional[str] = None
    children: List[ChildCreate]


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone_number: str
    dob: date
    profile_pic: Optional[str]
    children: List[ChildOut]

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# --------------- DailyCare: Progress Log Schemas ------------------

class ProgressLogBase(BaseModel):
    notes: Optional[str]
    completed_tasks: int
    total_tasks: int
    date: Optional[datetime] = None


class ProgressLogCreate(ProgressLogBase):
    child_id: int


class ProgressLogOut(ProgressLogBase):
    id: int
    child_id: int

    class Config:
        from_attributes = True


# --------------- DailyCare: Incident Log Schemas ------------------

class IncidentLogBase(BaseModel):
    description: str
    tag: str
    resolved: Optional[bool] = False
    date: Optional[datetime] = None


class IncidentLogCreate(IncidentLogBase):
    child_id: int


class IncidentLogOut(IncidentLogBase):
    id: int
    child_id: int

    class Config:
        from_attributes = True



class NearbyEmergencyResourceBase(BaseModel):
    resource_type: str = Field(..., description="Type such as ambulance, medical_store, doctor")
    name: str
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    latitude: float
    longitude: float
    availability: Optional[str] = None
    notes: Optional[str] = None

class NearbyEmergencyResourceCreate(NearbyEmergencyResourceBase):
    pass

class NearbyEmergencyResourceOut(NearbyEmergencyResourceBase):
    id: int

    class Config:
        from_attributes = True
