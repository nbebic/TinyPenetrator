
from .ASTNode import ASTNode

from .ExprNode import ExprNode
from .StrNode import StrNode

class PrintNode(ASTNode):
    """
    represents a PRINT statement

    vars: list of variables to be output
    """
    def __init__(self, expr):
        self.expr = expr

    def codegen(self):
        s = ""
        if isinstance(self.expr, ExprNode):
            s += self.expr.codegen()
            s += "\tPOP BC\n"
            s += "\tCALL print_num\n"
        elif isinstance(self.expr, StrNode):
            s += "\tLD HL,str%d\n" % self.expr.index
            s += "\tCALL print_str\n"
        else:
            raise ParseException("Use print with expression or string")
        return s
