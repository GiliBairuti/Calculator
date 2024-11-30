from math_interface import ArithmeticFuncs


class Add(ArithmeticFuncs):
    """
    adding method between two numbers
    """
    def resolve(self, arg1:float, arg2=0) -> float:
        return arg1 + arg2


class Sub(ArithmeticFuncs):
    """
    Subtraction method between two numbers -- first number minus the second
    """
    def resolve(self, arg1:float, arg2=0) -> float:
        return arg1 - arg2

