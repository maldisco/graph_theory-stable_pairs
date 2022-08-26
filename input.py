from teacher import Teacher
from school import School

class Input:

    def __init__(self) -> None:
        self.teacher_list = []
        self.school_list = []

    def gather(self):
        """ Gathe input from files and update school list and teacher list
        """
        with open("professores.txt", 'r') as file:
            for line in file.read().split('\n'):
                id, pref = line.split(':')

                teacher, qualification = id.split(",")
                pref = pref.split(",")

                self.teacher_list.append(Teacher(teacher, pref, int(qualification)))
        
        with open("escolas.txt", 'r') as file:
            for line in file.read().split('\n'):
                data = line.split(':')
                school = School(data.pop(0))
                
                for pref in map(int, data):
                    pref_list = []
                    for teacher in sorted(self.teacher_list, key=self._preference_sort, reverse=True):
                        if teacher.qualification >= pref and teacher.wants(school.id):
                            pref_list.append(teacher.id)
                    
                    school.add_offer(pref_list)
                
                self.school_list.append(school)
            
    def _preference_sort(self, e):
        return e.qualification