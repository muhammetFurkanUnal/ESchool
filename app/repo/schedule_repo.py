from ..models.schedule_model import *
from ..database import db
from ..database.queries.schedule_queries import ScheduleQueries
from ..models.model_utils import *


class ScheduleRepo:
    def __init__(self):
        self.db = db

    def get_all_schedules(self):
        query = ScheduleQueries.get_all()
        schedules_raw = db.execute_query(query)

        if len(schedules_raw) == 0:
            return None

        schedules = raw_to_model(schedules_raw, Schedule)
        return schedules

    def get_schedule_by_id(self, schedule_id):
        query = ScheduleQueries.get_by_id(schedule_id)
        schedule_raw = db.execute_query(query)

        if len(schedule_raw) == 0:
            return None

        schedule = raw_to_model(schedule_raw, Schedule)[0]
        return schedule
    
    def add_schedule(self, model: CreateScheduleRequest):
        query = ScheduleQueries.create_schedule(model)
        new_schedule_id = db.execute_query(query)
        schedule = self.get_schedule_by_id(new_schedule_id)
        return schedule
    
    
    def update_schedule(self, model: UpdateScheduleRequest, schedule_id):
        query = ScheduleQueries.update_schedule(model, schedule_id)
        db.execute_query(query)
        schedule = self.get_schedule_by_id(schedule_id)
        return schedule
    
    
    def delete_schedule(self, model: DeleteScheduleRequest):
        schedule = self.get_schedule_by_id(model.schedule_id)
        query = ScheduleQueries.delete_schedule(model)
        db.execute_query(query)
        return schedule
    
    