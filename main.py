from calculation import *


def main():
    exercise = "5&~---3!*2-(4%3)^3!"
    exercise = "5-(246#*4)-8"
    print(exercise + " = " + str(Calculation.calculation_answer(exercise)))


if __name__ == '__main__':
    main()
