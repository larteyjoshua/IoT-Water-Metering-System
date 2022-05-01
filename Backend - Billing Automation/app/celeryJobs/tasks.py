from app.celeryJobs.celeryWorker import celery, celery_log
from app.emails import billingEmail
import time
import json
from json import JSONEncoder
from sqlalchemy.orm import Session
from app.emails import billingEmail
from app.celeryJobs import billing
from app.utils import database

get_db = database.get_db

# @celery.autodiscover_tasks()
@celery.task(name ='app.celeryJobs.tasks.bill_creation')
def bill_creation():
    # db: Session = Depends(get_db)
    billing.generateBills()
   
    return {"message": "Bill Generation runs"}
    
@celery.task(name ='app.celeryJobs.tasks.sum_number')
def sum_number(x, y):
    add = x + y
    celery_log.info("I am suppose to run")
    return add

@celery.task(name ='app.celeryJobs.tasks.sendBillingEmail')
def sendBillingEmail(email:str, fullName: str, month: str, amount:str):
    time.sleep(5)
    celery_log.info("I am suppose to run")
    respon = billingEmail.sendBilling( email, fullName, month, amount)
    json_object = json.dumps(dict(respon), indent = 4) 
    return json_object
