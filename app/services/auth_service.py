from fastapi import HTTPException
from ..models.auth_model import GetAuthRequest, AccountType
from ..auth import create_access_token

class AuthService:
    def __init__(self):
        pass

    def authenticate_user(self, request: GetAuthRequest):
        username = request.username
        password = request.password
        account_type = request.account_type
        
        auth_strategy = None
        
        if account_type == AccountType.student:
            auth_strategy = StudentAuthStrategy()
        elif account_type == AccountType.teacher:
            auth_strategy = TeacherAuthStrategy()
        elif account_type == AccountType.administrator:
            auth_strategy = AdminAuthStrategy()
        else:
            raise HTTPException(status_code=400, detail="Invalid account type")
            
        auth_strategy.authenticate(username, password)
        
        return create_access_token(
            data={
                "username": username, 
                "account_type": account_type.value
            }
        )
        
        
        
class AccountAuthStrategy:
    def authenticate(self, username, password):
        raise NotImplementedError()
    
    
class StudentAuthStrategy(AccountAuthStrategy):
    def authenticate(self, username, password):
        from ..repo import StudentRepo
        student_repo = StudentRepo()
        student = student_repo.get_student_by_username(username)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        if student.password != password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        

class TeacherAuthStrategy(AccountAuthStrategy):
    def authenticate(self, username, password):
        from ..repo import TeacherRepo
        teacher_repo = TeacherRepo()
        teacher = teacher_repo.get_teacher_by_username(username)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        if teacher.password != password:
            raise HTTPException(status_code=401, detail="Invalid credentials")


class AdminAuthStrategy(AccountAuthStrategy):
    def authenticate(self, username, password):
        from ..repo import AdministratorRepo
        administrator_repo = AdministratorRepo()
        administrator = administrator_repo.get_administrator_by_username(username)
        if not administrator:
            raise HTTPException(status_code=404, detail="Administrator not found")
        if administrator.password != password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
