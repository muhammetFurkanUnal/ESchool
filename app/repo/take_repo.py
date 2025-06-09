from ..models.take_model import *
from ..database import db
from ..database.queries.take_queries import TakeQueries
from ..models.model_utils import *

class TakeRepo:
    def __init__(self):
        self.db = db

    def get_all_takes(self):
        query = TakeQueries.get_all()
        takes_raw = db.execute_query(query)

        if len(takes_raw) == 0:
            return None

        takes = raw_to_model(takes_raw, Take)
        return takes

    def get_take_by_student_and_lecture_id(self, student_id, lecture_id):
        query = TakeQueries.get_by_student_and_lecture_id(student_id, lecture_id)
        take_raw = db.execute_query(query)

        if len(take_raw) == 0:
            return None

        take = raw_to_model(take_raw, Take)[0]
        return take
    
    def add_take(self, model: CreateTakeRequest):
        query = TakeQueries.create_take(model)
        db.execute_query(query)
        take = self.get_take_by_student_and_lecture_id(model.student_id, model.lecture_id)
        return take
    
    def update_take(self, model: UpdateTakeRequest, student_id, lecture_id):
        query = TakeQueries.update_take(model, student_id, lecture_id)
        db.execute_query(query)
        take = self.get_take_by_student_and_lecture_id(student_id, lecture_id)
        return take
    
    
    def delete_take(self, model: DeleteTakeRequest):
        take = self.get_take_by_student_and_lecture_id(model.student_id, model.lecture_id)
        query = TakeQueries.delete_take(model)
        db.execute_query(query)
        return take
    
    
    