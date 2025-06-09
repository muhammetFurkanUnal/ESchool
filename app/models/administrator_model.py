from pydantic import BaseModel

class Administrator(BaseModel):
    account_id: int
    password: str
    username: str
    
    
    
class CreateAdministratorRequest(BaseModel):
    password: str
    username: str

    
class UpdateAdministratorRequest(BaseModel):
    password: str
    username: str
    
    
    
class DeleteAdministratorRequest(BaseModel):
    account_id: int