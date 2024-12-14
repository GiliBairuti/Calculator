from calculation import *
from colorama import Fore, Style


def main():
    exercise = "(-6+6))"
    result = Calculation.calculation_answer(exercise)
    if type(result) is float or type(result) is int:
        print(f"{exercise} = {Calculation.calculation_answer(exercise):.4}")

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
