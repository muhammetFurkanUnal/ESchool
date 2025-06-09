from ...models.teach_model import *

class TeachQueries:
    def get_all():
        return "SELECT * FROM teach"

    def get_by_teacher_and_lecture_id(teacher_id: int, lecture_id: int):
        return f"""
                SELECT * FROM teach
                WHERE teacher_id = {teacher_id} AND lecture_id = {lecture_id};
                """

    def create_teach(teach: CreateTeachRequest):
        return f"""
                INSERT INTO teach (teacher_id, lecture_id)
                VALUES (
                    {teach.teacher_id},
                    {teach.lecture_id}
                );
                """

    def delete_teach(teach: DeleteTeachRequest):
        return f"""
                DELETE FROM teach
                WHERE teacher_id = {teach.teacher_id} AND lecture_id = {teach.lecture_id};
                """
