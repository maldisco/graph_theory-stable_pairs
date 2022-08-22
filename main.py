import input_handler
import data_processing
from algorithm import find_stable_pairs

if __name__ == '__main__':
    teacher_pref, teacher_qualifications = input_handler.gather_teachers_input('professores.txt')
    school_pref = data_processing.process_school_preferences(input_handler.gather_schools_input('escolas.txt'), teacher_qualifications)

    find_stable_pairs(school_pref, teacher_pref)