from fastapi import APIRouter, HTTPException
from ..services import DepartmentService
from ..models import *
from ..models.generic_models import *

department_service = DepartmentService()

department_router = APIRouter(prefix="/api")

@department_router.get("/departments", response_model=GetSuccessResposne)
def get_all_departments():
    response = department_service.get_all_departments()
    return GetSuccessResposne(
        message="Get all departments successfull!",
        model=response
    )


@department_router.get("/department/{id}", response_model=GetSuccessResposne)
def get_department_by_id(id: int):
    response = department_service.get_department_by_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Department not found")
    
    return GetSuccessResposne(
        message="Get department by id successful!",
        model=response
    )
    
    
@department_router.post("/department", response_model=CreateSuccessResponse)
def add_department(department_request: CreateDepartmentRequest):
    department = department_service.add_department(department_request)
    return CreateSuccessResponse(
        message="Department added successfully!",
        model=department
    )
    
    
@department_router.put("/department/{id}", response_model=UpdateSuccessResponse)
def update_department(department_request: UpdateDepartmentRequest, id: int):
    department = department_service.update_department(department_request, id)
    return UpdateSuccessResponse(
        message="Department updated successfully!",
        model=department
    )
    
    
@department_router.delete("/department", response_model=DeleteSuccessResponse)
def delete_department(department_request: DeleteDepartmentRequest):
    department = department_service.delete_department(department_request)
    return DeleteSuccessResponse(
        message="Department deleted successfully!",
        model=department
    ) 