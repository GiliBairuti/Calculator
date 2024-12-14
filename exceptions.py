def format_number(num: float) -> str:
    """
    This function gets a number and change it into string format. If the number is integer, so it will return it in the
    correct format and if the number is float it will return a string of the number with 3 digits after the point.
    :param num:  float or int number
    :return: string format of the number
    """
    if num % 1 == 0:
        return f"{int(num)}"
    return f"{num:.4}"


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


class ImpossibleNumberException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The number you chose isn't possible because it has 2 or more decimal points."


class WrongUnaryMinusException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Unary minus can only appear before a number."


class EmptyEquationException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "You sent an empty equation, please try again!"


class UnknownCharException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "You used an unsupported char."


class OperatorAfterOperatorException(Exception):
    def __init__(self, operator):
        self._operator = operator
        super().__init__(self._operator)

    def __str__(self):
        return "The %s operator cannot appear after other operator." % self._operator


class OperatorAtFirstException(Exception):
    def __init__(self, operator):
        self._operator = operator
        super().__init__(self._operator)

    def __str__(self):
        return "The %s operator cannot appear at the start of the equation." % self._operator


class WrongNegativeOperatorPlaceException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"The ~ operator can appear only before a number (or signed minus)."


class BracketsWithoutEndOrStartException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"In math every opening bracket must also have a closing bracket."
    
