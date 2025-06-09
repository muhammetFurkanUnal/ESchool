from fastapi import FastAPI
from .routers import (
    health_router, 
    department_router, 
    student_router, 
    teacher_router, 
    administrator_router, 
    lecture_router, 
    warning_router, 
    schedule_router,
    take_router,
    teach_router
)
from .database import db

app = FastAPI()
app.include_router(health_router)
app.include_router(department_router)
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(administrator_router)
app.include_router(lecture_router)
app.include_router(warning_router)
app.include_router(schedule_router)
app.include_router(take_router)
app.include_router(teach_router)

