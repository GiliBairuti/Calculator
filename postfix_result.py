from MATH_OPERATORS import MathOperators
from arithmethic_functions import *

CLASS_DICT = {MathOperators.ADD.value: Add, MathOperators.SUB.value: Sub, MathOperators.MUL.value: Mul,
              MathOperators.DIV.value: Div, MathOperators.POW.value: Power, MathOperators.AVG.value: Average,
              MathOperators.MAX.value: Maximum, MathOperators.MIN.value: Minimum, MathOperators.MODULO.value: Modulo,
              MathOperators.NEG.value: Negative, MathOperators.FACTORIAL.value: Factorial,
              MathOperators.UNARY_MINUS.value: Negative}

OPERATORS = set(operator.value for operator in MathOperators)

UNARY_FUNCS = [MathOperators.FACTORIAL.value, MathOperators.NEG.value, MathOperators.UNARY_MINUS.value]


class GoingOverTheExercise:
    """
    this class's purpose is to take the postfix expression and going over it well until we
    finish and get the result of the mathematical question
    """

    @staticmethod
    def postfix_to_result(postfix_exercise: list) -> float:
        """
        This function is getting a postfix expression and return its result
        :param postfix_exercise: a list which holds a postfix expression
        :return: a float number which is the result of the expression
        """
        result = 0
        index = 0
        while len(postfix_exercise) != 1:
            if postfix_exercise[index] in OPERATORS:
                if postfix_exercise[index] in UNARY_FUNCS:
                    func = postfix_exercise.pop(index)
                    arg = postfix_exercise.pop(index - 1)
                    index -= 1

                    result = CLASS_DICT[func].resolve(arg)
                    postfix_exercise.insert(index, result)

                else:
                    func = postfix_exercise.pop(index)
                    arg2 = postfix_exercise.pop(index - 1)
                    arg1 = postfix_exercise.pop(index - 2)
                    index -= 2

                    result = CLASS_DICT[func].resolve(arg1, arg2)
                    postfix_exercise.insert(index, result)

            index += 1

        return result
