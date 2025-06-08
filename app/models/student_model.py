from pydantic import BaseModel

class Student(BaseModel):
    account_id: int
    student_id: int
    username: str
    password: str
    department_id: int

class CreateStudentRequest(BaseModel):
    student_id: int
    username: str
    password: str
    department_id: int


class UpdateStudentRequest(BaseModel):
    student_id: int
    username: str
    password: str
    department_id: int


class DeleteStudentRequest(BaseModel):
    account_id: int