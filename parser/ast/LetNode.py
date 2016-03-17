from .ASTNode import *

class LetNode(ASTNode):
    """description of class"""
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

