from calculation import *

def main():
    exercise = "5&~---3!*2-(4%3)^3!"
    exercise = "5-(246#*4)-8"
    exercise = "4.56-3.12."
    result = Calculation.calculation_answer(exercise)
    if type(result) is float or type(result) is int:
        print(exercise + " = " + str(Calculation.calculation_answer(exercise)))
    else:
        for exception in result:



if __name__ == '__main__':
    main()
