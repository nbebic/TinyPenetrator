

import unittest 

from parser import *

class TestExpression(unittest.TestCase):
    
    def setUp(self):
        pass

    def addition(self):
        e = parse_expr(["1", "+", "2"])
        self.assertEqual(e.left.number, 1)
        self.assertEqual(e.right.number, 2)
        self.assertEqual(e.operator, "+")

