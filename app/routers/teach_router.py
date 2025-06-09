from fastapi import APIRouter, HTTPException, Depends
from ..services import TeachService
from ..models.teach_model import *
from ..models.generic_models import *
from ..models import AccountType
from ..auth import verify_token, require_role
from ..models.auth_model import AccountType

teach_service = TeachService()

teach_router = APIRouter(prefix="/api")


@teach_router.get("/teaches", response_model=GetSuccessResposne)
def get_all_teaches(user=Depends(verify_token)):
    response = teach_service.get_all_teaches()
    return GetSuccessResposne(
        message="Get all teaches successful!",
        model=response
    )


@teach_router.get("/teach/{teacher_id}/{lecture_id}", response_model=GetSuccessResposne)
def get_teach_by_teacher_and_lecture_id(
        teacher_id: int, 
        lecture_id: int, 
        user=Depends(verify_token)
    ):
    response = teach_service.get_teach_by_teacher_and_lecture_id(teacher_id, lecture_id)

    if response is None:
        raise HTTPException(status_code=404, detail="Teach record not found")

    return GetSuccessResposne(
        message="Get teach by teacher and lecture id successful!",
        model=response
    )


@teach_router.post("/teach", response_model=CreateSuccessResponse)
def add_teach(
        teach_request: CreateTeachRequest,
        user=Depends(require_role([AccountType.administrator]))
    ):
    teach = teach_service.add_teach(teach_request)
    return CreateSuccessResponse(
        message="Teach record added successfully!",
        model=teach
    )


@teach_router.delete("/teach", response_model=DeleteSuccessResponse)
def delete_teach(
        teach_request: DeleteTeachRequest,
        user=Depends(require_role([AccountType.administrator]))
    ):
    deleted_teach = teach_service.delete_teach(teach_request)
    return DeleteSuccessResponse(
        message="Teach record deleted successfully!",
        model=deleted_teach
    )
