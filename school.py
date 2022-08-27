from teacher import Teacher
from slot import Slot

class School:

    def __init__(self, id) -> None:
        self.id : str = id
        self.slots : list[Slot] = []

    def add_offer(self, preferences):
        """ Add one slot for school
        Args:
            preferences (list): List of teachers prefered
        """  
        self.slots.append(Slot(preferences))
    
    def get_slots(self) -> list[Slot]:
        """ Get the list of slots

        Returns:
            list: slots
        """
        return self.slots
    
    def _choose_slot(self, teacher) -> Slot:
        """ Pick one slot according to teacher. If teacher is in slot preferences.

        Args:
            teacher (Teacher): teacher object

        Returns:
            Slot: slot object
        """
        for slot in self.slots:
            if slot.available and teacher.id in slot.preferences:
                return slot

        for slot in self.slots:
            if teacher.id in slot.preferences:
                return slot
        
        return False

    def _pick_worst_between(self, teacher1, teacher2, preferences) -> Teacher:
        """ Pick the worst teacher between two options. Based on rank in preference list

        Args:
            teacher1 (Teacher): option 1
            teacher2 (Teacher): option 2
            preferences (list): preference list

        Returns:
            Teacher: The worst teacher
        """
        for i in range(len(preferences)):
            if preferences[i] == teacher1:
                rank_teacher1 = i
            
            if preferences[i] == teacher2:
                rank_teacher2 = i
        
        return teacher2 if rank_teacher1 < rank_teacher2 else teacher1

    def assign(self, teacher: Teacher) -> None:
        """ Assign a teacher to school.

        Args:
            teacher (Teacher): teacher object
        """
        slot = self._choose_slot(teacher)
        if slot:
            if slot.available:
                slot.assign(teacher)
                teacher.assign(self)
            else:
                worst_teacher = self._pick_worst_between(teacher.id, slot.teacher.id, slot.preferences)
                if worst_teacher == slot.teacher.id:
                    slot.assign(teacher)
                    teacher.assign(self)
                else:
                    teacher.delete_pref(self.id)
                    slot.preferences.remove(teacher.id)      
        else:
            teacher.delete_pref(self.id)

    def full(self) -> bool:
        """ Check if school is full

        Returns:
            bool: True if is full
        """
        return all([not slot.available for slot in self.get_slots()])
    
    def get_invalid_pairs(self) -> list[tuple]:
        """ Get pairs of techers and school that will never be paired.\n
        A teacher and a school cant be paired if there's a better teacher allocated in that school

        Returns:
            list: list of tuples (teacher id, school id)
        """
        invalid_pairs = []

        for slot in self.get_slots():

            index = 0
            for i in  range(len(slot.preferences)):
                if slot.preferences[i] == slot.teacher.id:
                    index = i

            invalid_pairs.extend([(teacher_id, self.id) for teacher_id in slot.preferences[index+1:]])
            slot.preferences = slot.preferences[:index+1]
        

        return invalid_pairs