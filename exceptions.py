def format_number(num: float) -> str:
    """
    This function gets a number and change it into string format. If the number is integer, it will return it in the
    correct format and if the number is float it will return a string of the number with 3 digits after the point.
    :param num:  float or int number
    :return: string format of the number
    """
    if num % 1 == 0:
        return f"{int(num)}"
    return "%.3f" % num


class NegativeOperandException(Exception):
    def __init__(self, operator, operand):
        self._operator = operator
        self._operand = operand
        super().__init__(self._operator, self._operand)

    def __str__(self):
        return f"When using - {self._operator}, you can't use negative operands. Provided argument:" \
               f" {format_number(self._operand)} is not a positive number."


class DivisionByZeroException(Exception):
    def __init__(self, operand):
        self._operand = operand
        super().__init__(self._operand)

    def __str__(self):
        return f"Division by zero isn't possible. You tried to divide {format_number(self._operand)} by zero."


class FloatFactorialException(Exception):
    def __init__(self, operand):
        self._operand = operand
        super().__init__(self._operand)

    def __str__(self):
        return f"Factorial on float numbers isn't possible. You tried to calculate the factorial of " \
               f"{format_number(self._operand)}"


class WrongPowException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Power cannot get a negative base and a float exponent, because its like negative sqrt."


class ImpossibleNumberException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The number you chose isn't possible because it has 2 or more decimal points"


class EmptyEquationException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "You sent an empty equation, please try again!"


class UnknownCharException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "You used an unsupported char"


class OperatorAfterOperatorException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Operator cannot appear after an operator unless it is a prefix operator"


class OperatorAtFirstException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Every equation has to start with a number or prefix operator"


class OperatorAtLastException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Every equation has to end with a number or postfix operator"


class NegativeOperatorException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The ~ operator can appear only at the start of the equation, or after binary operators, or after '('"


class UnaryMinusPlaceException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Unary minus can appear only before a number or additional unary minus"


class PostfixOperatorException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "After a postfix operator we can get only an operator or ')'"


class BracketsWithoutEndOrStartException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"In math every opening bracket must also have a closing bracket"


class WrongBracketsPlaceException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Opening and closing brackets can appear only after and before operators (similar to operands)"


class EmptyBracketsException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Empty brackets aren't making sense... Put something in the brackets"


class DecimalPointException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Float numbers must contain digits before the decimal point"


class TooLongNumberException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"This number is too long, so the calculator can't handle it."
