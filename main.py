from input import Input
from solution import Solution

if __name__ == '__main__':
    input_handler = Input()
    input_handler.gather()

    solution = Solution(input_handler.school_list, input_handler.teacher_list)
    solution.spa()
    print(solution)