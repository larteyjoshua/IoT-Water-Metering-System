
from app.models import  model
from sqlalchemy.orm import Session
from app.models import schemas
 
def create(request: schemas.CreateSensorReadings, db: Session):
        print(request.sensorId)
        print(request.waterFlowRate)
        print(request.volume)
        sensorID = int(request.sensorId)
        waterFlowingRate = float(request.waterFlowRate)
        volumeOfWater = float(request.volume)
        if (waterFlowingRate > 0 and volumeOfWater > 0):
                new_reading = model.SensorReadings(sensorId = sensorID, 
                                        waterFlowRate = waterFlowingRate,
                                        volume = volumeOfWater)
                db.add(new_reading)
                db.commit()
                db.refresh(new_reading)
                return "Data inserted"
        else:
                return "No reading values"