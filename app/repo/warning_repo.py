from ..models.warning_model import *
from ..database import db
from ..database.queries.warning_queries import WarningQueries
from ..models.model_utils import *

class WarningRepo:
    def __init__(self):
        self.db = db

    def get_all_warnings(self):
        query = WarningQueries.get_all()
        warnings_raw = db.execute_query(query)

        if len(warnings_raw) == 0:
            return None

        warnings = raw_to_model(warnings_raw, Warning)
        return warnings

    def get_warning_by_id(self, warning_id):
        query = WarningQueries.get_by_id(warning_id)
        warning_raw = db.execute_query(query)

        if len(warning_raw) == 0:
            return None

        warning = raw_to_model(warning_raw, Warning)[0]
        return warning

    def add_warning(self, model: CreateWarningRequest):
        query = WarningQueries.create_warning(model)
        new_warning_id = db.execute_query(query)
        warning = self.get_warning_by_id(new_warning_id)
        return warning

    def update_warning(self, model: UpdateWarningRequest, warning_id):
        query = WarningQueries.update_warning(model, warning_id)
        db.execute_query(query)
        warning = self.get_warning_by_id(warning_id)
        return warning

    def delete_warning(self, model: DeleteWarningRequest):
        warning = self.get_warning_by_id(model.warning_id)
        query = WarningQueries.delete_warning(model)
        db.execute_query(query)
        return warning