from pydantic import BaseModel


class Teach(BaseModel):
    teacher_id: int
    lecture_id: int


class CreateTeachRequest(BaseModel):
    teacher_id: int
    lecture_id: int


class DeleteTeachRequest(BaseModel):
    teacher_id: int
    lecture_id: int
