from pydantic import BaseModel

class GetNursesResponses(BaseModel):
    name:str
    phone_number:str
    email:str

class GetDoctorsResponses(BaseModel):
    name:str
    phone_number:str
    email:str
    code:str

class GetPatientsResponses(BaseModel):
    name:str
    phone_number:str
