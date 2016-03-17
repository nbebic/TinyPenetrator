import re
from .ParseException import * 
from .ast import *
from .expression import parse_expr

def parse_varlist(t):
    retval = []
    for i in range(len(t)):
        if i % 2 == 0:
            if t[i] != ',':
                raise ParseException()
        else:
            if len(t[i]) > 1 and (not t[i][0] in 'QWERTYUIOPASDFGHJKLZXCVBNM'):
                raise ParseException()
            retval.append(t[i])

def parse_exprlist(t):
    retval = []
    last = -1
    for i in range(len(t)):
        if t[i] == ',':
            if last == i - 2 and t[i-1][0] == '"':
                retval.append(StrNode(t[i-1][1:-2]))
            else:
                retval.append(parse_expr(t[last+1:i-1]))
            last = i

def statement(input):
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
    if (op == 'GOSUB'):
        return GosubNode(parse_expr(input[1:-1]))
    if (op == 'INPUT'):
        return InputNode(parse_varlist(input[1:-1]))



if (__name__ == "__main__"):
    pass
