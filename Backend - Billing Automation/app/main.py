import uvicorn
import asyncio
import logging
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from app.utils.config import settings
from app.models import model, schemas
from app.repository import  sensorReadings
from sqlalchemy.orm import Session
from app.utils import database
from fastapi_utils.tasks import repeat_every
import logging
#models.Base.metadata.create_all(bind=engine)

description = """
. 🚀
## Automatic Generation of water Bills
"""
app = FastAPI(
    title = settings.PROJECT_NAME,
    description = description,
    contact={
        "name": "Joshua Lartey",
        "url": "https://www.linkedin.com/in/joshua-lartey-2ba404199/",
        "email": "larteyjoshua@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
get_db = database.get_db

 
@app.on_event("startup")  
                             
@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/requestinfo")
def info(request: Request):
    print(request.url)
    hostPort = request.client.port
    hostName = request.client.host
    url = request.url._url
    return { "hostName": hostName, "port": hostPort, "url": url }
    

@app.post('/sensor/addreading')
async def create_reading(request: schemas.CreateSensorReadings, db: Session = Depends(database.get_db)):
    return sensorReadings.create(request, db)