from config import cfg
from model import *
import shared
from dto import *
from typing import List, Optional
from utils.db import session
from model import ROLE_PATIENT,ROLE_NURSE, ROLE_DOCTOR

def fetchDoctors(name:Optional[str])->List[GetDoctorsResponses]:
    
    user_query = session.query(UserTable)

    nameDefault = ""

    if(name is not None):
        nameDefault = name

    users: UserTable =  user_query.filter(UserTable.role == ROLE_DOCTOR).filter(UserTable.name.like('%'+nameDefault+'%')).all()
    
    responses:List[GetDoctorsResponses] = []

    for u in users:
        responses.append(GetDoctorsResponses(name=u.name, phone_number=u.phone_number, email=u.email, code=u.code))

    return responses

def fetchDoctorSchedule(request:scheduleByPatientRequest):
    schedule_query = session.query(ScheduleTable)

    schedule = schedule_query.\
    filter(ScheduleTable.doctor_id == request.doctor_id).\
        filter(ScheduleTable.date_start <= request.date, ScheduleTable.date_end >= request.date).\
            first()
    
    if(schedule is not None):
        user_query = session.query(UserTable)
        doctor = user_query.filter(UserTable.id == request.doctor_id).first()
        response = scheduleByPatientResponse(
            schedule = ScheduleResponse(
            description= str(schedule.description),
            date_start=str(schedule.date_start),
            date_end=str(schedule.date_end),
            time_start=str(schedule.time_start),
            time_end=str(schedule.time_end)), 
            doctor = User(
                id= doctor.id,
                name= doctor.name,
                phone_number= doctor.phone_number,
                email= doctor.email,
                code= doctor.code,
                role= doctor.role))

        return response
   
    