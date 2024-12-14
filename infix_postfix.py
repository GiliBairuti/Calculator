from MATH_OPERATORS import MathOperators
from exceptions import OperatorAtFirstException, OperatorAfterOperatorException, WrongNegativeOperatorPlaceException, \
    WrongUnaryMinusException, EmptyEquationException, ImpossibleNumberException, \
    UnknownCharException, BracketsWithoutEndOrStartException

# I chose to call 'U' as unary-minus
OPERATORS_PRIORITY_DICT = {MathOperators.ADD.value: 1, MathOperators.SUB.value: 1, MathOperators.MUL.value: 2,
                           MathOperators.DIV.value: 2, MathOperators.POW.value: 3, MathOperators.AVG.value: 5,
                           MathOperators.MAX.value: 5, MathOperators.MIN.value: 5, MathOperators.MODULO.value: 4,
                           MathOperators.NEG.value: 6, MathOperators.FACTORIAL.value: 6,
                           MathOperators.UNARY_MINUS.value: 2.5, MathOperators.SUM_DIGIT.value: 6}

EXCEPTIONS_DICT = dict()


class InfixToPostfix:
    """
    This class's purpose is to change infix expression to postfix expression
    """

    @staticmethod
    def infix_to_postfix(infix_exercise: str) -> list or dict:
        """
        This function gets a string which is a math exercise in infix,
        and change it into a list of the numbers and the chars of the operators in a list ordered in postfix.
        :param infix_exercise: holding a string which represents a mathematical infix expression
        :return: list which includes the same math exercise but in postfix or exceptions dictionary
        """
        # remove the meaningless spaces
        infix_exercise = infix_exercise.replace(' ', '')

        operators = []
        postfix_exercise = []
        index = 0

        while index != len(infix_exercise):
            # operand
            if str.isdigit(infix_exercise[index]):
                postfix_exercise, index = InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index)

            # operator
            else:
                infix_exercise, postfix_exercise, operators, index = \
                    InfixToPostfix._operator_handling(infix_exercise, postfix_exercise, operators, index)

        bracket_index = -1
        # add the operators that are left
        while len(operators) != 0:
            if operators[-1] == '(':  # there is an opening bracket without closing
                bracket_index = infix_exercise.index('(', bracket_index + 1, len(infix_exercise))
                InfixToPostfix.adding_exception(BracketsWithoutEndOrStartException, bracket_index, bracket_index + 1)
            postfix_exercise.append(operators.pop(len(operators) - 1))

        if len(EXCEPTIONS_DICT) != 0:  # there are exceptions in this part
            return EXCEPTIONS_DICT

        return postfix_exercise

    @staticmethod
    def _operand_handling(infix_exercise: str, postfix_exercise: list, index: int,
                          flag: bool = False) -> list and int:
        """
        This class gets a string of infix expression, a list of the postfix expression and an index which
        point on the start of the number. The class adds the full number (can be floated) to the postfix list.
        :param infix_exercise: a string which is an infix expression
        :param postfix_exercise: a list which handled part of the postfix expression of the infix_exercise
        :param index: the start index of the operand we are going on right now
        :param flag: boolean parameter that signs if the number is negative number according to the unary minuses
        :return: all the updated variables
        """
        start_of_number_index = index
        decimal_point = False
        is_exception = False
        while (index + 1 != len(infix_exercise)) and (
                str.isdigit(infix_exercise[index + 1]) or (infix_exercise[index + 1] == '.')):
            if infix_exercise[index + 1] == '.':
                if decimal_point is True:  # this number has or more decimal points
                    is_exception = True
                decimal_point = True
            index += 1

        index += 1

        # the number isn't logic - has more than one decimal point
        if is_exception:
            InfixToPostfix.adding_exception(ImpossibleNumberException, start_of_number_index, index)

        else:
            # negative number
            if flag:
                postfix_exercise.append(-float(infix_exercise[start_of_number_index:index]))

            # positive number
            else:
                postfix_exercise.append(float(infix_exercise[start_of_number_index:index]))

        return postfix_exercise, index

    @staticmethod
    def _operator_handling(infix_exercise: str, postfix_exercise: list, operators: list,
                           index: int) -> str and list and list and int:
        """
        This class gets a string of infix expression, a list of the postfix expression, a list with operators
        and an index which point on the start of a number.
        The class handles with an operator according to the postfix representation
        :param infix_exercise: a string which is an infix expression
        :param postfix_exercise: a list which handled part of the postfix expression of the infix_exercise
        :param operators: a list with the operators that were left
        :param index: the start index of the operand we are going on right now
        :return: all the updated variables
        """
        # the treatment of brackets is different because it always in the first priority
        if infix_exercise[index] == ')':
            while len(operators) != 0 and operators[-1] != '(':
                postfix_exercise.append(operators.pop())
            if len(operators) == 0:
                InfixToPostfix.adding_exception(BracketsWithoutEndOrStartException, index, index + 1)
            else:
                operators.pop()
            index += 1
            return infix_exercise, postfix_exercise, operators, index

        # checking if it is a unary-minus and replace it to my custom char if its necessary
        if infix_exercise[index] == '-' and (index == 0 or not str.isdigit(infix_exercise[index - 1])):
            # checks if it is a unary minus which after an operator or not
            if index == 0 or infix_exercise[index - 1] == '(' or infix_exercise[index - 1] == 'U':
                infix_exercise = infix_exercise[:index] + 'U' + infix_exercise[index + 1:]
            else:
                postfix_exercise, index = InfixToPostfix._strong_unary_minus(infix_exercise, postfix_exercise, index)
                # in this situation we already handled the operator (unary-minus) so we can go back
                return infix_exercise, postfix_exercise, operators, index

        while len(operators) != 0 and len(postfix_exercise) != 0 and \
                InfixToPostfix._stronger_operator(operators[-1], infix_exercise[index]):
            postfix_exercise.append(operators.pop())
        operators.append(infix_exercise[index])
        index += 1
        return infix_exercise, postfix_exercise, operators, index

    @staticmethod
    def _negative_handling(infix_exercise: str, postfix_exercise: list, index: int) -> str and list:
        """
        This func gets an infix expression which starts with ~ and handling this ~ operator.
        Negative operator is the only infix operator, so we have to handle it differently.
        :param infix_exercise: a string which is an infix expression
        :param postfix_exercise: a list which handled part of the postfix expression of the infix_exercise
        :param index: the ~ index in the infix expression
        :return: the updated variables
        """
        index += 1
        while not str.isdigit(infix_exercise[index]):
            index += 1
        postfix_exercise, end_of_num = InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index)

        # removing the number from the expression
        infix_exercise = infix_exercise[:index] + infix_exercise[end_of_num:]
        return infix_exercise, postfix_exercise

    @staticmethod
    def _stronger_operator(operator1: chr, operator2: chr) -> chr:
        """
        This func gets 2 chars of arithmetic signs and return True if the first one
        is primer than the second one, otherwise False.
        :param operator1: operator
        :param operator2: operator
        :return: boolean variable
        """
        if operator1 == '(' or operator2 == '(':
            return False

        # because unary minus can repeat several times one after the other
        if operator1 == 'U':
            return True if OPERATORS_PRIORITY_DICT[operator1] > OPERATORS_PRIORITY_DICT[operator2] else False

        return True if OPERATORS_PRIORITY_DICT[operator1] >= OPERATORS_PRIORITY_DICT[operator2] else False

    @staticmethod
    def _strong_unary_minus(infix_exercise: str, postfix_exercise: list, index: int) -> list and int:
        """
       This func gets an infix expression, index in it and postfix expression. The index is the start of a number
       which starts with unary minus, it has to count the minuses and check if the number is positive or negative
       according to the minuses. The function returns the updated postfix expression with the number,
       and the first index after the number end.
       :param infix_exercise:   infix expression
       :param postfix_exercise: postfix expression
       :return: updated valuables
       """
        counter = 0
        while infix_exercise[index] == '-' and index != len(infix_exercise):
            counter += 1
            index += 1

        if index == len(infix_exercise):
            # raise exception
            print("frf")

        # positive number
        if counter % 2 == 0:
            return InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index)

        # negative number
        return InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index, True)

    @staticmethod
    def adding_exception(exception_key: Exception, start_index: int, end_index: int):
        """
        This function is getting an exception and add it to the exception's dictionary, if there is already this type
        of exception it adds the new one and keeps the previous exceptions.
        :param exception_key: the name of the exception
        :param start_index: the starting index of the problem
        :param end_index: the end index of the problem
        """
        if exception_key in EXCEPTIONS_DICT:  # checks if we already have this exception, to not override it.
            EXCEPTIONS_DICT[exception_key].append((start_index, end_index))
        else:
            EXCEPTIONS_DICT[exception_key] = [(start_index, end_index)]
