# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:45:43 2019

@author: 612383249
"""

import unittest
from ch4_harriet import is_prime
import sys

      
# TASK 3 - AN ALTERNATIVE METHOD OF TESTING PRIME FUNCTION
#--------------------------------------------------------------------------------------

class AltPrimesTest(unittest.TestCase):

#this checks that the function returns the value specified in the second arg    
    def test_value(self):
        self.assertEqual(is_prime(3), True)
        
#these check that the function returns True and False as expected
    def test_true(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        
#this checks that providing a string input produces an error
    def test_string(self):
        with self.assertRaises(TypeError):
            is_prime('1')
            
            
if __name__ == "__main__":
    unittest.main()