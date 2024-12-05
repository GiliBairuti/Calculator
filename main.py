from calculation import *


def main():
    exercise = "9+5*3-(2@6)/2"
    print(exercise + " = " + str(Calculation.calculation_answer(exercise)))


if __name__ == '__main__':
    main()
