from ..models.department_model import *
from ..database import db
from ..database.queries import DepartmentQueries
from ..models.model_utils import *

class DepartmentRepo:
    def __init__(self):
        self.db = db
        
    def get_all_departments(self):
        query = DepartmentQueries.get_all()
        departments_raw = db.execute_query(query)
        
        
        if len(departments_raw) == 0:
            return None
        
        departments = raw_to_model(departments_raw, Department)
        return departments  
    
    
    def get_department_by_id(self, department_id):
        query = DepartmentQueries.get_by_id(department_id)
        department_raw = db.execute_query(query)
        
        if len(department_raw) == 0:
            return None
        
        department = raw_to_model(department_raw, Department)[0]
        return department
    
    
    def add_department(self, model: CreateDepartmentRequest):
        query = DepartmentQueries.create_department(model)
        new_department_id = db.execute_query(query)
        department = self.get_department_by_id(new_department_id)
        return department  
    
    
    def update_department(self, model: UpdateDepartmentRequest, department_id):
        query = DepartmentQueries.update_department(model, department_id)
        db.execute_query(query)
        department = self.get_department_by_id(department_id)
        return department
    
    
    def delete_department(self, model: DeleteDepartmentRequest):
        department = self.get_department_by_id(model.department_id)
        query = DepartmentQueries.delete_department(model)
        db.execute_query(query)
        return department
    