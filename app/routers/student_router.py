from fastapi import APIRouter, HTTPException, Depends
from ..services import StudentService
from ..models import *
from ..models.generic_models import *
from ..auth import verify_token, require_role

student_service = StudentService()

student_router = APIRouter(prefix="/api")

@student_router.get("/students", response_model=GetSuccessResposne)
def get_all_students(user=Depends(verify_token)):
    response = student_service.get_all_students()
    return GetSuccessResposne(
        message="Get all students successful!",
        model=response
    )


@student_router.get("/student/{id}", response_model=GetSuccessResposne)
def get_student_by_account_id(id, user=Depends(verify_token)):
    response = student_service.get_student_by_account_id(id)
    
    if response == None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return GetSuccessResposne(
        message="Get student by id successful!",
        model=response
    )


# @student_router.get("/student/{id}")
# def get_student_by_student_id(id):
#     response = student_service.get_student_by_student_id(id)
#     return response


@student_router.post("/student", response_model=CreateSuccessResponse)
def add_student(
        student_request: CreateStudentRequest,
        user=Depends(require_role([AccountType.administrator]))
    ):
    student = student_service.add_student(student_request)
    return CreateSuccessResponse(
        message="Student added successfully!",
        model=student
    )


@student_router.put("/student/{id}", response_model=UpdateSuccessResponse)
def update_student(
        student_request: UpdateStudentRequest,
        id,
        user=Depends(require_role([AccountType.administrator]))
    ):
    student = student_service.update_student(student_request, id)
    return UpdateSuccessResponse(
        message="Student updated successfully!",
        model=student
    )
    
    
@student_router.delete("/student", response_model=DeleteSuccessResponse)
def delete_student(
        student_request: DeleteStudentRequest,
        user=Depends(require_role([AccountType.administrator]))
    ):
    student = student_service.delete_student(student_request)
    return DeleteSuccessResponse(
        message="Student deleted successfully!",
        model=student
    )
