from .ASTNode import *

class PokeNode(ASTNode):

    def __init__(self, dest, oper):
        self.dest = dest
        self.oper = oper

    def codegen(self):
        s = self.dest.codegen()
        s += self.oper.codegen()
        s += """
\tPOP DE
\tPOP HL
\tLD (HL), E
        """
        return s
