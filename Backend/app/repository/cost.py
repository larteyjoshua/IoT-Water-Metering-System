from sqlalchemy.orm import Session
from fastapi import HTTPException, status, BackgroundTasks
from app.models import model
from app.utils import schemas


def show(id: int, db: Session):
    cost = db.query(model.Cost).filter(model.Cost.id == id).first()
    if not cost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cost with the id {id} is not available")
    return cost

def get_all(db: Session):
    costs = db.query(model.Cost).all()
    return costs

def destroy(id: int, db: Session):
    cost = db.query(model.Cost).filter(model.Cost.id == id)
    if not cost.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cost with id {id} not found")
    cost.delete(synchronize_session=False)
    db.commit()
    return  {"success": f"Cost Deleted"}

def show_by_user(id: int, db: Session):
    costs = db.query(model.Cost).filter(model.Cost.sensorId == id).all()
    if not costs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cost with the id {id} is not available")
    return costs
