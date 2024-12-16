import random

from calculation import Calculation
from colorama import Fore, Style

OPTIONS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', '(', ')', '-', '+', '*', '/', '^', '@', '$', '&',
           '%', '~', '!', '#']


def main():
    for rand_equation in range(100):
        exercise = ""
        for length in range(random.randint(0,12)):
            exercise = exercise + OPTIONS[random.randint(0,len(OPTIONS) - 1)]
        print(exercise)
        result = Calculation.calculation_answer(exercise)
        if type(result) is float or type(result) is int:
            print(f"{exercise} = {Calculation.calculation_answer(exercise)}")
        else:
            exercise = exercise.replace(" ", "")
            if isinstance(result, Exception):
                print(result)
            else:
                for exception_name, exception_list in result.items():
                    message = exception_name().__str__()
                    for index_tuple in exception_list:
                        print(
                            f"{message} -> {exercise[:index_tuple[0]]}{Fore.RED}{exercise[index_tuple[0]: index_tuple[1]]}"
                            f"{Style.RESET_ALL}{exercise[index_tuple[1]:]}")


if __name__ == '__main__':
    main()
