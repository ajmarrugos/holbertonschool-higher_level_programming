#!/usr/bin/python3
"""
Unittest for: max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' unittest class for testing max_integer function '''
    def test_module_documentation(self):
        ''' test for module documentation'''
        test = __import__('6-max_integer').__doc__
        self.assertTrue(len(test) > 1)

    def test_module_function(self):
        ''' test for function documentation '''
        test = max_integer.__doc__
        self.assertTrue(len(test) > 1)

    def test_positive_int_start(self):
        ''' test result of positive int in list at start '''
        test = [60, 2, 23, 54, 15]
        self.assertEqual(max_integer(test), 60)

    def test_positive_int_middle(self):
        ''' test result of positive int in list in mid '''
        test = [3, 2, 6, 4, 5]
        self.assertEqual(max_integer(test), 6)
