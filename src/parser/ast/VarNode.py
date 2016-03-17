
from .ASTNode import * 

class VarNode(ASTNode):
    
    def __init__(self, var):
        self.var = var
