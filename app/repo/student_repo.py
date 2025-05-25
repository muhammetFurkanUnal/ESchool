from ..models import Student
from ..database import db
from ..database.queries.student_queries import StudentQueries

class StudentRepo:
    def __init__(self):
        self.db = db

    def get_all_students(self):
        query = StudentQueries.get_all_students()
        students = db.execute_single(query)
        print(students)
        return students
    
    def get_student_by_id(self, student_id):
        pass
    
    def add_student(self, student_data):
        pass

    def update_student(self, student_id, student_data):
        pass

    def delete_student(self, student_id):
        pass