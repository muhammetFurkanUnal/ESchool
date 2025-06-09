from fastapi import APIRouter, HTTPException
from ..services import AdministratorService
from ..models import *
from ..models.generic_models import *

administrator_service = AdministratorService()

administrator_router = APIRouter(prefix="/api")

@administrator_router.get("/administrators", response_model=GetSuccessResposne)
def get_all_administrators():
    response = administrator_service.get_all_administrators()
    return GetSuccessResposne(
        message="Get all administrators successful!",
        model=response
    )
    

@administrator_router.get("/administrator/{id}", response_model=GetSuccessResposne)
def get_administrator_by_account_id(id):
    response = administrator_service.get_administrator_by_account_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Administrator not found")
    
    return GetSuccessResposne(
        message="Get administrator by id successful!",
        model=response
    )
    
    
    
@administrator_router.post("/administrator", response_model=CreateSuccessResponse)
def add_administrator(administrator_request: CreateAdministratorRequest):
    administrator = administrator_service.add_administrator(administrator_request)
    return CreateSuccessResponse(
        message="Administrator added successfully!",
        model=administrator
    )
    
    
    
@administrator_router.put("/administrator/{id}", response_model=UpdateSuccessResponse)
def update_administrator(administrator_request: UpdateAdministratorRequest, id):
    administrator = administrator_service.update_administrator(administrator_request, id)
    return UpdateSuccessResponse(
        message="Administrator updated successfully!",
        model=administrator
    )
    
    
@administrator_router.delete("/administrator", response_model=DeleteSuccessResponse)
def delete_administrator(administrator_request: DeleteAdministratorRequest):
    administrator = administrator_service.delete_administrator(administrator_request)
    return DeleteSuccessResponse(
        message="Administrator deleted successfully!",
        model=administrator
    )



