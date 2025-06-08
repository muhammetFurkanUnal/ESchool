from pydantic import BaseModel
from typing import Any

class CreateSuccessResponse(BaseModel):
    message: str
    model: Any
    
    
class GetSuccessResposne(BaseModel):
    message: str
    model: Any


    
class UpdateSuccessResponse(BaseModel):
    message: str
    model: Any
    
    
class DeleteSuccessResponse(BaseModel):
    message: str
    model: Any