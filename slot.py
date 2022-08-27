from teacher import Teacher

class Slot:

    def __init__(self, preferences) -> None:
        self.preferences : list[str] = preferences
        self.available : bool = True
        self.teacher : Teacher = False

    def get_teacher(self) -> Teacher:
        return self.teacher
    
    def set_available(self, value) -> None:
        """ Set value of available

        Args:
            value (bool): available value
        """
        self.available = value
    
    def assign(self, teacher) -> None:
        """ Assign a teacher to the slot

        Args:
            teacher (Teacher): teacher object
        """

        if(self.teacher):
            self.teacher.unassign()

        self.teacher = teacher
        self.available = False

        
