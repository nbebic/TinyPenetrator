from .ASTNode import *
class StrNode(ASTNode):
    """
    represents a string literal
    
    s: literal sting, without quotes
    """
    def __init__(self, s):
        self.s = s

