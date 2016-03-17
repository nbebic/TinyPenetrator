class IfNode(object):
    """represents IF ..."""
    def __init__(self, lhs, relop, rhs, stmt):
        self.lhs = lhs
        self.rhs = rhs
        self.relop = relop
        self.stmt = stmt


