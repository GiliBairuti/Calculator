from abc import ABC, abstractmethod


class Calculator(ABC):
    """
    the abstract class of the calculation algorithm over the exercise
    """
    @staticmethod
    @abstractmethod
    def calculation_answer(exercise: str):
        ...
