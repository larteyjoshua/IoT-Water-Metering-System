from sqlalchemy import Column, Table,Integer, String, ForeignKey, DateTime, TIMESTAMP, Float, Boolean, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.utils.database import Base

association_table = Table('association', Base.metadata,
    Column('sensorId', ForeignKey('sensors.id'), primary_key=True),
    Column('userId', ForeignKey('users.id'), primary_key=True)
)

class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key =True, index = True)
    model = Column(String)
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    added_by =relationship("User",secondary=association_table, back_populates="sensors")

class SensorReadings(Base):
    __tablename__ = 'sensorReadings'
    id = Column(Integer, primary_key =True, index = True)
    sensorId =  Column(Integer, ForeignKey('sensors.id'))
    waterFlowRate = Column(Float,  nullable=True)
    volume = Column(Float,  nullable=True)
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
    which_sensor =relationship("Sensor",backref="sensorReadings")
    
class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String)
    description = Column(Text)
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String)
    email = Column(String, unique=True, index=True)
    phoneNumber = Column(String)
    location = Column(String,  nullable=True)
    homeGPSAddress = Column(String,  nullable=True)
    landMark = Column(String,  nullable=True)
    houseNo = Column(String,  nullable=True)
    password = Column(String)
    dateCreated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    isActive = Column(Boolean(), default=True)
    sensorId =  Column(Integer, ForeignKey('sensors.id'), nullable=True)
    sensors =  relationship(
        "Sensor",
        secondary=association_table,
        back_populates="added_by", primaryjoin= sensorId == Sensor.id, post_update=True)
    user_role = relationship("UserRole", back_populates="user", uselist=False)
    
    
class UserRole(Base):
    __tablename__ = "userRoles" 
    userId = Column(Integer,ForeignKey("users.id"), primary_key=True, nullable=False, index = True)
    roleId = Column(Integer, ForeignKey("roles.id"), primary_key=True,nullable=False, index =  True)
    role = relationship("Role")
    user = relationship("User", back_populates="user_role", uselist=False)

    __table_args__ = (
        UniqueConstraint("userId", "roleId", name="unique_user_role"),
    )

class Cost(Base):
    __tablename__ = 'costs'
    id = Column(Integer, primary_key = True, index =True)
    sensorId = Column(Integer, ForeignKey('sensors.id'))
    volumeUsed = Column(Float)
    ratePerLitre = Column(Float)
    totalCost = Column(Float)
    dateCreated = Column(DateTime, default=datetime.now)
    which_sensor =relationship("Sensor", primaryjoin= sensorId == Sensor.id, post_update=True)
    
class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key = True, index =True)
    sensorId = Column(Integer, ForeignKey('sensors.id'))
    amountPaid = Column(Float)
    balance = Column(Float)
    comment = Column(Text)
    modifyBy = Column(Integer, ForeignKey('users.id'))
    dateModified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    sensor_reading = relationship("Sensor",primaryjoin= sensorId == Sensor.id, post_update=True)
    modify_by =relationship("User", primaryjoin= modifyBy == User.id, post_update=True)
    
class Rate(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key = True, index =True)
    ratePerLitre = Column(Float)
    addedBy = Column(Integer, ForeignKey('users.id'))
    dateAdded = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    added_by =relationship("User", primaryjoin= addedBy == User.id, post_update=True)


    