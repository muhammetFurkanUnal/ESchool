from pydantic import BaseModel
from datetime import date


class Warning(BaseModel):
    warning_id: int
    date: date
    warning_text: str
    administrator_id: int


class CreateWarningRequest(BaseModel):
    date: date
    warning_text: str
    administrator_id: int


class UpdateWarningRequest(BaseModel):
    date: date
    warning_text: str
    administrator_id: int


class DeleteWarningRequest(BaseModel):
    warning_id: int
