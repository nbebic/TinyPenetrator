from .ExprNode import * 
from .ASTNode import *
from .VarNode import *

class LetNode(ASTNode):
    """represents a LET <var> = <expr> statement"""
    def __init__(self, var: str, expr: ExprNode):
        self.var = VarNode(var)
        self.expr = expr
    def codegen(self):
        s = self.expr.codegen()
        thing = """
        \tPOP HL
        \tLD (vars+%d), HL
        """
        s += thing % self.var.address
        return s

