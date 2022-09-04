class Teacher:
    """ Represents a teacher that will be paired with a school (subsequently a slot).
    """

    def __init__(self, id, preferences, qualification) -> None:
        self.id : str = id
        self.preferences : list[str] = preferences
        self.qualification : int = qualification
        self.free : bool = True
        self.school = False

    def is_free(self):
        """ Check if teacher already has a school

        Returns:
            bool: True if does not have a school
        """
        return self.free
    
    def has_pref(self):
        """ Check if teacher have at least 1 preference on preference list

        Returns:
            bool: True if has at least 1 preference
        """
        return True if self.preferences else False
    
    def set_free(self, value):
        """ Set value of free

        Args:
            value (bool): free
        """
        self.free = value

    def wants(self, school):
        """ Check if teacher wants (school is in preference list) a given school

        Args:
            school (str): school id

        Returns:
            bool: True if school in preference list
        """
        return school in self.preferences
    
    def get_first_pref(self):
        """ Get the first preference

        Returns:
            str: Id of the prefered school
        """
        return self.preferences[0]
    
    def delete_pref(self, pref):
        """ Delete a school from preference list

        Args:
            pref (str): school id
        """
        if pref in self.preferences:
            self.preferences.remove(pref)
    
    def assign(self, school):
        """ Assign teacher to some school

        Args:
            school (str): School object
        """
        self.school = school
        self.free = False
    
    def unassign(self):
        """  Unassign teacher.
        Delete assigned school and set free value as True
        """
        self.school = False
        self.free = True