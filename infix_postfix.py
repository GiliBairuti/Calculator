from MATH_OPERATORS import MathOperators

# I chose to call 'U' as unary-minus
OPERATORS_PRIORITY_DICT = {MathOperators.ADD.value: 1, MathOperators.SUB.value: 1, MathOperators.MUL.value: 2,
                           MathOperators.DIV.value: 2, MathOperators.POW.value: 3, MathOperators.AVG.value: 5,
                           MathOperators.MAX.value: 5, MathOperators.MIN.value: 5, MathOperators.MODULO.value: 4,
                           MathOperators.NEG.value: 6, MathOperators.FACTORIAL.value: 6,
                           MathOperators.UNARY_MINUS.value: 3.5}


class InfixToPostfix:
    """
    this class's purpose is to change infix expression to postfix expression
    """

    @staticmethod
    def infix_to_postfix(infix_exercise: str) -> list:
        """
        this function gets a string which is a math exercise in infix,
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
        this class gets a string of infix expression, a list of the postfix expression and an index which
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
        this class gets a string of infix expression, a list of the postfix expression, a list with operators
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

        if infix_exercise[index] == ')':
            while operators[-1] != '(':
                postfix_exercise.append(operators.pop())
            operators.pop()

        else:
            while len(operators) != 0 and InfixToPostfix._stronger_operator(operators[-1], infix_exercise[index]):
                postfix_exercise.append(operators.pop())
            operators.append(infix_exercise[index])
        index += 1

        return infix_exercise, postfix_exercise, operators, index

    @staticmethod
    def _stronger_operator(operator1: chr, operator2: chr) -> chr:
        """
        this class gets 2 chars of arithmetic signs and return True if the first one
        is primer than the second one, otherwise False
        :param operator1: operator
        :param operator2: operator
        :return: boolean variable
        """
        if operator1 == '(' or operator2 == '(':
            return False

        # because they are infix operators
        if operator1 == 'U' or operator1 == '~':
            return True if OPERATORS_PRIORITY_DICT[operator1] > OPERATORS_PRIORITY_DICT[operator2] else False

        return True if OPERATORS_PRIORITY_DICT[operator1] >= OPERATORS_PRIORITY_DICT[operator2] else False
