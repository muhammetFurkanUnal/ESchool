from ..models.lecture_model import *
from ..database import db
from ..database.queries.lecture_queries import LectureQueries
from ..models.model_utils import *

class LectureRepo:
    def __init__(self):
        self.db = db

    def get_all_lectures(self):
        query = LectureQueries.get_all()
        lectures_raw = db.execute_query(query)

        if len(lectures_raw) == 0:
            return None

        lectures = raw_to_model(lectures_raw, Lecture)
        return lectures

    def get_lecture_by_id(self, lecture_id):
        query = LectureQueries.get_by_id(lecture_id)
        lecture_raw = db.execute_query(query)

        if len(lecture_raw) == 0:
            return None

        lecture = raw_to_model(lecture_raw, Lecture)[0]
        return lecture
    
    def add_lecture(self, model: CreateLectureRequest):
        query = LectureQueries.create_lecture(model)
        new_lecture_id = db.execute_query(query)
        lecture = self.get_lecture_by_id(new_lecture_id)
        return lecture
    
    
    def update_lecture(self, model: UpdateLectureRequest, lecture_id):
        query = LectureQueries.update_lecture(model, lecture_id)
        db.execute_query(query)
        lecture = self.get_lecture_by_id(lecture_id)
        return lecture
    
    
    def delete_lecture(self, model: DeleteLectureRequest):
        lecture = self.get_lecture_by_id(model.lecture_id)
        query = LectureQueries.delete_lecture(model)
        db.execute_query(query)
        return lecture