
from .ASTNode import ASTNode

class ExprNode(ASTNode):
    right = None
    left = None 

    operator = None
    def codegen(self):
        prolog = """
        \tPOP HL
        \tPOP DE"""

        epilog = """
        \tPUSH HL
        """

        add = """
        \tADD HL, DE
        """

        sub = """
        \tLD F, 0
        \tSBC HL, DE
        """
        
        mul = """
        """

        div = """
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
