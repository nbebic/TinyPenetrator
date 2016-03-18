
import unittest 

from ..parser.ast import NumNode

class TestNumNode(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_basic(self):
        code = NumNode(5).codegen()
        self.assertEqual(len(code.split("\n")), 4)
        self.assertTrue("HL,5" in code)
