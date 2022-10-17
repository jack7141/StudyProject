from .Employee import Employee


class Admin(Employee):
    def get_role(self):
        return 'administration'