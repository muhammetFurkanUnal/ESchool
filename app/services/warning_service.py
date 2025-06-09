from ..repo import WarningRepo


class WarningService:
    def __init__(self):
        self.warning_repo = WarningRepo()

    def get_all_warnings(self):
        warnings = self.warning_repo.get_all_warnings()
        return warnings

    def get_warning_by_id(self, warning_id):
        warning = self.warning_repo.get_warning_by_id(warning_id)
        return warning

    def add_warning(self, model):
        warning = self.warning_repo.add_warning(model)
        return warning

    def update_warning(self, model, warning_id):
        updated_warning = self.warning_repo.update_warning(model, warning_id)
        return updated_warning

    def delete_warning(self, model):
        deleted_warning = self.warning_repo.delete_warning(model)
        return deleted_warning