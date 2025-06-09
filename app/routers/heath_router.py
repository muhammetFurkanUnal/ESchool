from fastapi import APIRouter, Depends
from ..auth import verify_token

health_router = APIRouter(prefix="/api")

@health_router.get("/health")
def health(user=Depends(verify_token)):
    
    from fastapi import HTTPException
    from ..models import AccountType
    
    if user["account_type"] == AccountType.teacher:
        return {"message": "Health check successful", "status": "OK"}
    
    
    return HTTPException(status_code=403, detail="Access forbidden for non-administrators")


