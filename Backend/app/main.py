from fastapi import FastAPI, Request
from app.models import model
from app.utils.database import engine
from app.routers import userActivities, userLogin
from fastapi.middleware.cors import CORSMiddleware
from app.utils.config import settings


#models.Base.metadata.create_all(bind=engine)

description = """
. 🚀

## Admins

You can **manage the this system**.

## Users

You will be able to:

* **Create users**.
* **Read water bill**.
* **make payment**.
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
    

app.include_router(userLogin.router)
app.include_router(userActivities.router)

