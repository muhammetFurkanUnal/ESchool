from fastapi import APIRouter, HTTPException
from ..services import LectureService
from ..models import *
from ..models.generic_models import *

lecture_service = LectureService()

lecture_router = APIRouter(prefix="/api")

@lecture_router.get("/lectures", response_model=GetSuccessResposne)
def get_all_lectures():
    response = lecture_service.get_all_lectures()
    return GetSuccessResposne(
        message="Get all lectures successful!",
        model=response
    )
    

@lecture_router.get("/lecture/{id}", response_model=GetSuccessResposne)
def get_lecture_by_id(id):
    response = lecture_service.get_lecture_by_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Lecture not found")
    
    return GetSuccessResposne(
        message="Get lecture by id successful!",
        model=response
    )
    
    
@lecture_router.post("/lecture", response_model=CreateSuccessResponse)
def add_lecture(lecture_request: CreateLectureRequest):
    lecture = lecture_service.add_lecture(lecture_request)
    return CreateSuccessResponse(
        message="Lecture added successfully!",
        model=lecture
    )
    
    
@lecture_router.put("/lecture/{id}", response_model=UpdateSuccessResponse)
def update_lecture(lecture_request: UpdateLectureRequest, id):
    lecture = lecture_service.update_lecture(lecture_request, id)
    return UpdateSuccessResponse(
        message="Lecture updated successfully!",
        model=lecture
    )

    
@lecture_router.delete("/lecture", response_model=DeleteSuccessResponse)
def delete_lecture(lecture_request: DeleteLectureRequest):
    lecture = lecture_service.delete_lecture(lecture_request)
    return DeleteSuccessResponse(
        message="Lecture deleted successfully!",
        model=lecture
    )