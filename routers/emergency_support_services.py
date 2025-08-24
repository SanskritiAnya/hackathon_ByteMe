from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from math import radians, cos, sin, asin, sqrt

from database import get_db
import models
import schemas

router = APIRouter()

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371 * c
    return km

@router.post("/", response_model=schemas.NearbyEmergencyResourceOut, tags=["EmergencyServices"])
def create_resource(resource: schemas.NearbyEmergencyResourceCreate, db: Session = Depends(get_db)):
    new_resource = models.NearbyEmergencyResource(**resource.dict())
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

@router.get("/", response_model=List[schemas.NearbyEmergencyResourceOut], tags=["EmergencyServices"])
def get_nearby_resources(
    resource_type: Optional[str] = Query(None, description="Filter by resource type"),
    latitude: Optional[float] = Query(None),
    longitude: Optional[float] = Query(None),
    radius_km: Optional[float] = Query(5.0, description="Radius in km"),
    city: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.NearbyEmergencyResource)
    if resource_type:
        query = query.filter(models.NearbyEmergencyResource.resource_type == resource_type)
    if city:
        query = query.filter(models.NearbyEmergencyResource.city == city)
    if state:
        query = query.filter(models.NearbyEmergencyResource.state == state)
    
    resources = query.all()

    if latitude is not None and longitude is not None:
        filtered = []
        for r in resources:
            distance = haversine(longitude, latitude, r.longitude, r.latitude)
            if distance <= radius_km:
                filtered.append(r)
        return filtered
    
    return resources

@router.get("/{resource_id}", response_model=schemas.NearbyEmergencyResourceOut, tags=["EmergencyServices"])
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(models.NearbyEmergencyResource).filter(models.NearbyEmergencyResource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.put("/{resource_id}", response_model=schemas.NearbyEmergencyResourceOut, tags=["EmergencyServices"])
def update_resource(resource_id: int, updated: schemas.NearbyEmergencyResourceCreate, db: Session = Depends(get_db)):
    resource = db.query(models.NearbyEmergencyResource).filter(models.NearbyEmergencyResource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    for var, value in vars(updated).items():
        setattr(resource, var, value) if value else None
    db.commit()
    db.refresh(resource)
    return resource

@router.delete("/{resource_id}", tags=["EmergencyServices"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(models.NearbyEmergencyResource).filter(models.NearbyEmergencyResource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(resource)
    db.commit()
    return {"detail": "Resource deleted"}
