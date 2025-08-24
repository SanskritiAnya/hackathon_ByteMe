from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models
import schemas

router = APIRouter()

# Create a progress log entry
@router.post("/progress", response_model=schemas.ProgressLogOut, tags=["DailyCare"])
def create_progress(progress: schemas.ProgressLogCreate, db: Session = Depends(get_db)):
    child = db.query(models.Child).filter(models.Child.id == progress.child_id).first()
    if not child:
        raise HTTPException(status_code=404, detail="Child not found")
    progress_log = models.ProgressLog(
        child_id=progress.child_id,
        date=progress.date or None,
        notes=progress.notes,
        completed_tasks=progress.completed_tasks,
        total_tasks=progress.total_tasks
    )
    db.add(progress_log)
    db.commit()
    db.refresh(progress_log)
    return progress_log

# Get all progress logs for a child
@router.get("/progress/{child_id}", response_model=List[schemas.ProgressLogOut], tags=["DailyCare"])
def get_progress_logs(child_id: int, db: Session = Depends(get_db)):
    return db.query(models.ProgressLog).filter(models.ProgressLog.child_id == child_id).all()

# Create an incident log entry
@router.post("/incident", response_model=schemas.IncidentLogOut, tags=["DailyCare"])
def create_incident(incident: schemas.IncidentLogCreate, db: Session = Depends(get_db)):
    child = db.query(models.Child).filter(models.Child.id == incident.child_id).first()
    if not child:
        raise HTTPException(status_code=404, detail="Child not found")
    incident_log = models.IncidentLog(
        child_id=incident.child_id,
        date=incident.date or None,
        description=incident.description,
        tag=incident.tag,
        resolved=incident.resolved or False
    )
    db.add(incident_log)
    db.commit()
    db.refresh(incident_log)
    return incident_log

# Get all incident logs for a child
@router.get("/incident/{child_id}", response_model=List[schemas.IncidentLogOut], tags=["DailyCare"])
def get_incident_logs(child_id: int, db: Session = Depends(get_db)):
    return db.query(models.IncidentLog).filter(models.IncidentLog.child_id == child_id).all()
