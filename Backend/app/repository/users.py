import re
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model 
from app.utils import schemas
from app.utils.passwordRecoverHelper import generate_password_recovery_token, verify_password_reset_token
from app.emails import passwordRecoveryEmail


def create(request: schemas.CreateUser, db: Session):
    user = db.query(model.User).filter(model.User.email == request.email).first()
    if user:
        return{"info": f"User with the email {request.email} already exist"}
    else: 
        new_user = model.User(fullName =request.fullName,
                              email = request.email,
                              phoneNumber = request.phoneNumber, 
                              location = request.location,
                              homeGPSAddress = request.homeGPSAddress,
                              landMark = request.landMark,
                              houseNo = request.houseNo,
                              password = Hash.bcrypt(request.password)
                              )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return{"success": f"User with the email {request.email} created"}


def show(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def get_all(db: Session):
    users = db.query(model.User).filter(model.User.sensorId != None).all()
    return users

def destroy(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    user.delete(synchronize_session=False)
    db.commit()
    return {"success": f"User Deleted"}


def update(id: int, request: schemas.ShowUser, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.fullName =request.fullName
    user.email = request.email
    user.phoneNumber = request.phoneNumber
    user.location = request.location
    user.homeGPSAddress = request.homeGPSAddress
    user.landMark = request.landMark
    user.houseNo = request.houseNo
    user.password = Hash.bcrypt(request.password)
    user.sensorId =  request.sensorId
    user.isActive = request.isActive
    db.commit()
    db.refresh(user)
    return user

def is_active(user: schemas.ShowUser) -> bool:
        return user.isActive

def is_superuser(user: schemas.ShowUser) -> bool:
        return user.is_superuser
    
def get_by_email(db: Session, request):
    user = db.query(model.User).filter(model.User.email ==request).first()
    return user

def authenticate( db: Session ,request):
        user = get_by_email(db, request.username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
        elif not Hash.verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
        return user

def showUser(db: Session, email: str ):
    user = db.query(model.User).filter(model.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {email} is not available")
    return user

def get_by_name(fullName: str, db: Session):
    user = db.query(model.User).filter(
        model.User.fullName ==fullName).first()
    return user


def passwordRecover( email: str, db: Session, url:str):
    user = db.query(model.User).filter(model.User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this email does not exist in the system.",
        )
    token = generate_password_recovery_token(email=user.email)

    link = f"{url}?token={token}"
    passwordRecoveryEmail.passwordRevovery(user.email, user.fullName, link)
    return {"msg": "Password recovery email sent"}

def passwordReset(token: str, new_password: str, db: Session):
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = db.query(model.User).filter(model.User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    user.paaword = Hash.bcrypt(new_password)
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}
   