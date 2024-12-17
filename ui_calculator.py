from calculation import Calculation
from colorama import Fore, Style


class UI:
    """
    This class is the user interface class -
    It has some functions that make the client use being much easier and more understandable and accessible
    """

    @staticmethod
    def opening_explain():
        """
        This function prints the first explanation about the calculator. This explanation appears when we open the calc.
        """
        print(f'Welcome to my calculator :) \nIn this calculator you can use a lot of functions.\n'
              f'[+,-,*,/,^,@,$,&,%,~,!,#]\nEnter "help" to see the deep explanation about the operators.\n'
              f'Enter "exit" to exit from the calculator.')

    @staticmethod
    def full_explain():
        """
        This function prints the deeper explanation about every function. This explanation appears when we enter "help".
        """
        print(f'\n"+" - Addition operator.\n'
              f'"-" - Subtraction operator.\n'
              f'"/" - Division operator.\n'
              f'"*" - Multiplication operator.\n'
              f'"^" - Power operator between two numbers - x^y.\n'
              f'"@" - Average between two numbers x@y.\n'
              f'"$" - Maximum number between the two.\n'
              f'"&" - Minimum number between the two.\n'
              f'"%" - Modulo operator.\n'
              f'"~" - Negative operator - gets a number and changes its sign.\n'
              f'"!" - Factorial operator - x!.\n'
              f'"#" - Summary digits operator - x#, gets a number and summary its digits.\n')

    @staticmethod
    def check_result(equation: str):
        """
        This function gets the equation and send it to the calculator.Then it handles the result,
        if it is an exception it prints it, if it is a dict of exceptions it sends them to other function to print them.
        Otherwise, it prints the result in the correct format.
        :param equation: the equation the client entered
        """
        result = Calculation.calculation_answer(equation)
        if type(result) is float or type(result) is int:
            UI.print_result(equation, result)
        else:
            equation = equation.replace(" ", "")
            if isinstance(result, Exception):
                print(result)
            else:
                UI.print_exceptions(equation, result)

    @staticmethod
    def print_result(equation: str, result: float or int):
        """
        This function gets the equation and the result, and it prints the result in the correct format.
        :param equation: the equation the client entered
        :param result: the result of the equation
        """
        if result % 1 == 0:
            print(f"{equation} = {int(result)}")
        else:
            print(f"{equation} = {result}")

    @staticmethod
    def print_exceptions(equation: str, exceptions_dict: dict):
        """
         This function gets the equation and the dictionary of exception that were found.
         The function prints all the exceptions and sign the mistake on the equation.
         :param equation: the equation the client entered
         :param exceptions_dict: a dictionary - key = Exception type, Value = tuple of start index and end index of the exception.
         """
        for exception_name, exception_list in exceptions_dict.items():
            message = exception_name().__str__()
            for index_tuple in exception_list:
                print(
                    f"{message} -> {equation[:index_tuple[0]]}{Fore.RED}{equation[index_tuple[0]: index_tuple[1]]}"
                    f"{Style.RESET_ALL}{equation[index_tuple[1]:]}")
