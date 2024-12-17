from MATH_OPERATORS import MathOperators
from exceptions import OperatorAtFirstException, OperatorAfterOperatorException, ImpossibleNumberException, \
    UnknownCharException, BracketsWithoutEndOrStartException, OperatorAtLastException, WrongBracketsPlaceException, \
    EmptyBracketsException, NegativeOperatorException, UnaryMinusPlaceException, DecimalPointException, \
    PostfixOperatorException

# I chose to call 'U' as unary-minus
OPERATORS_PRIORITY_DICT = {MathOperators.ADD.value: 1, MathOperators.SUB.value: 1, MathOperators.MUL.value: 2,
                           MathOperators.DIV.value: 2, MathOperators.POW.value: 3, MathOperators.AVG.value: 5,
                           MathOperators.MAX.value: 5, MathOperators.MIN.value: 5, MathOperators.MODULO.value: 4,
                           MathOperators.NEG.value: 6, MathOperators.FACTORIAL.value: 6,
                           MathOperators.UNARY_MINUS.value: 2.5, MathOperators.SUM_DIGIT.value: 6}

OPERATORS = set(operator.value for operator in MathOperators)

POSTFIX_OPERATORS = {MathOperators.SUM_DIGIT.value, MathOperators.FACTORIAL.value, ')'}
PREFIX_OPERATORS = {MathOperators.NEG.value, MathOperators.UNARY_MINUS.value, MathOperators.SUB.value, '('}
BINARY_OPERATORS = {MathOperators.ADD.value, MathOperators.SUB.value, MathOperators.MUL.value, MathOperators.DIV.value,
                    MathOperators.POW.value, MathOperators.AVG.value, MathOperators.MAX.value, MathOperators.MIN.value,
                    MathOperators.MODULO.value}

EXCEPTIONS_DICT = dict()


