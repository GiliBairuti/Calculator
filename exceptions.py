class NegativeOperandException(Exception):
    def __init__(self, operator, operand):
        self._operator = operator
        self._operand = operand

    def __str__(self):
        return "When using %c. You can't use negative operands. Provided argument %f is not a positive number." \
               % self._operator, self._operand


class DivisionByZeroException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Division by zero isn't possible."


class ImpossibleNumberException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The number you chose isn't possible because it has 2 or more decimal points."


class WrongUnaryMinusException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Unary minus can only appear before a number."


class EmptyEquationException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "You sent an empty equation, please try again!"


class UnknownCharException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "You used an unsupported char."


class OperatorAfterOperatorException(Exception):
    def __init__(self, operator):
        self._operator = operator

    def __str__(self):
        return "The %s operator cannot appear after other operator." % self._operator


class OperatorAtFirstException(Exception):
    def __init__(self, operator):
        self._operator = operator

    def __str__(self):
        return "The %s operator cannot appear at the start of the equation." % self._operator


class WrongNegativeOperatorPlaceException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The ~ operator can appear only before a number (or signed minus)."
