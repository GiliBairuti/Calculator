from abc import abstractmethod,ABC


class ArithmeticFuncs(ABC):
    """
    the abstract class of the arithmetic methods there are in the calculator
    """
    @classmethod
    @abstractmethod
    def resolve(cls, arg1, arg2=0):
        ...
