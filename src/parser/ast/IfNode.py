from .ASTNode import *


nexts = 0
class IfNode(ASTNode):
    """represents IF ..."""
    def __init__(self, lhs, relop, rhs, stmt):
        self.lhs = lhs
        self.rhs = rhs
        self.relop = relop
        self.stmt = stmt
    
    def codegen(self):
        global nexts
        s = self.lhs.codegen()
        s += self.rhs.codegen()

        s += """
        \tPOP DE
        \tPOP HL
        \tLF F, 0
        \tSBC HL, DE
        """
        nxtlbl = 'next%d' % nexts
        nexts += 1
        if self.relop == '<':
            s += '\tJP P, %s\n\tJP Z, %s\n' % (nxtlbl, nxtlbl)
        elif self.relop == '>':
            s += '\tJP M, %s\n\tJP Z, %s\n' % (nxtlbl, nxtlbl)
        elif self.relop == '=':
            s += '\tJP NZ, %s' % nxtlbl
        elif self.relop in ['<>', '><']:
            s += '\tJP Z, %s' % nxtlbl
        elif self.relop == '>=':
            s += '\tJP P, %s' % nxtlbl
        elif self.relop == '<=':
            s += '\tJP M, %s' % nxtlbl
        s += self.stmt.codegen()
        s += '\n' + nxtlbl + ':\n'
        return s
        
