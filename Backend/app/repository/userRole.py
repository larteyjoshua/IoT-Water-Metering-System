
from fastapi import HTTPException, status
from app.models import  model
from app.utils import schemas
from sqlalchemy.orm import Session
 
def create(request: schemas.UserRoleBase, db: Session):
        print('request', request)
        new_role = model.UserRole(userId=request.userId, roleId = request.roleId)
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return{"success": f"Role assigin to user with {request.userId}"}


def show(id: int, db: Session):
    role = db.query(model.UserRole).filter(model.UserRole.roleId == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User Role with the id {id} is not available")
    return role

def get_all(db: Session):
    roles = db.query(model.UserRole).all()
    return roles

def destroy(id: int, db: Session):
    role = db.query(model.UserRole).filter(model.UserRole.roleId == id)
    if not role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User Role with id {id} not found")
    role.delete(synchronize_session=False)
    db.commit()
    return{"success": f"Role with the name {role.role_id} Deleted"}


def update(id: int, request: schemas.UserRoleBase, db: Session):
    role = db.query(model.UserRole).filter(model.UserRole.role_id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f" User Role with id {id} not found")
     
    role.roleId = request.roleId
    role.userId = request.userId
    db.commit()
    db.refresh(role)
    return role