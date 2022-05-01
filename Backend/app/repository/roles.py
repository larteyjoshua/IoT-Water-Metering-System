from sqlalchemy.orm import Session
from fastapi import HTTPException, status, BackgroundTasks
from app.models import model
from app.utils import schemas


def create(request: schemas.CreateUser, db: Session):
    role = db.query(model.Role).filter(model.Role.name == request.name).first()
    if role:
        return{"info": f"Role with the name {request.name} already exist"}
    else: 
        new_role = model.Role(name=request.name, description = request.description)
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return{"success": f"Role with the name {request.name} created"}


def show(id: int, db: Session):
    role = db.query(model.Role).filter(model.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {id} is not available")
    return role

def get_all(db: Session):
    roles = db.query(model.Role).all()
    return roles

def destroy(id: int, db: Session):
    role = db.query(model.Role).filter(model.Role.id == id)
    if not role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    role.delete(synchronize_session=False)
    db.commit()
    return{"success": f"Role with the name {role.name} Deleted"}


def update(id: int, request: schemas.ShowUser, db: Session):
    role = db.query(model.Role).filter(model.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")
     
    role.name = request.name
    role.description = request.description
    db.commit()
    db.refresh(role)
    return role

def role_by_name(name: str, db: Session):
    role = db.query(model.Role).filter(model.Role.name == name).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {name} is not available")
    return role