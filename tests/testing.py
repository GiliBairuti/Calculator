import pytest

from exceptions import exceptions
from calc.calculator import Calculation


# Checking how the calculator handles syntax errors
def test_syntax_1():
    """
    Operator after operator
    """
    result = Calculation.calculation_to_result("1-+5")
    assert exceptions.OperatorAfterOperatorException in result


def test_syntax_2():
    """
    Operator at the start of the equation
    """
    result = Calculation.calculation_to_result("*7+2")
    assert exceptions.OperatorAtFirstException in result


def test_syntax_3():
    """
    Postfix operator in a prefix position and prefix operator in a postfix position
    """
    result = Calculation.calculation_to_result("8+#6-4~+3")
    assert exceptions.PostfixOperatorException in result and exceptions.NegativeOperatorException in result


def test_syntax_4():
    """
    Wrong float number - more than 1 decimal point
    """
    result = Calculation.calculation_to_result("5.7.4")
    assert exceptions.ImpossibleNumberException in result


def test_syntax_5():
    """
    Opening bracket without a closing bracket
    """
    result = Calculation.calculation_to_result("4-(7+9)*(5")
    assert exceptions.BracketsWithoutEndOrStartException in result


# Checking how the calculator handles Gibberish
def test_gibberish():
    """
    Nonsense input
    """
    result = Calculation.calculation_to_result("ddj3e309;'d3d390,_3=d_3,d93")
    assert exceptions.UnknownCharException in result


# Checking how the calculator handles empty inputs
def test_empty():
    """
    Empty input
    """
    with pytest.raises(exceptions.EmptyEquationException):
        Calculation.calculation_to_result("")


# Checking how the calculator handles white space inputs
def test_white_space():
    """
    White space  input (" " and "\t")
    """
    with pytest.raises(exceptions.EmptyEquationException):
        Calculation.calculation_to_result("            ")


# Now we want to check valid equations
def test_simple_1():
    assert 1 == Calculation.calculation_to_result(" 4 % 3  ")


def test_simple_2():
    assert 18.6 == Calculation.calculation_to_result("3+15.6")


def test_simple_3():
    assert 8.9 == Calculation.calculation_to_result("12.5-3.6")


def test_simple_4():
    assert 48 == Calculation.calculation_to_result("12 *4")


def test_simple_5():
    assert 0.9 == Calculation.calculation_to_result("9/10")


def test_simple_6():
    assert 144 == Calculation.calculation_to_result("12^2")


def test_simple_7():
    assert -9 == Calculation.calculation_to_result("-6@12")


def test_simple_8():
    assert 9 == Calculation.calculation_to_result("9$-34")


def test_simple_9():
    assert -6 == Calculation.calculation_to_result("-6&11")


def test_simple_10():
    assert 8 == Calculation.calculation_to_result("~-8")


def test_simple_11():
    assert 720 == Calculation.calculation_to_result("6!")


def test_simple_12():
    assert 11 == Calculation.calculation_to_result("--11")


def test_simple_13():
    assert 29 == Calculation.calculation_to_result("457.85#")


def test_simple_14():
    assert 0 == Calculation.calculation_to_result("7---61#")


def test_simple_15():
    assert 117649 == Calculation.calculation_to_result("0+7^3!")


# Now complicated equations
def test_complicated_1():
    assert 28.049999999999997 == Calculation.calculation_to_result("~-6+7&4-1^43#+28.55-(12@7)")


def test_complicated_2():
    assert 253 == Calculation.calculation_to_result("12/3!+23  4#$10  *5^2-23+~-4!")


def test_complicated_3():
    assert 11 == Calculation.calculation_to_result("(5+7-12@8*5+6!)%(~4*13+100)+100#")


def test_complicated_4():
    assert 176 == Calculation.calculation_to_result("-4+5%2@12+65^0--78+10&34-(42#$11)+100      -3")


def test_complicated_5():
    assert 1000033390 == Calculation.calculation_to_result("1000034332+100-(3^ 10)&60000%675  -(6)!+2")


def test_complicated_6():
    assert 25 == Calculation.calculation_to_result("4$5^2+7-------32   # +(-5)@1!")


def test_complicated_7():
    assert 53 == Calculation.calculation_to_result("(((8-((5+33)-12)&6)^2)-7)+12@100")


def test_complicated_8():
    assert 168.35000000000002 == Calculation.calculation_to_result("687*0.4+~102.45-(734.2#%12)")


def test_complicated_9():
    assert 33 == Calculation.calculation_to_result("(6-3)!+45/6%5+0  ^23 - 18")


def test_complicated_10():
    assert -7721 == Calculation.calculation_to_result("~-4+--45-5*-3-4-5-~-6^23#")


def test_complicated_11():
    assert 43 == Calculation.calculation_to_result("-(5*3+2)$14+7&18#*2^3+(12)/3")


def test_complicated_12():
    assert -89 == Calculation.calculation_to_result("~(8^2) + 12# - 5!&10*3 -- 2")


def test_complicated_13():
    assert -35 == Calculation.calculation_to_result("103.6#*~10+104    $23 -6*3! -(89&4$3)+1")


def test_complicated_14():
    assert 41 == Calculation.calculation_to_result("34444444356565.12###+100-~--(-4$30)*2")


def test_complicated_15():
    assert -10.18 == Calculation.calculation_to_result("7.6+10.22%4-6^3&1-12 +-6/3")


def test_complicated_16():
    assert 10 == Calculation.calculation_to_result("(12@3)$34-(132#+4!#+12)")


def test_complicated_17():
    assert -69 == Calculation.calculation_to_result("~--3*4!-5%(3+11)/31#*11+14&(2^3/2)   +   12.75")


def test_complicated_18():
    assert 37208 == Calculation.calculation_to_result("98334@-23946+~-542#-~3&4")


def test_complicated_19():
    assert 92 == Calculation.calculation_to_result("-(-12&(12#!   +54%2/4-7*2))+100")


def test_complicated_20():
    assert -3283.66 == Calculation.calculation_to_result("3333.2332#+23.1^2*-6-100$23--(7+53&3)%10@4")
