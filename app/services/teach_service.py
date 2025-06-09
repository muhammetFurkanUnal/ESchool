from ..repo import TeachRepo
# from ..models.model_utils import *  # Gerekirse açılabilir

class TeachService:
    def __init__(self):
        self.teach_repo = TeachRepo()

    def get_all_teaches(self):
        teaches = self.teach_repo.get_all_teaches()
        return teaches

    def get_teach_by_teacher_and_lecture_id(self, teacher_id, lecture_id):
        teach = self.teach_repo.get_teach_by_teacher_and_lecture_id(teacher_id, lecture_id)
        return teach

    def add_teach(self, teach_data):
        teach = self.teach_repo.add_teach(teach_data)
        return teach

    def delete_teach(self, teach_data):
        deleted_teach = self.teach_repo.delete_teach(teach_data)
        return deleted_teach
