from pydantic import BaseModel
from typing import Optional


class Take(BaseModel):
    student_id: int
    lecture_id: int
    pass_grade: Optional[float] 


class CreateTakeRequest(BaseModel):
    student_id: int
    lecture_id: int
    pass_grade: Optional[float] = None


class UpdateTakeRequest(BaseModel):
    pass_grade: Optional[float] = None


class DeleteTakeRequest(BaseModel):
    student_id: int
    lecture_id: int
