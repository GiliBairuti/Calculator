from math_interface import ArithmeticFuncs
from math import pow
from exceptions import NegativeOperandException, DivisionByZeroException, FloatFactorialException, WrongPowException


class Add(ArithmeticFuncs):
    """
    Addition method between two numbers
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return arg1 + arg2


class Sub(ArithmeticFuncs):
    """
    Subtraction method between two numbers -- first number minus the second
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return arg1 - arg2


class Mul(ArithmeticFuncs):
    """
    Multiplication method between two numbers
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return arg1 * arg2


class Div(ArithmeticFuncs):
    """
    Division method between two numbers -- first number divided by the second.
    If the second argument is negative it raises an exception because we cannot divide by zero.
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float or Exception:
        if arg2 == 0:
            raise DivisionByZeroException(arg1)
        return arg1 / arg2


class Power(ArithmeticFuncs):
    """
    Power method -- first number raised by the second number
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        if arg1 < 0 and arg2 % 1 != 0:
            raise WrongPowException()
        return pow(arg1, arg2)


class Average(ArithmeticFuncs):
    """
    Average method between two numbers
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return (arg1 + arg2) / 2


class Maximum(ArithmeticFuncs):
    """
    Returns the max number between the two
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return arg1 if arg1 > arg2 else arg2


class Minimum(ArithmeticFuncs):
    """
    Returns the min number between the two
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return arg1 if arg1 < arg2 else arg2


class Modulo(ArithmeticFuncs):
    """
    Modulo method between two numbers -- first number modulo by the second
    """
    @staticmethod
    def resolve(arg1: float, arg2: float) -> float:
        return arg1 % arg2


class Negative(ArithmeticFuncs):
    """
    Returns the number with the opposite sign
    """
    @staticmethod
    def resolve(arg: float) -> float:
        return -arg


class Factorial(ArithmeticFuncs):
    """
    Returns the factorial of the number.
    If the number is negative it raises an exception.
    """
    @staticmethod
    def resolve(arg: float) -> float or Exception:
        if arg < 0:
            raise NegativeOperandException('!', arg)
        if arg % 1 != 0:
            raise FloatFactorialException(arg)

        if arg == 0:
            return 1
        return arg * Factorial.resolve(arg - 1)


class SumDigits(ArithmeticFuncs):
    """
    Returns the sum of the digits of a number.
    If the number is negative it raises an exception because this operator cannot handle negative numbers.
    """
    @staticmethod
    def resolve(arg: int) -> int or Exception:
        if arg < 0:
            raise NegativeOperandException('#', arg)

        num = str(arg)
        summary = 0
        for dig in num:
            # exponent expression
            if dig == 'e':
                raise Exception()
            if str.isdigit(dig):
                summary += int(dig)
        return summary
