
import unittest 

from ..parser import *
from ..parser.ast import * 
from ..lexer import *

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

    def test_all(self):
        a = """
        10 LET X = 7
        20 LET Y = 5
        30 PRINT X + Y
        """

        b = lex(a.upper())
        c = parse_program(b)
        self.assertIsInstance(c, list)
