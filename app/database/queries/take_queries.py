from ...models.take_model import *

class TakeQueries:
    def get_all():
        return "SELECT * FROM take"

    def get_by_student_and_lecture_id(student_id: int, lecture_id: int):
        return f"""
                SELECT * FROM take
                WHERE student_id = {student_id} AND lecture_id = {lecture_id};
                """

    def create_take(take: CreateTakeRequest):
        return f"""
                INSERT INTO take (student_id, lecture_id, pass_grade)
                VALUES (
                    {take.student_id},
                    {take.lecture_id},
                    {take.pass_grade if take.pass_grade is not None else 'NULL'}
                );
                """

    def update_take(update: UpdateTakeRequest, student_id: int, lecture_id: int):
        return f"""
                UPDATE take
                SET pass_grade = {update.pass_grade if update.pass_grade is not None else 'NULL'}
                WHERE student_id = {student_id} AND lecture_id = {lecture_id};
                """

    def delete_take(take: DeleteTakeRequest):
        return f"""
                DELETE FROM take
                WHERE student_id = {take.student_id} AND lecture_id = {take.lecture_id};
                """
