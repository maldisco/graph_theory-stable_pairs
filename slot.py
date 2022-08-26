class Slot:

    def __init__(self, preferences) -> None:
        self.preferences = preferences
        self.available = True
        self.teacher = False
    
    def set_available(self, value):
        """ Set value of available

        Args:
            value (bool): available value
        """
        self.available = value
    
    def assign(self, teacher):
        """ Assign a teacher to the slot

        Args:
            teacher (Teacher): teacher object
        """

        if(self.teacher):
            self.teacher.unassign()

        self.teacher = teacher
        self.available = False

        
