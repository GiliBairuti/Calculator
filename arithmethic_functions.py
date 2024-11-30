from math_interface import ArithmeticFuncs
from math import pow


class Add(ArithmeticFuncs):
    """
    adding method between two numbers
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return arg1 + arg2


class Sub(ArithmeticFuncs):
    """
    Subtraction method between two numbers -- first number minus the second
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return arg1 - arg2


class Mul(ArithmeticFuncs):
    """
    Multiplication method between two numbers
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return arg1 * arg2


class Div(ArithmeticFuncs):
    """
    Division method between two numbers -- first number divided by the second
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return arg1 / arg2


class Power(ArithmeticFuncs):
    """
    Power method -- first number raised by the second number
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return pow(arg1, arg2)


class Average(ArithmeticFuncs):
    """
    Average method between two numbers
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return (arg1 + arg2) / 2


class Maximum(ArithmeticFuncs):
    """
    Returns the max number between the two
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return arg1 if arg1 > arg2 else arg2


class Minimum(ArithmeticFuncs):
    """
    Returns the min number between the two
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
        return arg1 if arg1 < arg2 else arg2


class Modulo(ArithmeticFuncs):
    """
    Modulo method between two numbers -- first number modulo by the second
    """
    @staticmethod
    def resolve(arg1: float, arg2: float = 0) -> float:
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
    Returns the factorial of the number
    """
    @staticmethod
    def resolve(arg: float) -> float:
        if arg == 0:
            return 1
        return arg * Factorial.resolve(arg-1)




