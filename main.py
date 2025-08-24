from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from database import Base, engine
import models  # Import all your models here to register them with SQLAlchemy

from routers import users, dailycare , emergency_support_services  # Add other routers as you create them

# Create all database tables on startup (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Health Copilot Backend")

# CORS settings: adjust origins per your frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Health Copilot</title></head>
        <body>
            <h1>Health Copilot Backend Running</h1>
            <p>Go to <a href="/docs">/docs</a> to test APIs</p>
        </body>
    </html>
    """

# Register routers for different functional modules
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(dailycare.router, prefix="/dailycare", tags=["DailyCare"])
app.include_router(emergency_support_services.router, prefix="/emergency", tags=["EmergencyServices"])
# Example placeholders - add your other routers here as you develop them:
# app.include_router(emergency.router, prefix="/emergency", tags=["Emergency"])
# app.include_router(resources.router, prefix="/resources", tags=["Resources"])
# app.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])
# app.include_router(specialists.router, prefix="/specialists", tags=["Specialists"])
# app.include_router(store_locator.router, prefix="/store_locator", tags=["StoreLocator"])

