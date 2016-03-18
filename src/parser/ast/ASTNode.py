
class ASTNode(object):
    
    def codegen(self):
        pass

    def __str__(self):
        return type(self).__str__()
