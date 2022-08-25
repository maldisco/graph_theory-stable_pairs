from teacher import Teacher
from slot import Slot

class School:

    def __init__(self, id, number_of_slots) -> None:
        self.id = id
        self.number_of_slots = number_of_slots
        self.slots = []
        self.assigned = []

    def add_offer(self, preferences):
        pref = []
        for teacher in preferences:
            if(teacher.wants(self.id)):
                pref.append(teacher)
        
        self.slots.append(Slot(pref))
    
    def get_slots(self):
        return self.slots
    
    def assign(self, teacher):
        return

        