from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, Child
from schemas import UserOut, UserLogin, Token
import shutil
from datetime import datetime, timedelta
from utils import hash_password, verify_password
import jwt

router = APIRouter()

SECRET_KEY = "your_hackathon_secret"  # replace with secure key
ALGORITHM = "HS256"

# ----------------------
# SIGNUP ROUTE
# ----------------------
@router.post("/signup", response_model=UserOut)
async def signup(
    username: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    dob: str = Form(...),
    password: str = Form(...),  # <-- new field
    profile_pic: UploadFile = File(None),
    child_name: str = Form(...),
    child_dob: str = Form(...),
    child_condition: str = Form(...),
    child_notes: str = Form(None),
    db: Session = Depends(get_db)
):
    # Check if email already exists
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Save profile picture if uploaded
    pic_path = None
    if profile_pic:
        filename = f"profile_{int(datetime.utcnow().timestamp())}_{profile_pic.filename}"
        pic_path = f"uploads/{filename}"
        with open(pic_path, "wb") as buffer:
            shutil.copyfileobj(profile_pic.file, buffer)

    # Hash the password
    hashed_pw = hash_password(password)

    # Create parent
    parent = User(
        username=username,
        email=email,
        phone_number=phone_number,
        dob=datetime.strptime(dob, "%Y-%m-%d").date(),
        profile_pic=pic_path,
        hashed_password=hashed_pw
    )
    db.add(parent)
    db.commit()
    db.refresh(parent)

    # Create child
    child = Child(
        parent_id=parent.id,
        name=child_name,
        dob=datetime.strptime(child_dob, "%Y-%m-%d").date(),
        condition=child_condition,
        notes=child_notes
    )
    db.add(child)
    db.commit()
    db.refresh(child)

    parent.children = [child]  # attach child for response
    return parent

# ----------------------
# LOGIN ROUTE
# ----------------------
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    payload = {
        "sub": str(db_user.id),
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
