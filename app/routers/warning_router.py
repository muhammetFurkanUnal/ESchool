from fastapi import APIRouter, HTTPException, Depends
from ..services import WarningService
from ..models import *
from ..models.generic_models import *
from ..models import AccountType
from ..auth import verify_token, require_role

warning_service = WarningService()

warning_router = APIRouter(prefix="/api")

@warning_router.get("/warnings", response_model=GetSuccessResposne)
def get_all_warnings(user=Depends(verify_token)):
    response = warning_service.get_all_warnings()
    return GetSuccessResposne(
        message="Get all warnings successful!",
        model=response
    )
    
    
@warning_router.get("/warning/{id}", response_model=GetSuccessResposne)
def get_warning_by_id(
        id, 
        user=Depends(verify_token)
    ):
    response = warning_service.get_warning_by_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Warning not found")
    
    return GetSuccessResposne(
        message="Get warning by id successful!",
        model=response
    )
    
    
@warning_router.post("/warning", response_model=CreateSuccessResponse)
def add_warning(
        warning_request: CreateWarningRequest,
        user=Depends(require_role([AccountType.administrator]))
    ):
    warning = warning_service.add_warning(warning_request)
    return CreateSuccessResponse(
        message="Warning added successfully!",
        model=warning
    )
    
    
@warning_router.put("/warning/{id}", response_model=UpdateSuccessResponse)
def update_warning(
        warning_request: UpdateWarningRequest,
        id,
        user=Depends(require_role([AccountType.administrator]))
    ):
    warning = warning_service.update_warning(warning_request, id)
    return UpdateSuccessResponse(
        message="Warning updated successfully!",
        model=warning
    )
    
    
@warning_router.delete("/warning", response_model=DeleteSuccessResponse)
def delete_warning(
        warning_request: DeleteWarningRequest,
        user=Depends(require_role([AccountType.administrator]))
    ):
    warning = warning_service.delete_warning(warning_request)
    return DeleteSuccessResponse(
        message="Warning deleted successfully!",
        model=warning
    )


