from .student_service import StudentService
from .teacher_service import TeacherService
from .administrator_service import AdministratorService
from ..models.auth_model import AccountType

class AccountService:
    def __init__(self):
        self.student_service = StudentService()
        self.teacher_service = TeacherService()
        self.administrator_service = AdministratorService()
        
        
    def get_account_by_id(self, account_id: str, account_type: AccountType):
        if account_type == AccountType.student:
            return self.student_service.get_student_by_id(account_id)
        elif account_type == AccountType.teacher:
            return self.teacher_service.get_teacher_by_id(account_id)
        elif account_type == AccountType.administrator:
            return self.administrator_service.get_administrator_by_id(account_id)
        else:
            raise ValueError("Invalid account type specified")


    def get_account_by_username(self, username: str, account_type: AccountType):
        if account_type == AccountType.student:
            return self.student_service.get_student_by_username(username)
        elif account_type == AccountType.teacher:
            return self.teacher_service.get_teacher_by_username(username)
        elif account_type == AccountType.administrator:
            return self.administrator_service.get_administrator_by_username(username)
        else:
            raise ValueError("Invalid account type specified")


