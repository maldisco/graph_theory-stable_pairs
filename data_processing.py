def process_school_preferences(school_pref, teacher_qualifications):

    new_school_pref = {}

    for school, preferences in school_pref.items():

        new_school_pref.update
        {
            school : new_school_pref.setdefault(school, []).extend([teacher_qualifications[pref] for pref in preferences])
        }
    
    return new_school_pref