from school import School
from teacher import Teacher
import time

class Solution:

    def __init__(self, school_list, teacher_list) -> None:
        self.schools : list[School] = school_list
        self.teachers : list[Teacher] = teacher_list
    
    def spa(self):
        """ Empair teachers and schools by teachers preference
        """

        for teacher in self.teachers:
            teacher.set_free(True)
        
        for school in self.schools:
            for slot in school.get_slots():
                slot.set_available(True)
            
        next = self._next_free_teacher()
        while(next):
            pref = next.get_first_pref()
            school = self._get_school(pref)
            school.assign(next)

            for slot in school.get_slots():
                if not slot.available:

                    for teacher in self._get_invalid_teachers(slot.get_preferences(), slot.required_qualification, slot.teacher.qualification):

                        slot.remove_pref(teacher.id)

            next = self._next_free_teacher()

    def pre_print(self) -> None:
        """test
        """

        for school in self.schools:
            for slot in school.get_slots():

                print(f"School {school.id} prefers {slot.preferences}")

    def __str__(self) -> str:
        stable_pairs = "---- Teachers allocation ----\n"
        for teacher in self.teachers:
            if(teacher.school):
                stable_pairs += f"Teacher {teacher.id} is paired with {teacher.school.id}\n"
            else:
                stable_pairs += f"Teacher {teacher.id} could not get a pair\n"
        
        stable_pairs += "----  Schools Allocation ----\n"
        for school in self.schools:
            school_slots = f"School {school.id} is paired with "
            if(len(school.slots) == 2):
                school_slots += f"{school.slots[0].teacher.id if school.slots[0].teacher else 'noone'} and {school.slots[1].teacher.id if school.slots[1].teacher else 'noone'}\n"
            else:
                school_slots += f"{school.slots[0].teacher.id if school.slots[0].teacher else 'noone'}\n"

            stable_pairs += school_slots

        return stable_pairs
    
    def _get_invalid_teachers(self, id_list, req_qualification, current_qualification) -> list[Teacher]:
        if req_qualification == current_qualification:
            return [teacher for teacher in self.teachers if teacher.id in id_list]
        else:
            return [teacher for teacher in self.teachers if teacher.id in id_list and teacher.qualification != req_qualification]

    def _next_free_teacher(self) -> Teacher:
        """ Find a teacher that is both free and has a non-empty preference list

        Returns:
            Teacher: The next free teacher (or False if not found)
        """
        for teacher in self.teachers:
            if teacher.is_free() and teacher.has_pref():
                return teacher
        
        return False
    
    def _get_school(self, id) -> School:
        """ Get School objet from school id

        Args:
            id (str): School id

        Returns:
            School: School object
        """
        for school in self.schools:
            if(school.id == id):
                return school