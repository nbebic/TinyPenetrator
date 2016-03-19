
from .ASTNode import *

class PeekNode(ASTNode):

    def __init__(self, dest, expr):
        self.dest = dest
        self.expr = expr

    def codegen(self):
        s = ""
        s += self.expr.codegen()
        s += """
\tPOP HL
\tLD A,(HL)
\tLD (vars+%d), A
        """ % self.dest.address
        return s
