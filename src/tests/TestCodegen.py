import unittest 

from ..parser.ast import *
from ..parser import *

class TestCodegen(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_basic(self):
        code = LetNode("X", parse_expr(["3", "+", "Y"]))
        st = code.codegen()
        self.assertTrue('48' in st)
        pass