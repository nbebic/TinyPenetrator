from .ExprNode import * 
from .ASTNode import * 

class LetNode(ASTNode):
    """represents a LET <var> = <expr> statement"""
    def __init__(self, var: str, expr: ExprNode):
        self.var = var
        self.expr = expr

