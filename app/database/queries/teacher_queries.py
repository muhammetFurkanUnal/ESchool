from ...models.teacher_model import *


class TeacherQueries:
    def get_all():
        return "SELECT * FROM Teacher"

    def get_by_account_id(id: int):
        return f"SELECT * FROM Teacher WHERE account_id={id}"
    
    
    def get_by_username(username: str):
        return f"SELECT * FROM Teacher WHERE username='{username}'"

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
                
                
    def get_teacher_lectures(id: int):
        return f"""
                SELECT t.teacher_id as account_id, l.lecture_id, l.lecture_name, d.dept_name
                FROM teach t
                JOIN Lecture l ON t.lecture_id = l.lecture_id
                JOIN Department d ON l.department_id = d.department_id
                WHERE t.teacher_id = {id}
                """
                
                
    def get_lecture_students(lecture_id: int):
        return f"""
                SELECT s.username, t.pass_grade, d.dept_name
                FROM take t
                JOIN Student s ON t.student_id = s.account_id
                LEFT JOIN Department d ON s.department_id = d.department_id
                WHERE t.lecture_id = {lecture_id}
                """
                
                
    def update_student_grade(account_id: int, lecture_id: int, grade: float):
        return f"UPDATE take SET pass_grade = {grade} WHERE student_id = {account_id} AND lecture_id = {lecture_id}"