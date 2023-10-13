from typing import Annotated

from fastapi import APIRouter, Depends

import controller
import middleware
import shared
from dto import UserResponse,GetNursesResponses, GetPatientsResponses, GetDoctorsResponses, scheduleByPatientRequest, scheduleByPatientResponse, reservationByNurseRequest
from model import User, ROLE_NURSE
from shared import IResponseBase, responses
from typing import List

route_nurse = APIRouter(
    prefix="/api/v1/nurse",
    tags=["Nurse"]
)


@route_nurse.post("/reservation/request", response_model=IResponseBase, responses=responses)
async def request_reservation(request:reservationByNurseRequest, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_NURSE):
        return shared.success_response(data=controller.requestReservationByNurse(request, current_user))
    else:
        return shared.error_response(message="try login as nurse", code="403001", error="auth error")


@route_nurse.patch("/reservation/confirm", response_model=IResponseBase, responses=responses)
async def confirm_reservation(reservation_id:str, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_NURSE):
        return shared.success_response(data=controller.confirmReservation(reservation_id))
    else:
        return shared.error_response(message="try login as nurse", code="403001", error='auth error')

@route_nurse.patch("/reservation/reject", response_model=IResponseBase, responses=responses)
async def reject_reservation(reservation_id:str, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_NURSE):
        return shared.success_response(data=controller.rejectReservation(reservation_id))
    else:
        return shared.error_response(message="try login as nurse", code="403001", error='auth error')

@route_nurse.patch("/reservation/cancel", response_model=IResponseBase, responses=responses)
async def cancel_reservation(reservation_id:str, current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_NURSE):
        return shared.success_response(data=controller.cancelReservation(reservation_id))
    else:
        return shared.error_response(message="try login as nurse", code="403001", error='auth error')

@route_nurse.post("/schedule/get", response_model=IResponseBase[scheduleByPatientResponse], responses=responses)
async def get_doctor_schedule(current_user:Annotated[User, Depends(middleware.get_current_user)],request: scheduleByPatientRequest):
    if(current_user.role == ROLE_NURSE):
        return shared.success_response(data=controller.fetchDoctorSchedule(request))
    else:
        return shared.error_response(message="try login as nurse", code="403001", error='auth error')


@route_nurse.get("/get/patients", response_model=IResponseBase[List[GetPatientsResponses]], responses=responses)
async def get_all_patients(current_user:Annotated[User, Depends(middleware.get_current_user)]):
    if(current_user.role == ROLE_NURSE):
         return shared.success_response(data=controller.fetchPatients())
    else:
        return shared.error_response(message="try login as nurse", code="403001", error='auth error')
   
