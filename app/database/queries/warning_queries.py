from ...models.warning_model import *

class WarningQueries:
    def get_all():
        return "SELECT * FROM Warning"


    def get_by_id(warning_id: int):
        return f"SELECT * FROM Warning WHERE warning_id = {warning_id}"

    
    def create_warning(warning: CreateWarningRequest):
        return f"""
                INSERT INTO Warning
                (date, warning_text, administrator_id)
                VALUES (
                    '{warning.date}', 
                    '{warning.warning_text}', 
                    {warning.administrator_id}
                );
                """

    
    def update_warning(warning: UpdateWarningRequest, warning_id: int):
        return f"""
                UPDATE Warning
                SET 
                    date = '{warning.date}',
                    warning_text = '{warning.warning_text}',
                    administrator_id = {warning.administrator_id}
                WHERE warning_id = {warning_id};
                """

    
    def delete_warning(warning: DeleteWarningRequest):
        return f"""
                DELETE FROM Warning
                WHERE warning_id = {warning.warning_id};
                """
