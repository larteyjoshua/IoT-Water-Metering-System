
from fastapi import HTTPException, status, BackgroundTasks
from app.models import  model
from app.utils import schemas
from sqlalchemy.orm import Session
 
def create(request: schemas.CreateRate, db: Session):
        new_rate = model.Rate(ratePerLitre = request.ratePerLitre, addedBy = request.addedBy)
        db.add(new_rate)
        db.commit()
        db.refresh(new_rate)
        return{"success": f"Rate added with {request.addedBy}"}


def show(id: int, db: Session):
    rate = db.query(model.Rate).filter(model.Rate.id == id).first()
    if not rate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Rate with the id {id} is not available")
    return rate

def get_all(db: Session):
    rates = db.query( model.Rate).all()
    return rates

def destroy(id: int, db: Session):
    rate = db.query( model.Rate).filter( model.Rate.id == id)
    if not rate.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Rate with id {id} not found")
    rate.delete(synchronize_session=False)
    db.commit()
    return{"success": f"Rate Deleted"}