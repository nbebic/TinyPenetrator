import re
from .ParseException import * 
from .ast import *
from .expression import parse_expr, is_number
from .get_curline import * 

def parse_varlist(t):
    retval = []
    for i in range(len(t)):
        if i % 2 == 1:
            if t[i] != ',':
                raise ParseException("Invalid variable list")
        else:
            if len(t[i]) > 1 or (not t[i][0] in 'QWERTYUIOPASDFGHJKLZXCVBNM'):
                raise ParseException("Invalid variable name '" + t[i] + "'")
            retval.append(t[i])
    return retval

def parse_exprlist(p):
    t = p + [',']
    retval = []
    last = -1
    for i in range(len(t)):
        if t[i] == ',':
            if last == i - 2 and t[i-1][0] == '"':
                retval.append(StrNode(t[i-1][1:-1]))
            else:
                retval.append(parse_expr(t[last+1:i]))
            last = i

    return retval

def linq_indexOfFirst(l, f):
    for i in range(len(l)):
        if f(l[i]): return i

def statement(input):
    """
    Parses given statement

    input: list of tokens to parse
    """
    op = input[0]
    if op == 'RETURN':
        return ReturnNode()
    if op == 'CLEAR':
        return ClearNode()
    if op == 'LIST':
        return ListNode()
    if op == 'RUN':
        return RunNode()
    if op == 'END':
        return EndNode()
    if op == 'LET':
        if input[2] != '=':
            raise ParseException("Invalid LET instruction")
        var = input[1]
        return LetNode(var, parse_expr(input[3:]))
    if op == 'GOSUB':
        return GosubNode(parse_expr(input[1:]))
    if op == 'INPUT':
        return InputNode(parse_varlist(input[1:]))
    if op == "GOTO":
        return GoToNode(parse_expr(input[1:]))
    if op == 'IF':
        relop = linq_indexOfFirst(input, lambda x: '<' in x or '>' in x or '=' in x)
        then = linq_indexOfFirst(input, lambda x: x == 'THEN')
        if relop == None or then == None:
            raise ParseException("Invalid IF instruction")
        one = parse_expr(input[1:relop])
        two = parse_expr(input[relop+1:then])
        rest = statement(input[then+1:])
        return IfNode(one, input[relop], two, rest)
    if op == "PRINT":
        return PrintNode(parse_exprlist(input[1:]))
    if op == 'POKE':
        com = linq_indexOfFirst(input, lambda x: x == ',')
        if com == None:
            raise ParseException('Invalid POKE instruction')
        dest = parse_expr(input[1:com])
        oper = parse_expr(input[com+1:])
        return PokeNode(dest, oper)
    if op == 'POINT':
        com = linq_indexOfFirst(input, lambda x: x == ',')
        if com == None:
            raise ParseException('Invalid POKE instruction')
        dest = parse_expr(input[1:com])
        oper = parse_expr(input[com+1:])
        return PointNode('SET', dest, oper)
    if len(op) >= 3 and op[0:3] == "REM":
        return None


def parse_program(t):
    global curLine
    p = t + ['\n']
    last = -1
    retval = []
    for i in range(len(p)):
        if p[i] == '\n':
            curLine += 1
            if last == i-1:
                last = i
                continue
            if is_number(p[last+1]):
                retval.append(LineNode(statement(p[last+2:i]), p[last+1]))
            else:
                raise ParseException("Unlabeled line")
            last = i
    return retval
