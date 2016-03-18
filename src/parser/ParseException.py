from .get_curline import * 

class ParseException(Exception):
    """description of class"""
    def __init__(self, reason):
        self.reason = reason
        self.line = get_curline()

