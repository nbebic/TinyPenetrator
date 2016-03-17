import unittest 
from ..parser import *

class TestListParsers(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_varlist(self):
        e = parse_varlist(['X',',','Y'])
        self.assertListEqual(['X','Y'], e)

    def test_varlist_singlevar(self):
        e = parse_varlist(['X'])
        self.assertListEqual(['X'], e)

    def test_varlist_invalid_list(self):
        with self.assertRaises(ParseException):
            parse_varlist(['X','Y'])

    def test_varlist_invalid_id(self):
        with self.assertRaises(ParseException):
            parse_varlist(['XYX', ',' ,'Y'])

        
