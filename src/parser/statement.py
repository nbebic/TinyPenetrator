import re
import parser.ParseException
from parser.ast import *
from parser.expression import parse_expr

def statement(input:list):
    """
    Parses given statement

    input: list of tokens to parse
    """
    op = input[0]
    if (op == 'RETURN'):
        return ReturnNode()
    if (op == 'CLEAR'):
        return ClearNode()
    if (op == 'LIST'):
        return ListNode()
    if (op == 'RUN'):
        return RunNode()
    if (op == 'END'):
        return EndNode()
    if (op == 'LET'):
        if input[2] != '=':
            raise ParseException()
        var = input[1]
        return LetNode(var, parse_expr(input[3:-1]))



if (__name__ == "__main__"):
    pass