from ...models.administrator_model import *


class AdministratorQueries:
    def get_all():
        return "SELECT * FROM Administrator"


    def get_by_account_id(account_id: int):
        return f"SELECT * FROM Administrator WHERE account_id={account_id}"


    def create_administrator(administrator: CreateAdministratorRequest):
        return f"""
                INSERT INTO Administrator
                (password, username)
                VALUES (
                    '{administrator.password}', 
                    '{administrator.username}'
                );
                """


    def update_administrator(administrator:UpdateAdministratorRequest, account_id: int):
        return f"""
                UPDATE Administrator
                SET username = '{administrator.username}',
                password = '{administrator.password}'
                WHERE account_id = {account_id}
                """


    def delete_administrator(administrator:DeleteAdministratorRequest):
        return f"""
                DELETE FROM Administrator
                WHERE account_id = {administrator.account_id};
                """