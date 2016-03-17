
import unittest 

from ..parser import *
from ..parser.ast import * 

class TestStatement(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_let(self):
        e = statement(["LET", "X", "=", "5"])
        self.assertIsInstance(e, LetNode)

    def test_goto(self):
        e = statement(["GOTO", "5", "+", "2"])
        self.assertIsInstance(e, GoToNode)

    def test_print(self):
        e = statement(["PRINT", "5", "+", "2"])
        self.assertIsInstance(e, PrintNode)
