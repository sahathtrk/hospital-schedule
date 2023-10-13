from typing import Annotated, Optional, List

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import GetDoctorsResponses, scheduleByPatientResponse, scheduleByPatientRequest, reservationRequest
from model import User, ROLE_PATIENT
from shared import IResponseBase, responses

route_patient = APIRouter(
    prefix="/api/v1/patient",
    tags=["Patient"]
)


@route_patient.post("/reservation/request", response_model=IResponseBase, responses=responses)
async def request_reservation(request:reservationRequest, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_PATIENT):
        return shared.success_response(data=controller.requestReservation(request, current_user))
    else:
        return shared.error_response(message="try login as patient", code="403001", error="auth error")

@route_patient.patch("/reservation/cancel", response_model=IResponseBase, responses=responses)
async def cancel_reservation(reservation_id:str, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_PATIENT):
        return shared.success_response(data=controller.rejectReservation(request))
    else:
        return shared.error_response(message="try login as patient", code="403001", error="auth error")

@route_patient.post("/schedule/get", response_model=IResponseBase[scheduleByPatientResponse], responses=responses)
async def get_doctor_schedule(current_user:Annotated[User, Depends(middleware.get_current_user)],request: scheduleByPatientRequest):
    if(current_user.role == ROLE_PATIENT):
        return shared.success_response(data=controller.fetchDoctorSchedule(request))
    else:
        return shared.error_response(message="try login as patient", code="403001", error='auth error')

@route_patient.get("/doctor/getAll", response_model=IResponseBase[List[GetDoctorsResponses]], responses=responses)
async def get_all_doctors(current_user:Annotated[User, Depends(middleware.get_current_user)], name:Optional[str]| None = None):
    if(current_user.role == ROLE_PATIENT):
        return shared.success_response(data=controller.fetchDoctors(name))
    else:
        return shared.error_response(message="try login as patient", code="403001", error='auth error')
