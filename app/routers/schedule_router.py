from fastapi import APIRouter, HTTPException, Depends
from ..services import ScheduleService
from ..models import *
from ..models.generic_models import *
from ..auth import require_role, verify_token

schedule_service = ScheduleService()

schedule_router = APIRouter(prefix="/api")

@schedule_router.get("/schedules", response_model=GetSuccessResposne)
def get_all_schedules(user=Depends(verify_token)):
    response = schedule_service.get_all_schedules()
    return GetSuccessResposne(
        message="Get all schedules successful!",
        model=response
    )
    
    
@schedule_router.get("/schedule/{id}", response_model=GetSuccessResposne)
def get_schedule_by_id(id, user=Depends(verify_token)):
    response = schedule_service.get_schedule_by_id(id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    
    return GetSuccessResposne(
        message="Get schedule by id successful!",
        model=response
    )
    
    
@schedule_router.post("/schedule", response_model=CreateSuccessResponse)
def add_schedule(
    schedule_request: CreateScheduleRequest,
    user=Depends(require_role([AccountType.administrator]))
):
    schedule = schedule_service.add_schedule(schedule_request)
    return CreateSuccessResponse(
        message="Schedule added successfully!",
        model=schedule
    )
    
    
@schedule_router.put("/schedule/{id}", response_model=UpdateSuccessResponse)
def update_schedule(
    schedule_request: UpdateScheduleRequest,
    id,
    user=Depends(require_role([AccountType.administrator]))
):
    schedule = schedule_service.update_schedule(schedule_request, id)
    return UpdateSuccessResponse(
        message="Schedule updated successfully!",
        model=schedule
    )
    
    
@schedule_router.delete("/schedule", response_model=DeleteSuccessResponse)
def delete_schedule(
    schedule_request: DeleteScheduleRequest,
    user=Depends(require_role([AccountType.administrator]))
):
    schedule = schedule_service.delete_schedule(schedule_request)
    return DeleteSuccessResponse(
        message="Schedule deleted successfully!",
        model=schedule
    )


