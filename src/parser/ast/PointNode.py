from .ASTNode import *

class PointNode(ASTNode):  
    def __init__(self, mode, x, y):
        self.mode = mode
        self.x = x
        self.y = y
    
    def codegen(self):
        s = self.x.codegen()
        s += self.y.codegen()
        s += """
\tPOP DE
\tPOP BC
\tLD B, E
\tCALL plot_xy
"""
        return s