from fastapi import HTTPException
from ..models.auth_model import GetAuthRequest, AccountType
from ..auth import create_access_token, verify_password

class AuthService:
    def __init__(self):
        pass

    def authenticate_user(self, request: GetAuthRequest):
        username = request.username
        password = request.password
        account_type = request.account_type
        
        # debugging mode active, disable this option in distribution
        if account_type == AccountType.debug:
            return create_access_token(
                data={
                    "username": username, 
                    "account_type": AccountType.administrator.value
                }
            )
        
        
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
        if not verify_password(password, student.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")


class TeacherAuthStrategy(AccountAuthStrategy):
    def authenticate(self, username, password):
        from ..repo import TeacherRepo
        teacher_repo = TeacherRepo()
        teacher = teacher_repo.get_teacher_by_username(username)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        if not verify_password(password, teacher.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")


class AdminAuthStrategy(AccountAuthStrategy):
    def authenticate(self, username, password):
        from ..repo import AdministratorRepo
        administrator_repo = AdministratorRepo()
        administrator = administrator_repo.get_administrator_by_username(username)
        if not administrator:
            raise HTTPException(status_code=404, detail="Administrator not found")
        if not verify_password(password, administrator.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
