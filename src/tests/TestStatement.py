
import unittest 

from ..parser import *
from ..parser.ast import * 

class TestStatement(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_let(self):
        e = statement(["LET", "X", "=", "5"])
        self.assertIsInstance(e, LetNode)
