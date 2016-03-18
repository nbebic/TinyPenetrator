
from .ASTNode import ASTNode
class PrintNode(ASTNode):
    """
    represents a PRINT statement

    vars: list of variables to be output
    """
    def __init__(self, expr):
        self.expr = expr

    def codegen(self):
        return "\t ; PRINT"

