from pydantic import BaseModel

class Student(BaseModel):
    username: str
    password: str
    department_id: int

