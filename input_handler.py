def gather_teachers_input(filename):

    with open(filename, 'r') as file:

        teacher_qualifications = {}
        teacher_pref = {}

        for line in file.read().split('\n'):
            id, pref = line.split(':')

            teacher, qualification = id.split(",")
            pref = pref.split(",")

            teacher_qualifications.update
            {
                qualification : teacher_qualifications.setdefault(qualification, []).append(teacher)
            }

            teacher_pref.update
            {
                teacher : teacher_pref.setdefault(teacher, []).extend(pref)
            }

    return teacher_pref, teacher_qualifications

def gather_schools_input(filename):
    
    with open(filename, 'r') as file:

        school_pref = {}

        for line in file.read().split('\n'):
            data = line.split(':')
            school = data.pop(0)
            pref = data
            
            school_pref.update
            {
                school : school_pref.setdefault(school, []).extend(pref)
            }
    
    return school_pref