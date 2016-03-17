from .ASTNode import ASTNode
class InputNode(ASTNode):
    """
    represents a INPUT <var-list> statement

    vars: list of variables to be input
    """
    def __init__(self, vars):
        self.vars = vars



