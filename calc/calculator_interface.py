from abc import ABC, abstractmethod


class Calculator(ABC):
    """
    the abstract class of the calc algorithm over the exercise
    """
    @staticmethod
    @abstractmethod
    def calculation_to_result(exercise: str):
        ...
