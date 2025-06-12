from ...models.lecture_model import *

class LectureQueries:
    def get_all():
        return "SELECT * FROM Lecture"

    def get_by_id(lecture_id: int):
        return f"SELECT * FROM Lecture WHERE lecture_id={lecture_id}"

    def create_lecture(lecture: CreateLectureRequest):
        return f"""
                INSERT INTO Lecture
                (lecture_name, department_id)
                VALUES (
                    '{lecture.lecture_name}', 
                    {lecture.department_id}
                );
                """

    def update_lecture(lecture: UpdateLectureRequest, lecture_id: int):
        return f"""
                UPDATE Lecture
                SET lecture_name = '{lecture.lecture_name}',
                department_id = {lecture.department_id}
                WHERE lecture_id = {lecture_id}
                """

    def delete_lecture(lecture: DeleteLectureRequest):
        return f"""
                DELETE FROM Lecture
                WHERE lecture_id = {lecture.lecture_id};
                """
                
                
    def get_lecture_students(lecture_id: int):
        return f"""
                SELECT s.username, t.pass_grade, d.dept_name
                FROM take t
                JOIN Student s ON t.student_id = s.account_id
                LEFT JOIN Department d ON s.department_id = d.department_id
                WHERE t.lecture_id = {lecture_id}
                """
                
                
    def get_all_lectures():
        """Get all lectures with department info"""
        return """
                SELECT l.lecture_id, l.lecture_name, d.dept_name
                FROM Lecture l
                JOIN Department d ON l.department_id = d.department_id
                ORDER BY l.lecture_name
                """