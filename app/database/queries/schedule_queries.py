from ...models.schedule_model import *

class ScheduleQueries:
    def get_all():
        return "SELECT * FROM Schedule"

    def get_by_id(schedule_id: int):
        return f"SELECT * FROM Schedule WHERE schedule_id = {schedule_id}"

    def create_schedule(schedule: CreateScheduleRequest):
        return f"""
                INSERT INTO Schedule
                (date, schedule_text, administrator_id)
                VALUES (
                    '{schedule.date}',
                    '{schedule.schedule_text}',
                    {schedule.administrator_id}
                );
                """

    def update_schedule(schedule: UpdateScheduleRequest, schedule_id: int):
        return f"""
                UPDATE Schedule
                SET 
                    date = '{schedule.date}',
                    schedule_text = '{schedule.schedule_text}',
                    administrator_id = {schedule.administrator_id}
                WHERE schedule_id = {schedule_id};
                """

    def delete_schedule(schedule: DeleteScheduleRequest):
        return f"""
                DELETE FROM Schedule
                WHERE schedule_id = {schedule.schedule_id};
                """
