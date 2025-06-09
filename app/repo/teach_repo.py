from ..models.teach_model import *
from ..database import db
from ..database.queries.teach_queries import TeachQueries
from ..models.model_utils import *


class TeachRepo:
    def __init__(self):
        self.db = db

    def get_all_teaches(self):
        query = TeachQueries.get_all()
        teaches_raw = db.execute_query(query)

        if len(teaches_raw) == 0:
            return None

        teaches = raw_to_model(teaches_raw, Teach)
        return teaches

    def get_teach_by_teacher_and_lecture_id(self, teacher_id, lecture_id):
        query = TeachQueries.get_by_teacher_and_lecture_id(teacher_id, lecture_id)
        teach_raw = db.execute_query(query)

        if len(teach_raw) == 0:
            return None

        teach = raw_to_model(teach_raw, Teach)[0]
        return teach

    def add_teach(self, model: CreateTeachRequest):
        query = TeachQueries.create_teach(model)
        db.execute_query(query)
        teach = self.get_teach_by_teacher_and_lecture_id(model.teacher_id, model.lecture_id)
        return teach

    def delete_teach(self, model: DeleteTeachRequest):
        teach = self.get_teach_by_teacher_and_lecture_id(model.teacher_id, model.lecture_id)
        query = TeachQueries.delete_teach(model)
        db.execute_query(query)
        return teach
