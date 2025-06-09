from fastapi import APIRouter, HTTPException, Depends
from ..services import TakeService
from ..models.take_model import *
from ..models.generic_models import *
from ..models import AccountType
from ..auth import verify_token, require_role

take_service = TakeService()

take_router = APIRouter(prefix="/api")


@take_router.get("/takes", response_model=GetSuccessResposne)
def get_all_takes(user=Depends(verify_token)):
    response = take_service.get_all_takes()
    return GetSuccessResposne(
        message="Get all takes successful!",
        model=response
    )


@take_router.get("/take/{student_id}/{lecture_id}", response_model=GetSuccessResposne)
def get_take_by_student_and_lecture_id(
        student_id: int, lecture_id: int, 
        user=Depends(verify_token)
    ):
    response = take_service.get_take_by_student_and_lecture_id(student_id, lecture_id)

    if response is None:
        raise HTTPException(status_code=404, detail="Take record not found")

    return GetSuccessResposne(
        message="Get take by student and lecture id successful!",
        model=response
    )


@take_router.post("/take", response_model=CreateSuccessResponse)
def add_take(
        take_request: CreateTakeRequest,
        user=Depends(require_role([AccountType.teacher, AccountType.administrator]))
    ):
    take = take_service.add_take(take_request)
    return CreateSuccessResponse(
        message="Take record added successfully!",
        model=take
    )


@take_router.put("/take/{student_id}/{lecture_id}", response_model=UpdateSuccessResponse)
def update_take(
        take_request: UpdateTakeRequest,
        student_id: int,
        lecture_id: int,
        user=Depends(require_role([AccountType.teacher, AccountType.administrator]))
    ):
    updated_take = take_service.update_take(take_request, student_id, lecture_id)
    return UpdateSuccessResponse(
        message="Take record updated successfully!",
        model=updated_take
    )


@take_router.delete("/take", response_model=DeleteSuccessResponse)
def delete_take(
        take_request: DeleteTakeRequest,
        user=Depends(require_role([AccountType.teacher, AccountType.administrator]))
    ):
    deleted_take = take_service.delete_take(take_request)
    return DeleteSuccessResponse(
        message="Take record deleted successfully!",
        model=deleted_take
    )
