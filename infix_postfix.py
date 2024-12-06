from MATH_OPERATORS import MathOperators

# I chose to call 'U' as unary-minus
OPERATORS_PRIORITY_DICT = {MathOperators.ADD.value: 1, MathOperators.SUB.value: 1, MathOperators.MUL.value: 2,
                           MathOperators.DIV.value: 2, MathOperators.POW.value: 3, MathOperators.AVG.value: 5,
                           MathOperators.MAX.value: 5, MathOperators.MIN.value: 5, MathOperators.MODULO.value: 4,
                           MathOperators.NEG.value: 6, MathOperators.FACTORIAL.value: 6,
                           MathOperators.UNARY_MINUS.value: 10}


class InfixToPostfix:
    """
    This class's purpose is to change infix expression to postfix expression
    """

    @staticmethod
    def infix_to_postfix(infix_exercise: str) -> list:
        """
        This function gets a string which is a math exercise in infix,
        and change it into a list of the numbers and the chars of the operators in a list ordered in postfix
        :param infix_exercise: holding a string which represents a mathematical infix expression
        :return: list which includes the same math exercise but in postfix
        """
        # remove the meaningless spaces
        infix_exercise = infix_exercise.replace(' ', '')

        operators = []
        postfix_exercise = []
        index = 0

        while index != len(infix_exercise):
            # operand
            if str.isdigit(infix_exercise[index]):
                infix_exercise, postfix_exercise, index = \
                    InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index)

            # operator
            else:
                infix_exercise, postfix_exercise, operators, index = \
                    InfixToPostfix._operator_handling(infix_exercise, postfix_exercise, operators, index)

        # add the operators that are left
        while len(operators) != 0:
            postfix_exercise.append(operators.pop(len(operators) - 1))

        return postfix_exercise

    @staticmethod
    def _operand_handling(infix_exercise: str, postfix_exercise: list, index: int) -> str and list and int:
        """
        This class gets a string of infix expression, a list of the postfix expression and an index which
        point on the start of the number. The class adds the full number (can be floated) to the postfix list.
        :param infix_exercise: a string which is an infix expression
        :param postfix_exercise: a list which handled part of the postfix expression of the infix_exercise
        :param index: the start index of the operand we are going on right now
        :return: all the updated variables
        """
        start_of_number_index = index
        while index + 1 != len(infix_exercise) and (
                str.isdigit(infix_exercise[index + 1]) or infix_exercise[index + 1] == '.'):
            index += 1

        postfix_exercise.append(float(infix_exercise[start_of_number_index:index + 1]))
        index += 1
        return infix_exercise, postfix_exercise, index

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
        # checking if it is a unary-minus and replace it to my custom char if its necessary
        if infix_exercise[index] == '-' and (index == 0 or infix_exercise[index - 1] in OPERATORS_PRIORITY_DICT.keys()):
            infix_exercise = infix_exercise[:index] + 'U' + infix_exercise[index + 1:]

        # the treatment of ~ is different because it is the only one infix operator
        if infix_exercise[index] == '~':
            infix_exercise, postfix_exercise = \
                InfixToPostfix._negative_handling(infix_exercise, postfix_exercise, index)

        # the treatment of brackets is different because it always in the first priority
        if infix_exercise[index] == ')':
            while operators[-1] != '(':
                postfix_exercise.append(operators.pop())
            operators.pop()

        else:
            while len(operators) != 0 and len(postfix_exercise) != 0 and \
                    InfixToPostfix._stronger_operator(operators[-1], infix_exercise[index]):
                postfix_exercise.append(operators.pop())
            operators.append(infix_exercise[index])
        index += 1

        return infix_exercise, postfix_exercise, operators, index

    @staticmethod
    def _negative_handling(infix_exercise: str, postfix_exercise: list,index: int) -> str and list:
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
        infix_exercise, postfix_exercise, end_of_num = InfixToPostfix._operand_handling(infix_exercise, postfix_exercise, index)

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

        # because it can repeat several times one after the other
        if operator1 == 'U':
            return True if OPERATORS_PRIORITY_DICT[operator1] > OPERATORS_PRIORITY_DICT[operator2] else False

        return True if OPERATORS_PRIORITY_DICT[operator1] >= OPERATORS_PRIORITY_DICT[operator2] else False
