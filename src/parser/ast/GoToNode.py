
from .ExprNode import *
from .ASTNode import *
from .NumNode import *
class GoToNode(ASTNode):
    """description of class"""
    def __init__(self, dest):
        self.dest = dest

    def codegen(self):
        if isinstance(self.dest, NumNode):
            return "\tJP line%d" % self.dest.number
        raise ValueError

