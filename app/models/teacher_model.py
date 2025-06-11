from pydantic import BaseModel

class Teacher(BaseModel):
    account_id: int
    password: str
    username: str
    office_hour: str
    office_no: str
    
    
class CreateTeacherRequest(BaseModel):
    password: str
    username: str
    office_hour: str
    office_no: str
    
    
class UpdateTeacherRequest(BaseModel):
    password: str
    username: str
    office_hour: str
    office_no: str
    
    
    
class DeleteTeacherRequest(BaseModel):
    account_id: int
    
    
class TeacherLecturesResponse(BaseModel):
    account_id: int
    lecture_id: int
    lecture_name: str
    dept_name: str
    
    
class LectureStudentsResponse(BaseModel):
    username: str
    pass_grade: float
    dept_name: str
    
    
class UpdateStudentGradeRequest(BaseModel):
    pass_grade: float