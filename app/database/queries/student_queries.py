from ...models.student_model import *


class StudentQueries:
    
    def get_all():
        return "SELECT * FROM Student"  
    
    def get_by_account_id(id: int):
        return f"SELECT * FROM Student WHERE account_id={id}"
    
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
