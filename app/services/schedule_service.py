from ..repo import ScheduleRepo


class ScheduleService:
    def __init__(self):
        self.schedule_repo = ScheduleRepo()

    def get_all_schedules(self):
        schedules = self.schedule_repo.get_all_schedules()
        return schedules

    def get_schedule_by_id(self, schedule_id):
        schedule = self.schedule_repo.get_schedule_by_id(schedule_id)
        return schedule

    def add_schedule(self, model):
        schedule = self.schedule_repo.add_schedule(model)
        return schedule

    def update_schedule(self, model, schedule_id):
        updated_schedule = self.schedule_repo.update_schedule(model, schedule_id)
        return updated_schedule

    def delete_schedule(self, model):
        deleted_schedule = self.schedule_repo.delete_schedule(model)
        return deleted_schedule