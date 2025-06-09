from ..repo import DepartmentRepo


class DepartmentService:
    def __init__(self):
        self.department_repo = DepartmentRepo()
        
        
    def get_all_departments(self):
        departments = self.department_repo.get_all_departments()
        return departments 
        
        
    def get_department_by_id(self, department_id):
        department = self.department_repo.get_department_by_id(department_id)
        return department
    
    
    def add_department(self, department_data):
        department = self.department_repo.add_department(department_data)
        return department
    
    
    def update_department(self, department_data, department_id):
        updated_department = self.department_repo.update_department(department_data, department_id)
        return updated_department
    
    
    def delete_department(self, department_data):
        department = self.department_repo.delete_department(department_data)
        return department