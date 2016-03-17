

import unittest 

from ..parser import *

class TestExpression(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_addition(self):
        e = parse_expr(["1", "+", "2"])
        self.assertEqual(e.left.number, 1)
        self.assertEqual(e.right.number, 2)
        self.assertEqual(e.operator, "+")
    
    def test_addition_many(self):
        e = parse_expr(["1", "+", "2", "+", "3"])
        self.assertEqual(e.left.left.number, 1)
        self.assertEqual(e.left.right.number, 2)
        self.assertEqual(e.operator, "+")
        self.assertEqual(e.right.number, 3)
    
    def test_multiplication_many(self):
        e = parse_expr(["1", "*", "2", "*", "3"])
        self.assertEqual(e.left.left.number, 1)
        self.assertEqual(e.left.right.number, 2)
        self.assertEqual(e.operator, "*")
        self.assertEqual(e.right.number, 3)
    
    def test_multiplication_addition(self):
        e = parse_expr(["1", "+", "2", "*", "3"])
        self.assertEqual(e.left.number, 1)
        self.assertEqual(e.right.left.number, 2)
        self.assertEqual(e.operator, "+")
        self.assertEqual(e.right.operator, "*")
        self.assertEqual(e.right.right.number, 3)

    def test_subtraction(self):
        e = parse_expr(["1", "-", "2"])
        self.assertEqual(e.left.number, 1)
        self.assertEqual(e.right.number, 2)
        self.assertEqual(e.operator, "-")
    
    def test_multiplication(self):
        e = parse_expr(["1", "*", "2"])
        self.assertEqual(e.left.number, 1)
        self.assertEqual(e.right.number, 2)
        self.assertEqual(e.operator, "*")

    def test_addition_brackets(self):
        e = parse_expr(["1", "+", "(", "2", "+", "3", ")"])
        self.assertEqual(e.left.number, 1)
        self.assertEqual(e.right.left.number, 2)
        self.assertEqual(e.right.right.number, 3)
        self.assertEqual(e.right.operator, "+")
        self.assertEqual(e.operator, "+")

    def test_negative_expression(self):
        e = parse_expr(["-", "1"])
        self.assertEqual(e.right.number, 1)
