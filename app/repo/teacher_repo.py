from ..models.teacher_model import *
from ..database import db
from ..database.queries.teacher_queries import TeacherQueries
from ..models.model_utils import *


class TeacherRepo:
    def __init__(self):
        self.db = db
        

    def get_all_teachers(self):
        query = TeacherQueries.get_all()
        teachers_raw = db.execute_query(query)
        
        if len(teachers_raw) == 0:
            return None
        
        teachers = raw_to_model(teachers_raw, Teacher)
        return teachers
    
    
    def get_teacher_by_account_id(self, account_id):
        query = TeacherQueries.get_by_account_id(account_id)
        teacher_raw = db.execute_query(query)
        
        
        if len(teacher_raw) == 0:
            return None
        
        teacher = raw_to_model(teacher_raw, Teacher)[0]
        return teacher
    
    
    def get_teacher_by_username(self, username):
        query = TeacherQueries.get_by_username(username)
        teacher_raw = db.execute_query(query)
        
        if len(teacher_raw) == 0:
            return None
        
        teacher = raw_to_model(teacher_raw, Teacher)[0]
        return teacher
    
    
    def add_teacher(self, model: CreateTeacherRequest):
        query = TeacherQueries.create_teacher(model)
        new_teacher_id = db.execute_query(query)
        print("new id: ", new_teacher_id)
        teacher = self.get_teacher_by_account_id(new_teacher_id)
        return teacher

    def update_teacher(self, model: UpdateTeacherRequest, account_id):
        query = TeacherQueries.update_teacher(model, account_id)
        db.execute_query(query)
        teacher = self.get_teacher_by_account_id(account_id)
        return teacher

    def delete_teacher(self, model: DeleteTeacherRequest):
        teacher = self.get_teacher_by_account_id(model.account_id)
        query = TeacherQueries.delete_teacher(model)
        db.execute_query(query)
        return teacher
    
    
    def get_teacher_lectures(self, account_id):
        teacher_lectures_query = TeacherQueries.get_teacher_lectures(account_id)
        teacher_lectures_raw = db.execute_query(teacher_lectures_query)
        print("teacher lectures raw: ", teacher_lectures_raw)
        if len(teacher_lectures_raw) == 0:
            return None
        teacher_lectures = raw_to_model(teacher_lectures_raw, TeacherLecturesResponse)
        return teacher_lectures
    
    
    def get_lecture_students(self, lecture_id):
        lecture_students_query = TeacherQueries.get_lecture_students(lecture_id)
        lecture_students_raw = db.execute_query(lecture_students_query)
        
        print("lecture students raw: ", lecture_students_raw)
        
        if len(lecture_students_raw) == 0:
            return None
        
        lecture_students = raw_to_model(lecture_students_raw, LectureStudentsResponse)
        return lecture_students
    
    
    def update_student_grade(self, account_id, lecture_id, pass_grade):
        query = TeacherQueries.update_student_grade(account_id, lecture_id, pass_grade)
        db.execute_query(query)
        return 