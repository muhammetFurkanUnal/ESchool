from ...models.teacher_model import *


class TeacherQueries:
    def get_all():
        return "SELECT * FROM Teacher"

    def get_by_account_id(id: int):
        return f"SELECT * FROM Teacher WHERE account_id={id}"

    def create_teacher(teacher: CreateTeacherRequest):
        return f"""
                INSERT INTO Teacher
                (password, username, office_hour, office_no)
                VALUES (
                    '{teacher.password}', 
                    '{teacher.username}', 
                    '{teacher.office_hour}', 
                    '{teacher.office_no}'
                );
                """

    def update_teacher(teacher: UpdateTeacherRequest, account_id: int):
        return f"""
                UPDATE Teacher
                SET office_hour = '{teacher.office_hour}',
                username = '{teacher.username}',
                password = '{teacher.password}',
                office_no = '{teacher.office_no}'
                WHERE account_id = {account_id}
                """

    def delete_teacher(teacher: DeleteTeacherRequest):
        return f"""
                DELETE FROM Teacher
                WHERE account_id = {teacher.account_id};
                """