from sqlalchemy import Column, Table,Integer, String, ForeignKey, DateTime, TIMESTAMP, Float, Boolean, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.utils.database import Base

class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key =True, index = True)
    model = Column(String)
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class SensorReadings(Base):
    __tablename__ = 'sensorReadings'
    id = Column(Integer, primary_key =True, index = True)
    sensorId =  Column(Integer, ForeignKey('sensors.id'))
    waterFlowRate = Column(Float,  nullable=True)
    volume = Column(Float,  nullable=True)
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
  
class Cost(Base):
    __tablename__ = 'costs'
    id = Column(Integer, primary_key = True, index =True)
    sensorId = Column(Integer, ForeignKey('sensors.id'))
    volumeUsed = Column(Float)
    ratePerLitre = Column(Float)
    totalCost = Column(Float)
    dateCreated = Column(DateTime, default=datetime.now)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String)
    email = Column(String, unique=True, index=True)
    phoneNumber = Column(String)
    location = Column(String)
    homeGPSAddress = Column(String)
    landMark = Column(String)
    houseNo = Column(String)
    password = Column(String)
    dateCreated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    isActive = Column(Boolean(), default=True)
    sensorId =  Column(Integer, ForeignKey('sensors.id'), nullable=True)
    
class Rate(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key = True, index =True)
    ratePerLitre = Column(Float)
    addedBy = Column(Integer, ForeignKey('users.id'))
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  
    

  
  