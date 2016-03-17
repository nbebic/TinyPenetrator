
from .ASTNode import * 

class NumNode(ASTNode):
    
    def __init__(self, number):
        self.number = number
