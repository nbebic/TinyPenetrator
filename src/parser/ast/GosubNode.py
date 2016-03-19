from .ExprNode import *
from .ASTNode import *
class GosubNode(ASTNode):
    """description of class"""
    def __init__(self, dest):
        self.dest = dest

    def codegen(self):
        return "call line%d" % self.dest


