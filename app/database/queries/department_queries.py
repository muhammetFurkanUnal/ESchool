from ...models.department_model import *


class DepartmentQueries:
    
    def get_all():
        return "SELECT * FROM Department"
    
    
    def get_by_id(id: int):
        return f"SELECT * FROM Department WHERE department_id={id}"
    
    
    def create_department(department: CreateDepartmentRequest):
        return f"INSERT INTO Department (dept_name) VALUES ('{department.dept_name}');"
    
    
    def update_department(department: UpdateDepartmentRequest, id:int):
        return f"UPDATE Department SET dept_name='{department.dept_name}' WHERE department_id={id}"
    
    
    def delete_department(department: DeleteDepartmentRequest):
        return f"DELETE FROM Department WHERE department_id={department.department_id}"
    