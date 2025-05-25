from ..repo import StudentRepo

class StudentService:
    def __init__(self):
        self.student_repo = StudentRepo()

    def get_student_by_id(self, student_id):
        student = self.student_repo.get_student_by_id(student_id)
        return student
    
    def get_all_students(self):
        students = self.student_repo.get_all_students()
        return students

    def add_student(self, student_data):
        new_student = self.student_repo.add_student(student_data)
        return new_student

    # to be fixed
    def update_student(self, student_id, student_data):
        updated_student = self.student_repo.update_student(student_id, student_data)
        return updated_student

    def delete_student(self, student_id):
        student = self.student_repo.delete_student(student_id)
        return student
