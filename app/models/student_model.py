from pydantic import BaseModel

class Student(BaseModel):
    account_id: int
    student_id: int
    username: str
    password: str
    department_id: int
    dept_name: str

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
    
    

class StudentLectures(BaseModel):
    lecture_id: int
    lecture_name: str
    dept_name: str
    pass_grade: int
    teacher_name: str