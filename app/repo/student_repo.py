from ..models.student_model import *
from ..database import db
from ..database.queries.student_queries import StudentQueries
from ..models.model_utils import *

class StudentRepo:
    def __init__(self):
        self.db = db
        

    def get_all_students(self):
        query = StudentQueries.get_all()
        students_raw = db.execute_query(query)
        
        if (len(students_raw) == 0):
            return None
        
        students = raw_to_model(students_raw, Student)
        return students
    
    
    def get_student_by_account_id(self, account_id):
        query = StudentQueries.get_by_account_id(account_id)
        student_raw = db.execute_query(query)
        
        if (len(student_raw) == 0):
            return None
        
        student = raw_to_model(student_raw, Student)[0]
        return student
    
    
    def get_student_by_username(self, username):
        query = StudentQueries.get_by_username(username)
        student_raw = db.execute_query(query)
        if (len(student_raw) == 0):
            return None
        
        student = raw_to_model(student_raw, Student)[0]
        return student
    
    
    # def get_student_by_student_id(self, account_id):
    #     query = StudentQueries.get_by_student_id(account_id)
    #     student_raw = db.execute_query(query)
    #     student = raw_to_model(student_raw, Student)
    #     return student
    
    
    def add_student(self, model: CreateStudentRequest):
        query = StudentQueries.create_student(model)
        new_student_id = db.execute_query(query)
        student = self.get_student_by_account_id(new_student_id)
        return student


    def update_student(self, model:UpdateStudentRequest, account_id):
        query = StudentQueries.update_student(model, account_id)
        db.execute_query(query)
        student = self.get_student_by_account_id(account_id)
        return student


    def delete_student(self, model:DeleteStudentRequest):
        student = self.get_student_by_account_id(model.account_id)
        query = StudentQueries.delete_student(model)
        db.execute_query(query)
        return student