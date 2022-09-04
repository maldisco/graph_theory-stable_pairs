from school import School
from teacher import Teacher

class Solution:
    """ Class that receives two lists (schools and teachers) and use a slightly different version of the SPA algorithm to empair each with their prefered pair.
    """

    def __init__(self, school_list, teacher_list) -> None:
        self.schools : list[School] = school_list
        self.teachers : list[Teacher] = teacher_list
    
    def spa(self):
        """ Empair teachers and schools by teachers preference
        """

        # Set teachers as free and schools as available
        for teacher in self.teachers:
            teacher.set_free(True)
        for school in self.schools:
            for slot in school.get_slots():
                slot.set_available(True)
                slot.teacher = False
        
        # While exists a free teacher
        next = self._next_free_teacher()
        while(next):
            # Get teacher's prefered school
            school = self._get_school(next.get_first_pref())
            
            # Provisionally assign teacher to school
            school.assign(next)

            # Remove worse teachers if school slot is full
            for slot in school.get_slots():
                if not slot.available:
                    for teacher in self._get_invalid_teachers(slot.get_preferences(), slot.teacher.qualification):
                        slot.remove_pref(teacher.id)
            
            # Get next free teacher
            next = self._next_free_teacher()
        
    def __str__(self) -> str:
        stable_teachers = 0
        stable_pairs = "---- Teachers allocation ----\n"
        for teacher in self.teachers:
            if(teacher.school):
                stable_pairs += f"Teacher {teacher.id} is paired with {teacher.school.id}\n"
                stable_teachers += 1
            else:
                stable_pairs += f"Teacher {teacher.id} could not get a pair\n"
        
        stable_pairs += "\n\n----  Schools Allocation ----\n"
        for school in self.schools:
            school_slots = f"School {school.id} is paired with "
            if(len(school.slots) == 2):
                school_slots += f"{school.slots[0].teacher.id if school.slots[0].teacher else 'noone'} and {school.slots[1].teacher.id if school.slots[1].teacher else 'noone'}\n"
            else:
                school_slots += f"{school.slots[0].teacher.id if school.slots[0].teacher else 'noone'}\n"

            stable_pairs += school_slots
        
        with open("results.txt", "w") as file:
            file.write(stable_pairs)

        stable_pairs = f"Foi possível alocar {stable_teachers} professores estavelmente.\nPara mais detalhes, foi gerado um arquivo 'results.txt' com cada pareamento."

        return stable_pairs

    def _get_invalid_teachers(self, id_list, current_qualification) -> list[Teacher]:
        """ Return a list of teachers that cant be paired with some school. Cant be paired meaning teachers that are worse than the current.

        Args:
            id_list (list[str]): list of teachers id (slot preferences)
            current_qualification (int): qualification of the teacher current alocated in the school

        Returns:
            list[Teacher]: invalid teachers
        """
        return [teacher for teacher in self.teachers if teacher.id in id_list and teacher.qualification > current_qualification]

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