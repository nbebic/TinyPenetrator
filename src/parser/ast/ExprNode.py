
from .ASTNode import ASTNode

class ExprNode(ASTNode):
    right = None
    left = None 

    operator = None
    def codegen(self):
        prolog = ""
        if self.operator in "+-":
            prolog = """
\tPOP DE
\tPOP HL
"""
        else:
            if self.operator == "*":
                prolog = """
\tPOP DE
\tPOP BC
"""
            else:
                prolog = """
\tPOP BC
\tPOP HL
\tLD B,0
"""

        epilog = """
\tPUSH HL
"""

        add = """
\tADD HL, DE
"""

        sub = """
\tAND A
\tSBC HL, DE
"""
        
        mul = """
call mult_de_bc
"""

        div = """
call div_hl_c
"""
        s = ""
        s += self.left.codegen()
        s += self.right.codegen()
        s += prolog
        if self.operator == '+':
            s += add
        elif self.operator == '-':
            s += sub
        elif self.operator == '*':
            s += mul
        elif self.operator == '/':
            s += div
        s += epilog
        return s
