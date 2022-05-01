
from fastapi import HTTPException, status, BackgroundTasks
from app.models import  model
from app.utils import schemas
from sqlalchemy.orm import Session
 
def create(request: schemas.CreateSensor, db: Session):
        new_sensor = model.Sensor(model = request.model)
        db.add(new_sensor)
        db.commit()
        db.refresh(new_sensor)
        return{"success": f"Sensor added with {request.model}"}


def show(id: int, db: Session):
    sensor = db.query(model.Sensor).filter(model.Sensor.id == id).first()
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sensor with the id {id} is not available")
    return sensor

def get_all(db: Session):
    sensors = db.query( model.Sensor).all()
    return sensors

def destroy(id: int, db: Session):
    sensor = db.query( model.Sensor).filter( model.Sensor.id == id)
    if not sensor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sensor with id {id} not found")
    sensor.delete(synchronize_session=False)
    db.commit()
    return{"success": f"Sensor with the name {sensor.id} Deleted"}


def update(id: int, request: schemas.ShowSensor, db: Session):
    sensor = db.query( model.Sensor).filter( model.Sensor.id == id).first()
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f" Sensor with id {id} not found")
     
    sensor.model = request.model
    db.commit()
    db.refresh(sensor)
    return sensor