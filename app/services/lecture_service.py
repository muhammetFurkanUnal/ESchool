from ..repo import LectureRepo


class LectureService:
    def __init__(self):
        self.lecture_repo = LectureRepo()

    def get_all_lectures(self):
        lectures = self.lecture_repo.get_all_lectures()
        return lectures

    def get_lecture_by_id(self, lecture_id):
        lecture = self.lecture_repo.get_lecture_by_id(lecture_id)
        return lecture

    def add_lecture(self, model):
        lecture = self.lecture_repo.add_lecture(model)
        return lecture

    def update_lecture(self, model, lecture_id):
        updated_lecture = self.lecture_repo.update_lecture(model, lecture_id)
        return updated_lecture

    def delete_lecture(self, model):
        deleted_lecture = self.lecture_repo.delete_lecture(model)
        return deleted_lecture