
from .ASTNode import * 

class NumNode(ASTNode):
    
    def __init__(self, number):
       self.number = number

    def codegen(self):
        return """
        LD HL,%d
        PUSH HL
        """ % self.number
