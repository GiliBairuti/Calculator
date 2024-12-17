from MATH_OPERATORS import MathOperators
from arithmethic_functions import *
from exceptions import TooLongNumberException, NegativeOperandException, DivisionByZeroException, FloatFactorialException, WrongPowException


CLASS_DICT = {MathOperators.ADD.value: Add, MathOperators.SUB.value: Sub, MathOperators.MUL.value: Mul,
              MathOperators.DIV.value: Div, MathOperators.POW.value: Power, MathOperators.AVG.value: Average,
              MathOperators.MAX.value: Maximum, MathOperators.MIN.value: Minimum, MathOperators.MODULO.value: Modulo,
              MathOperators.NEG.value: Negative, MathOperators.FACTORIAL.value: Factorial,
              MathOperators.UNARY_MINUS.value: Negative, MathOperators.SUM_DIGIT.value: SumDigits}

OPERATORS = set(operator.value for operator in MathOperators)

UNARY_FUNCS = [MathOperators.FACTORIAL.value, MathOperators.NEG.value,
               MathOperators.UNARY_MINUS.value, MathOperators.SUM_DIGIT.value]

MATH_EXCEPTIONS = [NegativeOperandException, DivisionByZeroException, FloatFactorialException, WrongPowException]


class GoingOverTheExercise:
    """
    this class's purpose is to take the postfix expression and going over it well until we
    finish and get the result of the mathematical question
    """

    @staticmethod
    def postfix_to_result(postfix_exercise: list) -> float or Exception:
        """
        This function is getting a postfix expression and return its result, if there is a mathematical problem it
        returns a specific exception with the problem.
        :param postfix_exercise: a list which holds a postfix expression
        :return: a float number which is the result of the expression or an exception
        """
        # checks if got only a number
        if len(postfix_exercise) == 1:
            return postfix_exercise[0]

        result = 0
        index = 0
        while len(postfix_exercise) != 1:
            if postfix_exercise[index] in OPERATORS:
                if postfix_exercise[index] in UNARY_FUNCS:
                    func = postfix_exercise.pop(index)
                    arg = postfix_exercise.pop(index - 1)
                    index -= 1

                    try:
                        result = CLASS_DICT[func].resolve(arg)
                    except Exception as e:
                        if type(e) not in MATH_EXCEPTIONS:  # making sure it is a python exception and not our custom exceptions
                            raise TooLongNumberException()
                        raise   # raising our custom exception

                else:
                    func = postfix_exercise.pop(index)
                    arg2 = postfix_exercise.pop(index - 1)
                    arg1 = postfix_exercise.pop(index - 2)
                    index -= 2

                    try:
                        result = CLASS_DICT[func].resolve(arg1, arg2)
                    except Exception as e:
                        if type(e) not in MATH_EXCEPTIONS:  # making sure it is a python exception and not our custom exceptions
                            raise TooLongNumberException()
                        raise   # raising our custom exception

                postfix_exercise.insert(index, result)

            index += 1

        return result
