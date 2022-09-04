from xmlrpc.client import boolean
from teacher import Teacher
from slot import Slot


class School:
    """ Represents a school that will be paired with 1 or 2 teachers.
    """

    def __init__(self, id) -> None:
        self.id: str = id
        self.slots: list[Slot] = []

    def add_offer(self, preferences, req_qualification):
        """ Add one slot for school
        Args:
            preferences (list): List of teachers prefered
        """
        self.slots.append(Slot(preferences, req_qualification))

    def get_slots(self) -> list[Slot]:
        """ Get the list of slots

        Returns:
            list: slots
        """
        return self.slots

    def assign(self, teacher: Teacher) -> None:
        """ Assign a teacher to school.

        Args:
            teacher (Teacher): teacher object
        """

        for slot in self.get_slots():
            if slot.available and teacher.id in slot.preferences:
                slot.assign(teacher)
                teacher.assign(self)
                return
            elif teacher.id in slot.preferences and teacher.qualification <= slot.teacher.qualification:
                slot.assign(teacher)
                teacher.assign(self)
                return
        teacher.delete_pref(self.id)
     
