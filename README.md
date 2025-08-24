# ByteMe Backend — AI Health Copilot

A compassionate **AI-backed care companion platform** for parents of children with special needs.  
Built with **FastAPI**, this backend powers essential features like daily care tracking, scheduling, emergency assistance, and resource recommendations.

---

## ✨ Features

- **User Signup & Authentication**  
  Secure onboarding for parents and children with profile picture upload.  

- **Daily Care Dashboard**  
  Log behaviors, incidents, medications, and track progress with alerts.  

- **Scheduler**  
  Manage appointments, medication reminders, and therapy schedules.  

- **Resource Recommender**  
  Fetch context-aware articles, videos, and the latest assistive technologies.  

- **Locator Services**  
  - **Specialist Finder** — Locate nearby therapists & clinics.  
  - **Medical Store Locator** — Find nearby pharmacies.  

- **Emergency SOS**  
  One-tap alert system to contact nearby hospitals or emergency services.  

- **Parent Mental Health Support (Planned)**  
  Stress-management resources, self-care reminders, and counseling referrals.  

- **AI Chat Assistant (Planned)**  
  Multilingual, always-available companion for guidance and quick answers.  

---

## 🛠 Tech Stack

- **Backend**: FastAPI  
- **Database**: SQLite (default), easily swappable with PostgreSQL  
- **ORM**: SQLAlchemy  
- **Validation**: Pydantic  
- **Server**: Uvicorn  
- **Auth & Security**: JWT, Passlib (bcrypt)  

---

## 📂 Project Structure

├── main.py # Entrypoint
├── database.py # DB connection & session
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
└── routers/
├── users.py
├── daily_care.py
├── schedule.py
├── resources.py
├── store_locator.py
├── specialist.py
└── emergency.py


---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/SanskritiAnya/hackathon_ByteMe.git
cd hackathon_ByteMe
git checkout backend


2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic[email] passlib[bcrypt] PyJWT python-multipart

4. Initialize the database
python
>>> from database import Base, engine
>>> import models
>>> Base.metadata.create_all(bind=engine)
>>> exit()

5. Run the server
uvicorn main:app --reload


6. Explore API

Go to: http://127.0.0.1:8000/docs

Use Swagger UI to test endpoints.

📌 Usage Flow

Signup → /users/signup
Register parent and child with details and profile picture.

Login → /users/login
Authenticate and receive JWT token.

Dashboard → /daily_care/...
Log and track daily routines, incidents, medications.

Scheduler → /schedule/...
Manage appointments, reminders, and therapy plans.

Resources & Locators → /resources, /store_locator, /specialist
Access articles, find pharmacies, and locate specialists.

Emergency → /emergency/sos
Trigger one-tap hospital contact.

🌱 Next Steps

Parent mental health support module

Multilingual accessibility

AI-powered personalized recommendations

Real-time emergency notifications via SMS/push





