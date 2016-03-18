import unittest
from ..lexer import *

class TestLexer(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic(self):
        e = lex('2 3+7 "ma + ()gija" (2+3*4) LET S = X')
        self.assertListEqual(['2', '3', '+', '7', '"ma + ()gija"', '(', '2', '+', '3', '*', '4', ')', 'LET', 'S', '=', 'X'],e)

        e = lex("PRINT \",aaa\"")
        self.assertListEqual(e, ["PRINT", "\"aaa\""])
