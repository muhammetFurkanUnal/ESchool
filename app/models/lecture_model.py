from pydantic import BaseModel


class Lecture(BaseModel):
    lecture_id: int
    lecture_name: str
    department_id: int
    
    
class CreateLectureRequest(BaseModel):
    lecture_name: str
    department_id: int
    
    
class UpdateLectureRequest(BaseModel):
    lecture_name: str
    department_id: int
    
    
class DeleteLectureRequest(BaseModel):
    lecture_id: int