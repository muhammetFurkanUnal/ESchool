from ..repo import TakeRepo
# from ..models.model_utils import *  # Gerekirse açılabilir

class TakeService:
    def __init__(self):
        self.take_repo = TakeRepo()

    def get_all_takes(self):
        takes = self.take_repo.get_all_takes()
        return takes

    def get_take_by_student_and_lecture_id(self, student_id, lecture_id):
        take = self.take_repo.get_take_by_student_and_lecture_id(student_id, lecture_id)
        return take

    def add_take(self, take_data):
        take = self.take_repo.add_take(take_data)
        return take

    def update_take(self, take_data, student_id, lecture_id):
        updated_take = self.take_repo.update_take(take_data, student_id, lecture_id)
        return updated_take

    def delete_take(self, take_data):
        deleted_take = self.take_repo.delete_take(take_data)
        return deleted_take
