from pydantic import BaseModel
from datetime import date


class Schedule(BaseModel):
    schedule_id: int
    date: date
    schedule_text: str
    administrator_id: int


class CreateScheduleRequest(BaseModel):
    date: date
    schedule_text: str
    administrator_id: int


class UpdateScheduleRequest(BaseModel):
    date: date
    schedule_text: str
    administrator_id: int


class DeleteScheduleRequest(BaseModel):
    schedule_id: int
