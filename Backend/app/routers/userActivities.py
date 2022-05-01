
from fastapi import APIRouter, Depends, status, Security, UploadFile, Form, File
from app.models import  model
from sqlalchemy.orm import Session
from app.utils import database, schemas
from app.security import oauth2
from app.repository import roles, users, sensors, sensors, rate,userRole, admin, sensorReading, cost, payment
from typing import List
from app.appcommons.userRoles import Role


router = APIRouter()
get_db = database.get_db

# Show Addmin
@router.post('/admin/register', tags = ['Admins'])
async  def create_admin(request: schemas.CreateAdmin, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return admin.create(request, db)

@router.get('/{id}', response_model=schemas.ShowAdmin, tags = ['Admins'])
async def get_admin(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return admin.show(id, db)

@router.get('/admin/',  response_model=List[schemas.ShowAdmin], tags = ['Admins'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return admin.get_all(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowAdmin, tags = ['Admins'])
async def update(id: int, request: schemas.ShowAdmin, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return admin.update(id, request, db)

@router.delete('/admin/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return admin.destroy(id, db)


#Users
@router.post('/users/register', tags = ['Admins'])
async  def create_user(request: schemas.CreateUser, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return users.create(request, db)

@router.get('/users/{id}', response_model=schemas.ShowUser,tags = ['Admins', "Users"])
async def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.ShowUser = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"], Role.USER["name"]],
    )):
    return users.show(id, db)

@router.get('/users/',  response_model=List[schemas.ShowUser], tags = ['Admins'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return users.get_all(db)


@router.put('/users/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowUser, tags = ['Admins', 'Users', 'Account Manager'])
async def update(id: int, request: schemas.ShowUser, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"], Role.ACCOUNT_MANAGER["name"], Role.USER['name']],
    )):
    return users.update(id, request, db)


@router.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return users.destroy(id, db)

# Sensor
@router.post('/sensors/register', tags = ['Admins'])
async  def create_sensor(request: schemas.CreateSensor, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return sensors.create(request, db)

@router.put('/sensors/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowSensor, tags = ['Admins'])
async def update(id: int, request: schemas.ShowSensor, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return sensors.update(id, request, db)

@router.get('/sensors/{id}', response_model=schemas.ShowSensor,tags = ['Admins'])
async def get_sensor(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"], Role.USER["name"]],
    )):
    return sensors.show(id, db)

@router.get('/sensors/',  response_model=List[schemas.ShowSensor], tags = ['Admins'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return sensors.get_all(db)

@router.delete('/sensors/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return sensors.destroy(id, db)

#roles
@router.post('/roles/add', tags = ['Admins'])
async  def create_role(request: schemas.CreateRole, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return roles.create(request, db)

@router.put('/roles/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowRole, tags = ['Admins'])
async def update(id: int, request: schemas.ShowRole, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return roles.update(id, request, db)

@router.get('/roles/',  response_model=List[schemas.ShowRole], tags = ['Admins'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return roles.get_all(db)

@router.get('/roles/{id}', response_model=schemas.ShowRole,tags = ['Admins'])
async def get_role(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"], Role.USER["name"]],
    )):
    return roles.show(id, db)

@router.delete('/roles/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return roles.destroy(id, db)

#rates
@router.post('/rates/add', tags = ['Admins'])
async  def create_rate(request: schemas.CreateRate, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return rate.create(request, db)

# @router.put('/rates/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowRates, tags = ['Admins'])
# async def update(id: int, request: schemas.ShowRates, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
#         oauth2.get_current_active_user,
#         scopes=[ Role.SUPER_ADMIN["name"]],
#     )):
#     return rate.update(id, request, db)

@router.get('/rates/',  response_model=List[schemas.ShowRates], tags = ['Admins'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return rate.get_all(db)

@router.get('/rates/{id}', response_model=schemas.ShowRates,tags = ['Admins', "Users"])
async def get_rate(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"], Role.USER["name"]],
    )):
    return rate.show(id, db)

@router.delete('/rates/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return rate.destroy(id, db)

# SensorReading
@router.get('/sensorReading/',  response_model=List[schemas.ShowSensorReadings], tags = ['Admins'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"]],
    )):
    return sensorReading.get_all(db)

@router.delete('/sensorReading/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return sensorReading.destroy(id, db)

@router.get('/sensorReading/{id}', tags = ['Admins'] )
async def all(id: int,db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return sensorReading.show_by_user(id, db)


#Assigning User Roles.

@router.post('/userRole/', tags = ['Admins'])
async def assigin_user_role(request: schemas.UserRoleBase, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return userRole.create(request, db)

@router.get('/userRole/{id}', tags = ['Admins'])
async def get_user_role(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return userRole.show(id, db)

@router.get('/userRole/', tags = ['Admins'] )
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return userRole.get_all(db)


@router.put('/userRole/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UserRoleBase, tags = ['Admins'])
async def update(id: int, request: schemas.UserRoleBase, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return userRole.update(id, request, db)

@router.delete('/userRole/{id}', status_code=status.HTTP_204_NO_CONTENT,  tags = ['Admins'])
async def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return cost.destroy(id, db)

#Costs
@router.get('/cost/{id}', tags = ['Admins'])
async def get_user_cost(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return cost.show(id, db)

@router.get('/cost/', tags = ['Admins'] )
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return cost.get_all(db)

@router.get('/waterCost/{id}', tags = ['Users'] )
async def all(id: int,db: Session = Depends(get_db), current_user: schemas.ShowUser = Security(
        oauth2.get_current_active_user,
        scopes=[Role.USER["name"]],
    )):
    return cost.show_by_user(id, db)


# Payment
@router.post('/payment/pay', tags = ['Admins', 'Account Manager'])
async  def create_payment(request: schemas.CreatePayment, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"]],
    )):
    return payment.create(request, db)

@router.put('/payment/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowPayment, tags = ['Admins','Account Manager'])
async def update(id: int, request: schemas.ShowPayment, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"], Role.ACCOUNT_MANAGER["name"]],
    )):
    return payment.update(id, request, db)

@router.get('/payment/{id}', response_model=schemas.ShowPayment,tags = ['Admins', 'Account Manager'])
async def get_payment(id: int, db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"], Role.USER["name"],  Role.ACCOUNT_MANAGER["name"]],
    )):
    return payment.show(id, db)

@router.get('/payment/',  response_model=List[schemas.ShowPayment], tags = ['Admins', 'Account Manager'])
async def all(db: Session = Depends(get_db), current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[ Role.SUPER_ADMIN["name"],  Role.ACCOUNT_MANAGER["name"]],
    )):
    return payment.get_all(db)

@router.delete('/payment/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Admins', 'Account Manager'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,
        scopes=[Role.SUPER_ADMIN["name"],  Role.ACCOUNT_MANAGER["name"]],
    )):
    return payment.destroy(id, db)


@router.get('/payment/{id}', tags = ['Users', 'Account Manager'] )
async def all(id: int,db: Session = Depends(get_db), current_user: schemas.ShowUser = Security(
        oauth2.get_current_active_user,
        scopes=[Role.USER["name"],  Role.ACCOUNT_MANAGER["name"]],
    )):
    return cost.show_by_user(id, db)