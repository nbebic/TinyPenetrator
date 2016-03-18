
from .ASTNode import * 

class ReturnNode(ASTNode):
    """description of class"""
    def codegen(self):
        return "\tRET"


