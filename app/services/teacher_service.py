from ..repo import TeacherRepo


class TeacherService:
    def __init__(self):
        self.teacher_repo = TeacherRepo()

    def get_teacher_by_account_id(self, account_id):
        teacher = self.teacher_repo.get_teacher_by_account_id(account_id)
        return teacher

    def get_all_teachers(self):
        teachers = self.teacher_repo.get_all_teachers()
        return teachers

    def add_teacher(self, teacher_data):
        teacher = self.teacher_repo.add_teacher(teacher_data)
        return teacher

    def update_teacher(self, teacher_data, account_id):
        updated_teacher = self.teacher_repo.update_teacher(teacher_data, account_id)
        return updated_teacher

    def delete_teacher(self, teacher_data):
        teacher = self.teacher_repo.delete_teacher(teacher_data)
        return teacher