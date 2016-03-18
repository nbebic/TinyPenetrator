
from .ASTNode import * 

class VarNode(ASTNode):
    
    def __init__(self, var):
        self.var = var
        self.address = (ord(self.var) - 65)*2

    def codegen(self):
        return """
        LD BC,(vars+%d)
        PUSH BC
        """ % self.address
