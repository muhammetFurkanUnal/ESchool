from fastapi import APIRouter

health_router = APIRouter(prefix="/api")

@health_router.get("/health")
def health():
    return "merhaba dünya!"


