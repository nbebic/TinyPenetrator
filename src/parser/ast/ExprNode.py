
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
        s += left.codegen()
        s += right.codegen()
        s += prolog
        if operator == '+':
            s += add
        elif operator == '-':
            s += sub
        elif operator == '*':
            s += mul
        elif operator == '/':
            s += div
        s += epilog
        return s
