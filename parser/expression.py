
from ast import NumNode
from ast import VarNode

class ExprNode():
    
    right = None
    left = None 

    operator = None 


def is_factor(expr):
    brackets = 0 
    operators = 0
    for c in expr:
        if c == "(":
            brackets += 1
        if c == ")":
            brackets -= 1
        if c in "+-*/" and brackets == 0:
            operators += 1
    return operators == 0

def is_number(expr):
    for c in expr:
        if not c in "0123456789":
            return False 
    return True

def is_term(expr):
    operator_plusminus = 0
    operator = 0
    brackets = 0
    for c in expr:
        if c == "(":
            brackets += 1
        if c == ")":
            brackets -= 1
        if c in "+-" and brackets == 0:
            operator_plusminus += 1
        if c in "*/" and brackets == 0:
            operator += 1
    return operator > 0 and operator_plusminus == 0


def is_var(expr):
    return expr in "QWERTYUIOPASDFGHJKLZXCVBNM"


def without_brackets(expr):
    if expr[0] == "(" and expr[-1] == ")":
        return expr[1:-1]
    return expr

def parse_expr(expr, term=False):
    """
    Parses given string 

    expr: string to parse 

    Returns: ExprNode
    """
    if is_number(expr):
        return NumNode(int(expr))
    if is_var(expr):
        return VarNode(c)
    res = ExprNode()
    brackets = 0
    parse_left = False
    operand_right = ""
    operand_left = ""
    # go through given argument backwards
    for c in expr[::-1]:
        if c == "(":
            brackets += 1
        if c == ")":
            brackets -= 1
        if ((term and c in "+-*/") or (not term and c in "+-")) and brackets == 0:
            parse_left = True
            res.operator = c
        else:
            if not parse_left:
                operand_right += c
            else:
                operand_left += c

    if is_term(operand_right):
        res.right = parse_expr(without_brackets(operand_right[::-1]), True)
    else:
        res.right = parse_expr(without_brackets(operand_right[::-1]), False)
    if is_term(operand_left):
        res.left = parse_expr(without_brackets(operand_left[::-1]), True)
    else:
        res.left = parse_expr(without_brackets(operand_left[::-1]), False)
    
    return res

