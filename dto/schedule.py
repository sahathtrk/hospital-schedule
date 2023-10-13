from pydantic import BaseModel
from model import User

class ScheduleResponse(BaseModel):
    description:str
    # doctor_id:str
    date_start:str
    date_end:str
    time_start:str
    time_end:str


class ScheduleRequest(BaseModel):
    description: str
    date_start: str
    date_end: str
    time_start: str
    time_end: str

class scheduleByPatientRequest(BaseModel):
    doctor_id:str
    date:str

class scheduleByPatientResponse(BaseModel):
    schedule: ScheduleResponse
    doctor: User    
