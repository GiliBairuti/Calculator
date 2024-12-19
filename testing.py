import pytest

import exceptions
from calculation import Calculation


# Checking how the calculator handles syntax errors
def test_syntax_1():
    """
    Operator after operator
    """
    result = Calculation.calculation_answer("1-+5")
    assert exceptions.OperatorAfterOperatorException in result


def test_syntax_2():
    """
    Operator at the start of the equation
    """
    result = Calculation.calculation_answer("*7+2")
    assert exceptions.OperatorAtFirstException in result


def test_syntax_3():
    """
    Postfix operator in a prefix position and prefix operator in a postfix position
    """
    result = Calculation.calculation_answer("8+#6-4~+3")
    assert exceptions.PostfixOperatorException in result and exceptions.NegativeOperatorException in result


def test_syntax_4():
    """
    Wrong float number - more than 1 decimal point
    """
    result = Calculation.calculation_answer("5.7.4")
    assert exceptions.ImpossibleNumberException in result


def test_syntax_5():
    """
    Opening bracket without a closing bracket
    """
    result = Calculation.calculation_answer("4-(7+9)*(5")
    assert exceptions.BracketsWithoutEndOrStartException in result


# Checking how the calculator handles Gibberish
def test_gibberish():
    """
    Nonsense input
    """
    result = Calculation.calculation_answer("ddj3e309;'d3d390,_3=d_3,d93")
    assert exceptions.UnknownCharException in result


# Checking how the calculator handles empty inputs
def test_empty():
    """
    Empty input
    """
    with pytest.raises(exceptions.EmptyEquationException):
        Calculation.calculation_answer("")


# Checking how the calculator handles white space inputs
def test_white_space():
    """
    White space  input (" " and "\t")
    """
    with pytest.raises(exceptions.EmptyEquationException):
        Calculation.calculation_answer("            ")


# Now we want to check valid equations
def test_simple_1():
    assert 1 == Calculation.calculation_answer(" 4 % 3  ")


def test_simple_2():
    assert 18.6 == Calculation.calculation_answer("3+15.6")


def test_simple_3():
    assert 8.9 == Calculation.calculation_answer("12.5-3.6")


def test_simple_4():
    assert 48 == Calculation.calculation_answer("12 *4")


def test_simple_5():
    assert 0.9 == Calculation.calculation_answer("9/10")


def test_simple_6():
    assert 144 == Calculation.calculation_answer("12^2")


def test_simple_7():
    assert -9 == Calculation.calculation_answer("-6@12")


def test_simple_8():
    assert 9 == Calculation.calculation_answer("9$-34")


def test_simple_9():
    assert -6 == Calculation.calculation_answer("-6&11")


def test_simple_10():
    assert 8 == Calculation.calculation_answer("~-8")


def test_simple_11():
    assert 720 == Calculation.calculation_answer("6!")


def test_simple_12():
    assert 11 == Calculation.calculation_answer("--11")


def test_simple_13():
    assert 29 == Calculation.calculation_answer("457.85#")


def test_simple_14():
    assert 0 == Calculation.calculation_answer("7---61#")


def test_simple_15():
    assert 117649 == Calculation.calculation_answer("0+7^3!")
