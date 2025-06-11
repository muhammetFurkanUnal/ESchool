from pydantic import BaseModel
from enum import Enum
from typing import Any

class AccountType(str, Enum):
    student = "student"
    teacher = "teacher"
    administrator = "administrator"
    debug = "debug"


class GetAuthRequest(BaseModel):
    username: str
    password: str
    account_type: AccountType
    

class AuthSuccessResponse(BaseModel):
    message: str
    token: str
    account: Any
    