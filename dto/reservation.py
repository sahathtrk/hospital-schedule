from pydantic import BaseModel

class reservationRequest(BaseModel):
    date_request:str
    date_request_at:str
    time_start:str
    time_end:str
    reason:str
    schedule_id:str

class reservationByNurseRequest(BaseModel):
    date_request:str
    date_request_at:str
    time_start:str
    time_end:str
    reason:str
    schedule_id:str
    patient_id:str

class reservationStatusRequest(BaseModel):
    status:str
    reservation_id:str

class reservationAssignNurseRequest(BaseModel):
    nurse_id:str
    reservation_id:str