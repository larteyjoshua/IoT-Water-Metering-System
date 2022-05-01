from app.utils.config import settings
from sqlalchemy.orm import Session
from app.utils import schemas
from app.repository import roles, admin, userRole, users
from app.appcommons.userRoles import Role
from app.appcommons.initialUsers import User
import logging

def databaseinit(db: Session) -> None:
        logging.info("Initializing Database with Roles and Super Admin")
 # Create Role If They Don't Exist
        user_role_in = schemas.CreateRole(
            name=Role.USER["name"], description=Role.USER["description"])
        roles.create(user_role_in, db)

        account_manager = schemas.CreateRole(name=Role.ACCOUNT_MANAGER["name"],description=Role.ACCOUNT_MANAGER["description"])
        roles.create(account_manager, db)

    
        super_admin_role = schemas.CreateRole(name=Role.SUPER_ADMIN["name"],description=Role.SUPER_ADMIN["description"])
        roles.create(super_admin_role, db)
   
        ## Creating SuperAdmin
        super_admin_ = schemas.CreateAdmin(fullName=User.SUPER_ADMIN["fullName"],email=User.SUPER_ADMIN["email"], phoneNumber= User.SUPER_ADMIN["phoneNumber"], password=User.SUPER_ADMIN["password"])
        admin.create(super_admin_, db)
        
    # # Assign super_admin role to user
        role = roles.role_by_name(Role.SUPER_ADMIN["name"], db )
        print(role)
        user =users.get_by_name(User.SUPER_ADMIN["fullName"],db)
        print(user)
        super_admin_role =  schemas.UserRoleBase(userId = user.id, roleId = role.id)
        userRole.create(super_admin_role, db)
        
        logging.info("Database init Completed")
        return {"success": "Database Initialization Completed"}