class InfixToPostfix:
    """
    This class's purpose is to change infix expression to postfix expression
    """

    @staticmethod
    def infix_to_postfix(infix_exercise: str) -> list or dict:
        """
        This function gets a string which represents a math equation in infix,
        and change it into a list of the numbers, and the chars of the operators, ordered in postfix.
        :param infix_exercise: holding a string which represents a mathematical infix expression
        :return: list which includes the same math exercise but in postfix or exceptions dictionary
        """
        # clear the exceptions from the last equation
        EXCEPTIONS_DICT.clear()

        operators = []
        postfix_exercise = []
        index = 0

        while index != len(infix_exercise):
            # operand
            if str.isdigit(infix_exercise[index]):
                index = InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index)

            # operator
            else:
                if infix_exercise[index] in OPERATORS or infix_exercise[index] in ')(':
                    index = InfixToPostfix._operator_handling(infix_exercise, postfix_exercise, operators, index)

                else:
                    if infix_exercise[index] == '.':
                        InfixToPostfix.adding_exception(DecimalPointException, index, index + 1)

                    else:
                        InfixToPostfix.adding_exception(UnknownCharException, index, index + 1)
                    index += 1

        if not (str.isdigit(infix_exercise[-1]) or infix_exercise[-1] in POSTFIX_OPERATORS):
            InfixToPostfix.adding_exception(OperatorAtLastException, index - 1, index)

        bracket_index = -1
        # add the operators that were left
        while len(operators) != 0:
            if operators[-1] == '(':  # there is an opening bracket without closing
                bracket_index = infix_exercise.index('(', bracket_index + 1, len(infix_exercise))
                InfixToPostfix.adding_exception(BracketsWithoutEndOrStartException, bracket_index, bracket_index + 1)
            postfix_exercise.append(operators.pop(len(operators) - 1))

        if len(EXCEPTIONS_DICT) != 0:  # there are exceptions in this part
            return EXCEPTIONS_DICT

        return postfix_exercise

    @staticmethod
    def _operand_handling(infix_exercise: str, postfix_exercise: list, index: int, flag: bool = False) -> int:
        """
        This class gets a string of infix expression, a list of the postfix expression and an index which
        point on the start of the number. The class adds the full number (can be floated) to the postfix list.
        :param infix_exercise: a string which is an infix expression
        :param postfix_exercise: a list which handled part of the postfix expression of the infix_exercise
        :param index: the start index of the operand we are going on right now
        :param flag: boolean parameter that signs if the number is negative number according to the unary minuses
        :return: the updated index
        """
        # brackets exceptions checking
        if (index + 1 != len(infix_exercise) and infix_exercise[index + 1] == '(') or \
                (index != 0 and infix_exercise[index - 1] == ')'):
            InfixToPostfix.adding_exception(WrongBracketsPlaceException, index, index + 1)

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

        return index

    @staticmethod
    def _operator_handling(infix_exercise: str, postfix_exercise: list, operators: list, index: int) -> int:
        """
        This class gets a string of infix expression, a list of the postfix expression, a list with operators
        and an index which point on the start of a number.
        The class handles with an operator according to the postfix representation
        :param infix_exercise: a string which is an infix expression
        :param postfix_exercise: a list which handled part of the postfix expression of the infix_exercise
        :param operators: a list with the operators that were left
        :param index: the start index of the operand we are going on right now
        :return: the updated index
        """
        # the treatment of brackets is different because it always in the first priority
        if infix_exercise[index] == ')':
            if infix_exercise[index - 1] == '(':
                InfixToPostfix.adding_exception(EmptyBracketsException, index - 1, index + 1)
            if infix_exercise[index - 1] in OPERATORS and infix_exercise[index - 1] not in POSTFIX_OPERATORS:
                InfixToPostfix.adding_exception(WrongBracketsPlaceException, index - 1, index + 1)
            while len(operators) != 0 and operators[-1] != '(':
                postfix_exercise.append(operators.pop())
            if len(operators) == 0:
                InfixToPostfix.adding_exception(BracketsWithoutEndOrStartException, index, index + 1)
            else:
                operators.pop()
            index += 1
            return index

        # checking if it is a unary-minus and replace it to my custom char if its necessary
        if infix_exercise[index] == MathOperators.SUB.value and index == 0 or \
                infix_exercise[index - 1] not in POSTFIX_OPERATORS and \
                (infix_exercise[index - 1] in OPERATORS or infix_exercise[index - 1] == '('):
            # checks if it is a unary minus which appears at the start of an expression or a sign minus
            if index == 0 or infix_exercise[index - 1] == '(' or \
                    infix_exercise[index - 1] == MathOperators.UNARY_MINUS.value:
                infix_exercise = infix_exercise[:index] + MathOperators.UNARY_MINUS.value + infix_exercise[index + 1:]
                if index + 1 != len(infix_exercise) and not (
                        str.isdigit(infix_exercise[index + 1]) or infix_exercise[index + 1] == MathOperators.SUB.value):
                    InfixToPostfix.adding_exception(UnaryMinusPlaceException, index, index + 1)
            else:
                post = False
                if infix_exercise[index - 1] in POSTFIX_OPERATORS:
                    postfix_exercise.append(operators.pop())
                    post = True
                index = InfixToPostfix._strong_unary_minus(infix_exercise, index, operators)

                if post:  # if the operator before the unary minus is a postfix operator than we have to add +
                    postfix_exercise.append(MathOperators.ADD.value)
                # in this situation we already handled the operator (unary-minus) so we can go back to the main loop
                return index

        # an equation cannot start with an operator unless it is a prefix operator
        if index == 0 and infix_exercise[0] not in PREFIX_OPERATORS:
            InfixToPostfix.adding_exception(OperatorAtFirstException, index, index + 1)

        # ~ can appear only after a binary operator '('
        if index != 0 and infix_exercise[index] == MathOperators.NEG.value and \
                infix_exercise[index - 1] not in BINARY_OPERATORS and infix_exercise[index - 1] != '(':
            InfixToPostfix.adding_exception(NegativeOperatorException, index, index + 1)

        # operator cannot appear after an operator unless the second one is a prefix operator or the first is a postfix
        if index != 0 and infix_exercise[index] not in PREFIX_OPERATORS and infix_exercise[index - 1] in OPERATORS \
                and infix_exercise[index - 1] not in POSTFIX_OPERATORS:
            InfixToPostfix.adding_exception(OperatorAfterOperatorException, index - 1, index + 1)

        # after a postfix operator we have to get an operator or ')'
        if index + 1 != len(infix_exercise) and infix_exercise[index] in POSTFIX_OPERATORS and \
                infix_exercise[index + 1] not in OPERATORS and infix_exercise[index + 1] != ')':
            InfixToPostfix.adding_exception(PostfixOperatorException, index, index + 1)

        while len(operators) != 0 and len(postfix_exercise) != 0 and \
                InfixToPostfix._stronger_operator(operators[-1], infix_exercise[index]):
            postfix_exercise.append(operators.pop())
        operators.append(infix_exercise[index])
        index += 1
        return index

    @staticmethod
    def _stronger_operator(operator1: chr, operator2: chr) -> bool:
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
        if operator1 == MathOperators.UNARY_MINUS.value:
            return True if OPERATORS_PRIORITY_DICT[operator1] > OPERATORS_PRIORITY_DICT[operator2] else False

        return True if OPERATORS_PRIORITY_DICT[operator1] >= OPERATORS_PRIORITY_DICT[operator2] else False

    @staticmethod
    def _strong_unary_minus(infix_exercise: str, index: int, operators: list) -> int:
        """
       This func gets an infix expression and an index. This index is the start of a number which starts with unary
       minus, we have to count the minuses and check if the number is positive or negative
       according to the minuses. The function returns the first index after the number ends.
       :param infix_exercise:   infix expression
       :param index: the index of the first unary minus
       :param operators: the left operators in the operators list of the algorithm
       :return: the updated index
       """
        counter = 0
        while index != len(infix_exercise) and infix_exercise[index] == MathOperators.SUB.value:
            counter += 1
            index += 1

        # Unary minus can appear only before number
        if index == len(infix_exercise) or infix_exercise[index] in OPERATORS:
            InfixToPostfix.adding_exception(UnaryMinusPlaceException, index - 1, index)

        else:
            # negative number
            if counter % 2 == 1:
                operators.append(MathOperators.NEG.value)

        return index

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
