from fastapi import APIRouter
from ..services import StudentService

student_service = StudentService()

student_router = APIRouter(prefix="/api")

@student_router.get("/students")
def get_all_students():
    response = student_service.get_all_students()
    return response



