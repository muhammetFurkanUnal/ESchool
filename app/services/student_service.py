from ..repo import StudentRepo
from ..auth import hash_password
# from ..models.model_utils import *

class StudentService:
    def __init__(self):
        self.student_repo = StudentRepo()

    def get_student_by_account_id(self, student_id):
        student = self.student_repo.get_student_by_account_id(student_id)
        return student
    
    # def get_student_by_student_id(self, student_id):
    #     student = self.student_repo.get_student_by_student_id(student_id)
    #     return student
    
    def get_all_students(self):
        students = self.student_repo.get_all_students()
        return students

    def add_student(self, student_data):
        student_data.password = hash_password(student_data.password)
        student = self.student_repo.add_student(student_data)
        return student

    # to be fixed
    def update_student(self, student_data, account_id):
        updated_student = self.student_repo.update_student(student_data, account_id)
        return updated_student

    def delete_student(self, student_data):
        student = self.student_repo.delete_student(student_data)
        return student