from abc import abstractmethod,ABC


class ArithmeticFuncs(ABC):
    """
    the abstract class of the arithmetic methods there are in the calculator
    """
    @abstractmethod
    def resolve(self, arg1, arg2=0):
        ...
