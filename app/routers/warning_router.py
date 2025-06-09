from fastapi import APIRouter, HTTPException
from ..services import WarningService
from ..models import *
from ..models.generic_models import *

warning_service = WarningService()

warning_router = APIRouter(prefix="/api")

@warning_router.get("/warnings", response_model=GetSuccessResposne)
def get_all_warnings():
    response = warning_service.get_all_warnings()
    return GetSuccessResposne(
        message="Get all warnings successful!",
        model=response
    )
    
    
@warning_router.get("/warning/{id}", response_model=GetSuccessResposne)
def get_warning_by_id(id):
    response = warning_service.get_warning_by_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Warning not found")
    
    return GetSuccessResposne(
        message="Get warning by id successful!",
        model=response
    )
    
    
@warning_router.post("/warning", response_model=CreateSuccessResponse)
def add_warning(warning_request: CreateWarningRequest):
    warning = warning_service.add_warning(warning_request)
    return CreateSuccessResponse(
        message="Warning added successfully!",
        model=warning
    )
    
    
@warning_router.put("/warning/{id}", response_model=UpdateSuccessResponse)
def update_warning(warning_request: UpdateWarningRequest, id):
    warning = warning_service.update_warning(warning_request, id)
    return UpdateSuccessResponse(
        message="Warning updated successfully!",
        model=warning
    )
    
    
@warning_router.delete("/warning", response_model=DeleteSuccessResponse)
def delete_warning(warning_request: DeleteWarningRequest):
    warning = warning_service.delete_warning(warning_request)
    return DeleteSuccessResponse(
        message="Warning deleted successfully!",
        model=warning
    )
    
    
    