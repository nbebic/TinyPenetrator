
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

        left.codegen()
        right.codegen()
        asm_output(prolog)
        if operator == '+':
            asm_output(add)
        elif operator == '-':
            asm_output(sub)
        elif operator == '*':
            asm_output(mul)
        elif operator == '/':
            asm_output(div)
        asm_output(epilog)
