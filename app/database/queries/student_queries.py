from ...models.student_model import *


class StudentQueries:
    
    def get_all():
        return "SELECT * FROM Student"  
    
    def get_by_account_id(id: int):
        return f"""
                SELECT s.*, d.dept_name
                FROM Student s
                LEFT JOIN Department d ON s.department_id = d.department_id
                WHERE s.account_id = {id}
                """
    
    
    def get_by_username(username: str):
        return f"""
                SELECT s.*, d.dept_name
                FROM Student s
                LEFT JOIN Department d ON s.department_id = d.department_id
                WHERE s.username = '{username}'
                """
    
    # def get_by_student_id(id: int):
    #     return f"SELECT * FROM Student WHERE student_id={id}"
    
    def create_student(student: CreateStudentRequest):
        return f"""
                INSERT INTO Student
                (student_id, username, password, department_id)
                VALUES (
                    {student.student_id}, 
                    '{student.username}', 
                    '{student.password}', 
                    {student.department_id}
                );
                
                """
                
                
    def update_student(student: UpdateStudentRequest, account_id: int):
        return f"""
                UPDATE Student
                SET student_id = {student.student_id},
                username = '{student.username}',
                password = {student.password},
                department_id = {student.department_id}
                WHERE account_id = {account_id}
                """

    def delete_student(student: DeleteStudentRequest):
        return f"""
                DELETE FROM Student
                WHERE account_id = {student.account_id};
    
                """

    def get_student_lectures(student_id: int):
        """Get all lectures for a student with grades"""
        
        return f"""
              SELECT t.student_id, l.lecture_id, l.lecture_name, d.dept_name, t.pass_grade,
                    te.username as teacher_name
              FROM take t
              JOIN Lecture l ON t.lecture_id = l.lecture_id
              JOIN Department d ON l.department_id = d.department_id
              LEFT JOIN teach th ON l.lecture_id = th.lecture_id
              LEFT JOIN Teacher te ON th.teacher_id = te.account_id
              WHERE t.student_id = {student_id}
              """
              
              
    def update_student_grade(account_id: int, lecture_id: int, grade: float):
        return f"UPDATE take SET pass_grade = {grade} WHERE student_id = {account_id} AND lecture_id = {lecture_id}"