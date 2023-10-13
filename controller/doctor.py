from config import cfg
from model import *
from dto import *
from typing import List
from utils.db import session
from model import ROLE_PATIENT,ROLE_NURSE, ROLE_DOCTOR
import uuid

def fetchNurses() -> List[GetNursesResponses]:
    user_query = session.query(UserTable)
    nurses: UserTable =  user_query.filter(UserTable.role == ROLE_NURSE).all()
    
    responses:List[GetNursesResponses] = []

    i = 0
    for n in nurses:
        i += 1
        responses.append(GetNursesResponses(name=n.name, phone_number=n.phone_number, email=n.email))

    return responses

def fetchPatients() -> List[GetPatientsResponses]:
    user_query = session.query(UserTable)
    users: UserTable =  user_query.filter(UserTable.role == ROLE_PATIENT).all()
    
    responses:List[GetPatientsResponses] = []

    for u in users:
        responses.append(GetPatientsResponses(name=u.name, phone_number=u.phone_number))
    
    return responses


def createSchedule(request, current_user)->Schedule:
    schedule_query = session.query(ScheduleTable)
    new_schedule = ScheduleTable(
        id=uuid.uuid4(),
        description= request.description,
        date_start= request.date_start,
        date_end= request.date_end,
        time_start= request.time_start,
        time_end= request.time_end,
        doctor_id=current_user.id,
    )
    response = Schedule(
        id=str(uuid.uuid4()) ,
        description= str(request.description),
        date_start= str(request.date_start),
        date_end= str(request.date_end),
        time_start= str(request.time_start),
        time_end= str(request.time_end),
        doctor_id=str(current_user.id)
        )
    session.add(new_schedule)
    session.commit()
    return response