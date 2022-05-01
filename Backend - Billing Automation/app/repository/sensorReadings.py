
from app.models import  model
from sqlalchemy.orm import Session
from app.models import schemas
 
def create(request: schemas.CreateSensorReadings, db: Session):
        new_reading = model.SensorReadings(sensorId = request.sensorId, 
                                  waterFlowRate = request.waterFlowRate,
                                  volume = request.volume)
        db.add(new_reading)
        db.commit()
        db.refresh(new_reading)
        return{"success": f"Reading added with {request.sensorId}"}