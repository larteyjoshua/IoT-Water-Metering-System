from cgitb import text
from typing import List, Optional
from pydantic import BaseModel
from datetime import  datetime

class CreateUser(BaseModel):
    fullName: str
    email: str
    phoneNumber: str
    location: str
    homeGPSAddress: str
    landMark: str
    houseNo: str
    password: str

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    id: int
    fullName: str
    email: str
    phoneNumber: str
    location: str
    homeGPSAddress: str
    landMark: str
    houseNo: str
    isActive: bool
    dateCreated: datetime
    sensorId:  Optional[str] = None
    
    class Config():
        orm_mode = True
      
        
class CreateRole(BaseModel):
    name: str
    description: str
    class Config():
        orm_mode = True 
        
class ShowRole(BaseModel):
    id: int
    name: str
    description: str
    dateAdded: datetime
    
    class Config():
        orm_mode = True


class CreatePayment(BaseModel):
    sensorId: int
    totalAmount: float
    amountPaid: float
    balance: float
    comment: str
    modifyBy: str
    class Config():
        orm_mode = True

class ShowPayment(BaseModel):
    id: int
    sensorId: int
    totalAmount: float
    amountPaid: float
    balance: float
    comment: str
    modifyBy: str
    dateModified: datetime = None
    class Config():
        orm_mode = True
     
        
class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
 
    
class UserRoleBase(BaseModel):
    userId: Optional[int] = None
    roleId: Optional[int] = None
    
    
class CreateRate(BaseModel):
    ratePerLitre: float
    addedBy: int
    class Config():
        orm_mode = True
        
class ShowRates(BaseModel):
    id: int
    ratePerLitre: float
    addedBy: int
    dateAdded: datetime
    
    class Config():
        orm_mode = True
        
class CreateSensor(BaseModel):
    model: str
    class Config():
        orm_mode = True
        
class ShowSensor(BaseModel):
    id: int
    model: str
    dateAdded: datetime
    
    class Config():
        orm_mode = True
        
class CreateSensorReadings(BaseModel):
    sensorId: int
    waterFlowRate: float
    volume: float
    
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
        
class Msg(BaseModel):
    msg: str
    
class CreateCost(BaseModel):
    sensorId: int
    volumeUsed: float
    ratePerLitre: float
    totalCost: float
    
    class Config():
        orm_mode = True

class ShowAdmin(BaseModel):
    id: int = None
    fullName:str = None
    email:str = None
    phoneNumber: str = None
    isActive: bool =None
    dateCreated: datetime = None
    roleId: int = None
    
    class Config():
        orm_mode = True 
        
class CreateAdmin(BaseModel):
    fullName:str
    email:str
    phoneNumber: str
    password: str

    class Config():
        orm_mode = True 
        
class ShowCost(BaseModel):
    id: int
    volumeUsed: float
    ratePerLitre: float
    totalCost: float
    dateCreated: datetime
    
    class Config():
        orm_mode = True
