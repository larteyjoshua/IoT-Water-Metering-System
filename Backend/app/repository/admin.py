
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, BackgroundTasks
from app.security.hashing import Hash
from app.models import model
from app.utils import schemas

def create(request: schemas.CreateAdmin, db: Session):
    user = db.query(model.User).filter(model.User.email == request.email).first()
    if user:
        return{"info": f"User with the email {request.email} already exist"}
    else: 
        new_manager = model.User(fullName=request.fullName,
                                     email=request.email,
                                      phoneNumber = request.phoneNumber, 
                                     password= Hash.bcrypt(request.password))
        db.add(new_manager)
        db.commit()
        db.refresh(new_manager)
        return{"success": f"Manager with the email {request.email} created"}


def show(id: int, db: Session):
    admin = db.query(model.User).filter(model.User.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"admin with the id {id} is not available")
    return admin

def get_all(db: Session):
    # admins =db.query(
    # models.User, 
    # models.UserRole, 
    # models.Role).filter(
    # models.User.id ==  models.UserRole.user_id).filter(
    # models.UserRole.role_id == models.Role.id).filter(models.Role.name == "ADMIN").all()
    admins = db.query(model.User).filter(model.User.sensorId == None).all()
    #roles = db.query(models.Role, models.UserRole).all()

    return admins

def destroy(id: int, db: Session):
    admin = db.query(model.User).filter(model.User.id == id)
    if not admin.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin with id {id} not found")
    admin.delete(synchronize_session=False)
    db.commit()
    return{"success": f"Admin with the email {id} Deleted"}

def update(id: int, request: schemas.ShowUser, db: Session):
    admin = db.query(model.User).filter(model.User.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin with id {id} not found")
     
    admin.email = request.email
    admin.fullName = request.fullName
    admin.isActive = request.isActive
    admin.roleId = request.roleId
    admin.phoneNumber = request.phoneNumber
    db.commit()
    db.refresh(admin)
    return admin


def is_active(admin: schemas.ShowAdmin) -> bool:
        return admin.is_active

def is_superuser(admin: schemas.ShowAdmin) -> bool:
        return admin.is_superuser
    

def showAdmin(db: Session, email: str ):
    #admin = db.query(models.Manager).filter(models.Manager.email == email).first()
    admin = db.query(model.User).join(model.Role).filter(model.User.email == email).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin with the id {email} is not available")
    #role =db.query(models.Role).filter(models.Role.id == admin.roleId).first()
    return admin