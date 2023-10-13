from utils.db import session
from model import ROLE_DOCTOR,ROLE_NURSE, ROLE_PATIENT
from model import *
from dto import *
from utils import create_password_hash
import uuid

def addNurse(request:adminRequest, current_user):
    user_query = session.query(UserTable)
    found_user = user_query.filter(UserTable.email == request.email).first()
    if found_user is None:
        new_user = UserTable(email=request.email,
                          id=uuid.uuid4(),
                          name=request.name,
                          password=create_password_hash(request.password),
                          phone_number=request.phone_number,
                          role=ROLE_NURSE,)
        session.add(new_user)
        session.commit()
        
    

def addDoctor(request:adminRequest, current_user):
    user_query = session.query(UserTable)
    found_user = user_query.filter(UserTable.email == request.email).first()
    if found_user is None:
        new_user = UserTable(email=request.email,
                          id=uuid.uuid4(),
                          name=request.name,
                          password=create_password_hash(request.password),
                          phone_number=request.phone_number,
                          code=ROLE_DOCTOR[0:4]+request.name[0:3],
                          role=ROLE_DOCTOR,)
        session.add(new_user)
        session.commit()
