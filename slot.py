from teacher import Teacher

class Slot:

    def __init__(self, preferences : list[str], req_qualification : int) -> None:
        self.preferences : list[str] = preferences
        self.available : bool = True
        self.teacher : Teacher = False
        self.required_qualification : int = req_qualification

    def get_teacher(self) -> Teacher:
        return self.teacher

    def get_preferences(self) -> list[str]:
        return self.preferences
    
    def set_available(self, value) -> None:
        """ Set value of available

        Args:
            value (bool): available value
        """
        self.available = value
    
    def assign(self, teacher : Teacher) -> None:
        """ Assign a teacher to the slot

        Args:
            teacher (Teacher): teacher object
        """

        if(self.teacher):
            self.teacher.unassign()

        self.teacher = teacher
        self.available = False

    def remove_pref(self, teacher_id) -> None:
        """ Remove a teacher from preferences

        Args:
            teacher_id (str): id of the teacher to be removed
        """
        self.preferences.remove(teacher_id)