from sqlalchemy import Column, UUID, String, Text, DateTime, ForeignKey, Time, Date
from sqlalchemy.orm import relationship
from typing import List

from pydantic import BaseModel
from utils.db import engine, base

class ScheduleTable(base):
    __tablename__ = "schedules"

    id = Column(String(36), primary_key=True, index=True)
    description = Column(Text, nullable=False)

    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)

    time_start = Column(Time(timezone=True), nullable=False)
    time_end = Column(Time(timezone=True), nullable=False)

    doctor_id = Column(String(36), ForeignKey("users.id"))
    doctor = relationship("UserTable", back_populates="schedules")

    reservations = relationship("ReservationTable", back_populates="schedule")

class Schedule(BaseModel):
    id: str
    description: str
    date_start: str
    date_end: str
    time_start: str
    time_end: str
    doctor_id:str
    # doctors: User

    @staticmethod
    def from_model_table(schedule_table: ScheduleTable):
        return Schedule(id=schedule_table.id,
                    description=schedule_table.description,
                    date_start=schedule_table.date_start,
                    date_end=schedule_table.date_end,
                    time_start=schedule_table.time_start,
                    time_end=schedule_table.time_end,
                    # doctors=schedule_table.doctors
                    )

