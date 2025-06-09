from ..models.administrator_model import *
from ..database import db
from ..database.queries.administrator_queries import AdministratorQueries
from ..models.model_utils import *

class AdministratorRepo:
    def __init__(self):
        self.db = db
        
    def get_all_administrators(self):
        query = AdministratorQueries.get_all()
        administrators_raw = db.execute_query(query)
        
        if len(administrators_raw) == 0:
            return None
        
        administrators = raw_to_model(administrators_raw, Administrator)
        return administrators
    
    def get_administrator_by_account_id(self, account_id):
        query = AdministratorQueries.get_by_account_id(account_id)
        administrator_raw = db.execute_query(query)
        
        if len(administrator_raw) == 0:
            return None
        
        administrator = raw_to_model(administrator_raw, Administrator)[0]
        return administrator
    
    
    def get_administrator_by_username(self, username):
        query = AdministratorQueries.get_by_username(username)
        administrator_raw = db.execute_query(query)
        
        if len(administrator_raw) == 0:
            return None
        
        administrator = raw_to_model(administrator_raw, Administrator)[0]
        return administrator
    
    
    def add_administrator(self, model: CreateAdministratorRequest):
        query = AdministratorQueries.create_administrator(model)
        new_administrator_id = db.execute_query(query)
        administrator = self.get_administrator_by_account_id(new_administrator_id)
        return administrator
    
    
    def update_administrator(self, model: UpdateAdministratorRequest, account_id):
        query = AdministratorQueries.update_administrator(model, account_id)
        db.execute_query(query)
        administrator = self.get_administrator_by_account_id(account_id)
        return administrator
    
    
    def delete_administrator(self, model: DeleteAdministratorRequest):
        administrator = self.get_administrator_by_account_id(model.account_id)
        query = AdministratorQueries.delete_administrator(model)
        db.execute_query(query)
        return administrator
    
    
    