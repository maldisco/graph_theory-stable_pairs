from school import School
from teacher import Teacher
from assignment import Assignment

class Solution:

    def __init__(self, school_list, teacher_list) -> None:
        self.schools = school_list
        self.teachers = teacher_list
    

    def spa(self):

        for teacher in self.teachers:
            teacher.set_free(True)
        
        for school in self.schools:
            for slot in school.get_slots():
                slot.set_available(True)
            
        next = self._free_teacher()
        while(next):
            pref = next.get_first_pref()
            school = self._get_school(pref)

            school.assign(next)

            pass
        
    
    def _free_teacher(self):
        for teacher in self.teachers:
            if teacher.is_free() and teacher.has_pref():
                return teacher
        
        return False
    
    def _get_school(self, id):
        for school in self.schools:
            if(school.id == id):
                return school