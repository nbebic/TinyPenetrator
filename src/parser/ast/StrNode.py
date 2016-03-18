from .ASTNode import *

str_index = 0

CONSTANTS_CODE = ""

class StrNode(ASTNode):
    global str_index 
    global CONSTANTS_CODE
    """
    represents a string literal
    
    s: literal sting, without quotes
    """
    def __init__(self, s):
        global str_index 
        global CONSTANTS_CODE
        self.s = s
        self.index = str_index
        str_index += 1
        CONSTANTS_CODE += "\nstr%d:" % self.index
        CONSTANTS_CODE += "\n\tDB \"%s\",0" % self.s

    def codegen(self):
        return ""
        
