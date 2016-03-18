import unittest 

from ..parser.ast import *
from ..parser import *

class TestCodegen(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_let(self):
        code = LetNode("X", parse_expr(["3", "+", "Y"]))
        st = code.codegen()
        self.assertTrue('48' in st)
    
    def test_var(self):
        code = VarNode("B").codegen()
        self.assertEqual(len(code.split("\n")), 4)
        self.assertTrue("vars+2" in code)
    
    def test_num(self):
        code = NumNode(5).codegen()
        self.assertEqual(len(code.split("\n")), 4)
        self.assertTrue("HL,5" in code)
