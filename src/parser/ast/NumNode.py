
from .ASTNode import * 

class NumNode(ASTNode):
    
    def __init__(self, number):
       self.number = number

    def codegen(self):
        return """
\tLD HL,%d
\tPUSH HL
    """ % self.number
