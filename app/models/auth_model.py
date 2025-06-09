from pydantic import BaseModel
from enum import Enum

class AccountType(str, Enum):
    student = "student"
    teacher = "teacher"
    administrator = "administrator"


class GetAuthRequest(BaseModel):
    username: str
    password: str
    account_type: AccountType
    

class AuthSuccessResponse(BaseModel):
    message: str
    token: str
    