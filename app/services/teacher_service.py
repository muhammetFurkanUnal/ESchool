from ..repo import TeacherRepo
from ..auth import hash_password


class TeacherService:
    def __init__(self):
        self.teacher_repo = TeacherRepo()

    def get_teacher_by_account_id(self, account_id):
        teacher = self.teacher_repo.get_teacher_by_account_id(account_id)
        return teacher
    
    def get_teacher_by_username(self, username):
        teacher = self.teacher_repo.get_teacher_by_username(username)
        return teacher

    def get_all_teachers(self):
        teachers = self.teacher_repo.get_all_teachers()
        return teachers

    def add_teacher(self, teacher_data):
        teacher_data.password = hash_password(teacher_data.password)
        teacher = self.teacher_repo.add_teacher(teacher_data)
        return teacher

    def update_teacher(self, teacher_data, account_id):
        updated_teacher = self.teacher_repo.update_teacher(teacher_data, account_id)
        return updated_teacher

    def delete_teacher(self, teacher_data):
        teacher = self.teacher_repo.delete_teacher(teacher_data)
        return teacher
    
    
    def get_teacher_lectures(self, account_id):
        lectures = self.teacher_repo.get_teacher_lectures(account_id)
        return lectures
    
    
    def get_lecture_students(self, lecture_id):
        students = self.teacher_repo.get_lecture_students(lecture_id)
        return students
    
    
    def update_student_grade(self, account_id, lecture_id, pass_grade):
        self.teacher_repo.update_student_grade(account_id, lecture_id, pass_grade)
        return 
    
    
    