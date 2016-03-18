from .ASTNode import *

class LineNode(ASTNode):
    """represents a (possibly labeled) program line"""
    def __init__(self, stmt, line = -1):
        self.stmt = stmt
        self.line = line

