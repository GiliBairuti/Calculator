from calculator_interface import Calculator
from infix_postfix import InfixToPostfix
from postfix_result import GoingOverTheExercise


class Calculation(Calculator):
    """
    this class gets a string which represents a mathematical exercise and go over the string and calculate this exercise
    while refer to the priority of the operators and checking the validity of the input
    """
    @staticmethod
    def calculation_answer(infix_exercise: str) -> list or dict:
        postfix_exercise = InfixToPostfix.infix_to_postfix(infix_exercise)
        if type(postfix_exercise) is dict:  # exceptions were found in the infix to postfix part
            return postfix_exercise    # exceptions dict
        return GoingOverTheExercise.postfix_to_result(postfix_exercise)

