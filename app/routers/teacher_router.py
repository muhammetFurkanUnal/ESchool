from fastapi import APIRouter, HTTPException
from ..services import TeacherService
from ..models import *
from ..models.generic_models import *

teacher_service = TeacherService()
teacher_router = APIRouter(prefix="/api")

@teacher_router.get("/teachers", response_model=GetSuccessResposne)
def get_all_teachers():
    response = teacher_service.get_all_teachers()
    return GetSuccessResposne(
        message="Get all teachers successful!",
        model=response
    )
    
@teacher_router.get("/teacher/{id}", response_model=GetSuccessResposne)
def get_teacher_by_account_id(id):
    response = teacher_service.get_teacher_by_account_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    return GetSuccessResposne(
        message="Get teacher by id successful!",
        model=response
    )
    
    
@teacher_router.post("/teacher", response_model=CreateSuccessResponse)
def add_teacher(teacher_request: CreateTeacherRequest):
    teacher = teacher_service.add_teacher(teacher_request)
    return CreateSuccessResponse(
        message="Teacher added successfully!",
        model=teacher
    )
    
    
@teacher_router.put("/teacher/{id}", response_model=UpdateSuccessResponse)
def update_teacher(teacher_request: UpdateTeacherRequest, id):
    teacher = teacher_service.update_teacher(teacher_request, id)
    return UpdateSuccessResponse(
        message="Teacher updated successfully!",
        model=teacher
    )
    
    
@teacher_router.delete("/teacher", response_model=DeleteSuccessResponse)
def delete_teacher(teacher_request: DeleteTeacherRequest):
    teacher = teacher_service.delete_teacher(teacher_request)
    return DeleteSuccessResponse(
        message="Teacher deleted successfully!",
        model=teacher
    )