from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import model
from app.utils import schemas


def create(request: schemas.CreatePayment, db: Session): 
    cost = db.query(model.Cost).filter(model.Cost.sensorId == request.sensorId.desc()).first()
    old_payment = db.query(model.Payment).filtet(model.Payment.sensorId == request.sensorId.desc()).first()
    totalAmount = old_payment.totalAmount + cost.totalCost,
    new_payment = model.Payment(sensorId = request.sensorId,
                                totalAmount = totalAmount,
                                amountPaid = request.amountPaid,
                                balance =   totalAmount - request.amountPaid ,
                                comment = request.comment,
                                modifyBy =request.modifyBy)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return{"success": f"Payment Made for sensorId {request.sensorId}"}


def show(id: int, db: Session):
    payment = db.query(model.Payment).filter(model.Payment.id == id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"payment with the id {id} is not available")
    return payment

def get_all(db: Session):
    payments = db.query(model.Payment).all()
    return payments

def destroy(id: int, db: Session):
    payment = db.query(model.Payment).filter(model.Payment.id == id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Payment with id {id} not found")
    payment.delete(synchronize_session=False)
    db.commit()
    return  {"success": f"Payment Deleted"}

def update(id: int, request: schemas.ShowPayment, db: Session):
    payment = db.query(model.Payment).filter(model.Payment.id == id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"payment with id {id} not found")
    
    payment.amountPaid = request.amountPaid,
    payment.balance = request.balance,
    payment.modifyBy = request.modifyBy
    db.commit()
    db.refresh(payment)
    return payment

def show_by_user(id: int, db: Session):
    payments = db.query(model.Payment).filter(model.Payment.id == id).all()
    if not payments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Payment with the id {id} is not available")
    return payments