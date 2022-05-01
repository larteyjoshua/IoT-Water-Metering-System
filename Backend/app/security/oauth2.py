from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.security import token
from sqlalchemy.orm import Session
from app.utils import database
from app.appcommons.userRoles import Role
from fastapi.security import SecurityScopes
from app.repository import users

get_db = database.get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", 
                                      scopes={
        Role.USER["name"]: Role.USER["description"],
        Role.ACCOUNT_MANAGER["name"]: Role.ACCOUNT_MANAGER["description"],
        Role.SUPER_ADMIN["name"]: Role.SUPER_ADMIN["description"],
       
    },
                                      )


def get_current_user( security_scopes: SecurityScopes,
                     data: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    
    return token.verify_token(data, db, security_scopes,)

def get_current_active_user(
    current_user = Security(get_current_user, scopes=[],)):
    if not users.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user