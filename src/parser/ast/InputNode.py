from .ASTNode import ASTNode
from .VarNode import * 
class InputNode(ASTNode):
    """
    represents a INPUT <var-list> statement

    vars: list of variables to be input
    """
    def __init__(self, vars):
        self.vars = vars
    
    def codegen(self):
        for v in self.vars:
            fuck = VarNode(v)
            s = ""
            s += "\tcall input\n"
            s += "\tLD (vars+%d), BC\n" % fuck.address
        return s

