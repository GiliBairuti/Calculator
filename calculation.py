from calculator_interface import Calculator
from infix_postfix import InfixToPostfix


class Calculation(Calculator):
    """
    this class gets a string which represents a mathematical exercise and go over the string and calculate this exercise
    while refer to the priority of the operators and checking the validity of the input
    """
    @staticmethod
    def calculation_answer(infix_exercise: str) -> list:
        postfix_exercise = InfixToPostfix.infix_to_postfix(infix_exercise)
        return postfix_exercise

