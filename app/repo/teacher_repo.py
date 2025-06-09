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
        
        print(teacher_raw)
        
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