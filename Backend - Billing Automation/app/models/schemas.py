from cgitb import text
from typing import List, Optional
from pydantic import BaseModel
from datetime import  datetime

class CreateSensorReadings(BaseModel):
    sensorId: int
    waterFlowRate: float
    volume: float
    
    class Config():
        orm_mode = True
        
class CreateCost(BaseModel):
    sensorId: int
    volumeUsed: float
    ratePerLitre: float
    totalCost: float
    
    class Config():
        orm_mode = True
        
class ShowSensorReadings(BaseModel):
    id: int
    sensorId: int
    waterFlowRate: float
    volume: float
    dateAdded: datetime
    
    class Config():
        orm_mode = True