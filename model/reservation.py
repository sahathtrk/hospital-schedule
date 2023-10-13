from sqlalchemy import Column, String, Text, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from utils.db import engine, base
from pydantic import BaseModel

class ReservationTable(base):
    __tablename__ = "reservations"

    id = Column(String(36), primary_key=True)
    queue_number = Column(String(255), nullable=False)

    date_request = Column(Date, nullable=False)
    date_request_at = Column(Date, nullable=True)

    time_start = Column(Time(timezone=True), nullable=False)
    time_end = Column(Time(timezone=True), nullable=False)

    status = Column(String(20), nullable=False)
    reason = Column(Text, nullable=False)

    schedule_id = Column(String(36), ForeignKey("schedules.id"))
    schedule = relationship("ScheduleTable", back_populates="reservations")

    nurse_id = Column(String(36), ForeignKey("users.id"))
    patient_id = Column(String(36), ForeignKey("users.id"))
    # nurse = relationship("UserTable", cascade="all, delete-orphan", back_populates="reservations_nurse")
    # patient_id = Column(String(36), ForeignKey="users.id")
    

    
class Reservation(BaseModel):
    id: str
    queue_number: str
    date_request: str
    date_request_at: str
    time_start: str
    time_end: str
    status: str
    reason: str
    
    @staticmethod
    def from_model_table(reservation_table: ReservationTable):
        return Reservation(id=reservation_table.id,
                    queue_number=reservation_table.queue_number,
                    date_request=reservation_table.date_request,
                    date_request_at=reservation_table.date_request_at,
                    time_start=reservation_table.time_start,
                    time_end=reservation_table.time_end,
                    status=reservation_table.status,
                    reason=reservation_table.reason,
                   )
                