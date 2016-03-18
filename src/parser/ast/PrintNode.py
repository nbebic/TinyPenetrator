
from .ASTNode import ASTNode

from .ExprNode import ExprNode
from .StrNode import StrNode
from ..ParseException import *

class PrintNode(ASTNode):
    """
    represents a PRINT statement

    vars: list of variables to be output
    """
    def __init__(self, expr):
        self.expr = expr

    def codegen(self):
        s = ""
        for e in self.expr:
            if isinstance(e, ExprNode):
                s += e.codegen()
                s += "\tPOP BC\n"
                s += "\tCALL print_num\n"
            elif isinstance(e, StrNode):
                s += "\tLD HL,str%d\n" % e.index
                s += "\tCALL print_str\n"
            else:
                raise ParseException("Use print with expression or string")
        return s
