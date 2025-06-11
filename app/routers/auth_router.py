from fastapi import APIRouter, HTTPException
from ..models.auth_model import *
from ..services import AuthService, AccountService

auth_service = AuthService()
account_service = AccountService()

auth_router = APIRouter(prefix="/api")

@auth_router.post("/auth", response_model=AuthSuccessResponse)
def authenticate(auth_request: GetAuthRequest):
    
    # null check
    if not auth_request.username or not auth_request.password:
        raise HTTPException(status_code=400, detail="Username and password are required")
    
    token = auth_service.authenticate_user(auth_request)
    
    account = account_service.get_account_by_username(
        username=auth_request.username, 
        account_type=auth_request.account_type
    )
    
    return AuthSuccessResponse(
        message="Authentication successful",
        token=token,
        account=account
    )
    
    
    
