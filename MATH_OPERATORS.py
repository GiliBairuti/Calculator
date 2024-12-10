from enum import Enum


class MathOperators(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    POW = '^'
    AVG = '@'
    MAX = '$'
    MIN = '&'
    MODULO = '%'
    NEG = '~'
    FACTORIAL = '!'
    UNARY_MINUS = 'U'
    UNARY_MINUS_AFTER_NEG = 'A'   # highest priority
    UNARY_MINUS_REGULAR = 'B'
