
from fastapi import HTTPException, status, BackgroundTasks
from app.models import  model
from app.utils import schemas
from sqlalchemy.orm import Session
 

def show(id: int, db: Session):
    reading = db.query(model.SensorReadings).filter(model.SensorReadings.id == id).first()
    if not reading:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sensor with the id {id} is not available")
    return reading

def get_all(db: Session):
    reading = db.query( model.SensorReadings).all()
    return reading

def destroy(id: int, db: Session):
    reading = db.query( model.SensorReadings).filter( model.SensorReadings.id == id)
    if not reading.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sensor with id {id} not found")
    reading.delete(synchronize_session=False)
    db.commit()
    return{"success": f"Sensor reading {id} Deleted"}

def show_by_user(id: int, db: Session):
    readings = db.query(model.SensorReadings).filter(model.SensorReadings.sensorId == id).all()
    if not readings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Readings id {id} is not available")
    return readings
