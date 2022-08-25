from operator import truediv


class Teacher:

    def __init__(self, id, preferences, qualification) -> None:
        self.name = id
        self.preferences = preferences
        self.qualification = qualification
        self.free = True
    
    def is_free(self):
        return self.free
    
    def has_pref(self):
        return True if self.preferences else False
    
    def set_free(self, value):
        self.free = value

    def wants(self, school):
        return school in self.preferences
    
    def get_first_pref(self):
        return self.preferences[0]