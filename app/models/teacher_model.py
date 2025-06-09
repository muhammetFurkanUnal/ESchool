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