from config import cfg
from model import *
import shared
from dto import *
from typing import List, Optional
from utils.db import session
from model import ROLE_PATIENT,ROLE_NURSE, ROLE_DOCTOR
import uuid

def requestReservation(request:reservationRequest, current_user):
    schedule_query = session.query(ScheduleTable)
    found_schedule = schedule_query.filter(ScheduleTable.id == request.schedule_id).first()
    
    if(found_schedule is not None):
        user_query = session.query(UserTable)
        user_found = user_query.filter(UserTable.id == found_schedule.doctor_id).first()
        
        reservation_query = session.query(ReservationTable)
        total_reservation = reservation_query.filter(ReservationTable.schedule_id == found_schedule.id).all()
       
        new_reservation = ReservationTable(
            id=uuid.uuid4(),
            queue_number=user_found.code+"_"+str(len(total_reservation) + 1)+"_"+request.date_request_at,
            date_request=request.date_request,
            date_request_at=request.date_request_at,
            time_start=request.time_start,
            time_end=request.time_end,
            status="pending",
            reason=request.reason,
            schedule_id=found_schedule.id,
            nurse_id=None,
            patient_id=str(current_user.id)
        )
        session.add(new_reservation)
        session.commit()

    else:
        return shared.error_response(error="something error")

    return "success add reservation"


def requestReservationByNurse(request:reservationRequest, current_user):

    schedule_query = session.query(ScheduleTable)
    found_schedule = schedule_query.filter(ScheduleTable.id == request.schedule_id).first()
    
    if(found_schedule is not None):
        user_query = session.query(UserTable)
        user_found = user_query.filter(UserTable.id == found_schedule.doctor_id).first()
        
        reservation_query = session.query(ReservationTable)
        total_reservation = reservation_query.filter(ReservationTable.schedule_id == found_schedule.id).all()
       
        new_reservation = ReservationTable(
            id=uuid.uuid4(),
            queue_number=user_found.code+"_"+str(len(total_reservation)+1)+"_"+request.date_request_at,
            date_request=request.date_request,
            date_request_at=request.date_request_at,
            time_start=request.time_start,
            time_end=request.time_end,
            status="pending",
            reason=request.reason,
            schedule_id=found_schedule.id,
            nurse_id=current_user.id,
            patient_id=request.patient_id
        )
        session.add(new_reservation)
        session.commit()

    else:
        return shared.error_response(error="something error")

    return "success add reservation"

def confirmReservation(reservation_id:str):
    reservation_query = session.query(ReservationTable)
    found_reservation = reservation_query.filter(ReservationTable.id == reservation_id).first()
    if(found_reservation is not None):
        found_reservation.status = "confirmed"
        session.add(found_reservation)
        session.commit()
        return "success confirm reservation"
    else:
        return shared.error_response(error="reservation not found")

def rejectReservation(reservation_id:str):
    reservation_query = session.query(ReservationTable)
    found_reservation = reservation_query.filter(ReservationTable.id == reservation_id).first()
    if(found_reservation is not None):
        found_reservation.status = "rejected"
        session.add(found_reservation)
        session.commit()
        return "success reject reservation"
    else:
        return shared.error_response(error="reservation not found")

def cancelReservation(reservation_id:str):
    reservation_query = session.query(ReservationTable)
    found_reservation = reservation_query.filter(ReservationTable.id == reservation_id).first()
    if(found_reservation is not None):
        found_reservation.status = "canceled"
        session.add(found_reservation)
        session.commit()
        return "success confirm reservation"
    else:
        return shared.error_response(error="reservation not found")

def assignNurseReservation(request:reservationAssignNurseRequest):
    reservation_query = session.query(ReservationTable)
    found_reservation = reservation_query.filter(ReservationTable.id == request.reservation_id).first()
    if(found_reservation is not None):
        found_reservation.nurse_id = request.nurse_id
        session.add(found_reservation)
        session.commit()
        return "success assign nurse"
    else:
        return shared.error_response(error="reservation not found")