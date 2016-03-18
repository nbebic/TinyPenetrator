

import unittest 

from ..parser.ast import VarNode

class TestVarNode(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_basic(self):
        code = VarNode("B").codegen()
        self.assertEqual(len(code.split("\n")), 4)
        self.assertTrue("vars+2" in code)
