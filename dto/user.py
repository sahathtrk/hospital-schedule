from pydantic import BaseModel

class UserResponse(BaseModel):
    name:str
    phone_number:str
    password:str
    email:str
    code:str
    role:str

class adminRequest(BaseModel):
    name:str
    phone_number:str
    password:str
    email:str
