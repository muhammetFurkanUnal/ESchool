from pydantic import BaseModel, Field

class Department(BaseModel):
    department_id: int
    dept_name: str


class CreateDepartmentRequest(BaseModel):
    dept_name:str
    
    
class UpdateDepartmentRequest(BaseModel):
    dept_name: str
    
    
class DeleteDepartmentRequest(BaseModel):
    department_id: int