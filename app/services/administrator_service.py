from ..repo import AdministratorRepo
from ..auth import hash_password


class AdministratorService:
    def __init__(self):
        self.administrator_repo = AdministratorRepo()

    def get_administrator_by_account_id(self, account_id):
        administrator = self.administrator_repo.get_administrator_by_account_id(account_id)
        return administrator

    def get_all_administrators(self):
        administrators = self.administrator_repo.get_all_administrators()
        return administrators

    def add_administrator(self, administrator_data):
        administrator_data.password = hash_password(administrator_data.password)
        administrator = self.administrator_repo.add_administrator(administrator_data)
        return administrator

    def update_administrator(self, administrator_data, account_id):
        updated_administrator = self.administrator_repo.update_administrator(administrator_data, account_id)
        return updated_administrator

    def delete_administrator(self, administrator_data):
        administrator = self.administrator_repo.delete_administrator(administrator_data)
        return administrator