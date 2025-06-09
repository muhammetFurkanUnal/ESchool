from fastapi import FastAPI
from .routers import health_router, department_router, student_router, teacher_router
from .database import db

app = FastAPI()
app.include_router(health_router)
app.include_router(department_router)
app.include_router(student_router)
app.include_router(teacher_router)


