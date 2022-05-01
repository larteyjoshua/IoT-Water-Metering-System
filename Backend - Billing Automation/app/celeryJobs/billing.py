from sqlalchemy.orm import Session
from app.models import model, schemas
from datetime import datetime, timedelta
from sqlalchemy import and_
from fastapi import BackgroundTasks
from app.emails import billingEmail
import calendar
from app.celeryJobs import tasks

from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from app.utils import config


import logging

def generateBills():
     db_string = config.settings.SQLALCHEMY_DATABASE_URI
     con = create_engine(db_string)  
     Session = sessionmaker(con)  
     db = Session()
     
     
     fifteen_days_ago = datetime.today() - timedelta(days = 15)
     sensors = db.query( model.Sensor).all()
     print('days',fifteen_days_ago)
     print('leng sensors', len(sensors))
     volumeUsed = 0
     rate= db.query(model.Rate).order_by(model.Rate.id.desc()).first()
     print('rate',  rate.ratePerLitre)
     for sensor in sensors:
          senData = sensor
          readings = db.query(model.SensorReadings).filter(model.SensorReadings.sensorId == senData.id and model.SensorReadings.dateAdded <= fifteen_days_ago).all()
          user = db.query(model.User).filter(model.User.sensorId == senData.id).first()
          print('leng readings',len(readings))
          volumeUsed = sum(reading.volume for reading in readings)
          print('volume',volumeUsed)
          totalCost = volumeUsed * rate.ratePerLitre
          print('id', senData.id)
          print('totalcost', totalCost)
          new_cost =  model.Cost(sensorId = senData.id,
                                   volumeUsed = volumeUsed,
                                   ratePerLitre = rate.ratePerLitre,
                                   totalCost = totalCost)
          print(new_cost)
          #   db.add(new_cost)
          #   db.commit()
          #   db.refresh(new_cost)
          if user is not None:
               datem = datetime.strptime(str(senData.dateAdded), "%Y-%m-%d %H:%M:%S.%f")
               month =  calendar.month_name[datem.month]
               print('month', month)
               print('username',user.email)
               # respon = billingEmail.sendBilling( user.email,  user.fullName, month, str(totalCost))
               # print(respon)
               task = tasks.sendBillingEmail.delay( user.email, user.fullName, month, str(totalCost))
          db.close()   
          logging.info("Cost bill generate for sensor")
          