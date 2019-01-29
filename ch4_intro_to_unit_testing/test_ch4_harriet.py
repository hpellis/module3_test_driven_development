# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:58:46 2019

@author: 612383249
"""

import unittest
from ch4_harriet import is_prime
from ch4_harriet import word_count
import sys

#TestCase is the individual unit of testing
#it checks for a specific respones to a particular set of inputs
#unittest provides a base class, TestCase, which may be used to create new test cases
#best to keep tests separate, because then you know which one failed

#goal is to test some edge cases
#in this example, test cases would be the numbers 0, 1, negative numbers and very large numbers, float numbers


# TASK 1 & 2 - TEST PRIME NUMBERS
#--------------------------------------------------------------------------------------

class PrimesTest(unittest.TestCase):
    
    def test_prime(self):
        self.assertTrue(is_prime(5))
        
    def test_non_prime(self):
        self.assertFalse(is_prime(4))
        
    def test_non_prime_alt(self):
        self.assertTrue(is_prime(4), msg = "Four is not a prime number.")
        
    def test_zero(self):
        self.assertFalse(is_prime(0))
        

#wrapper function
#this calls the main function, which is by default the first function in a file        
if __name__ == "__main__":
    unittest.main()

#alternative syntax below    
#unittest.TestCase.assertTrue(is_prime(5))
#unittest.TestCase.assertFalse(is_prime(4))
#unittest.TestCase.assertFalse(is_prime(0))        

     
## TASK 3 - AN ALTERNATIVE METHOD OF TESTING PRIME FUNCTION
##--------------------------------------------------------------------------------------
#run in separate file to use
    
    
#class AltPrimesTest(unittest.TestCase):
#
##this checks that the function returns the value specified in the second arg    
#    def test_value(self):
#        self.assertEqual(is_prime(3), True)
#        
##these check that the function returns True and False as expected
#    def test_true(self):
#        self.assertTrue(is_prime(5))
#        self.assertFalse(is_prime(4))
#        
##this checks that providing a string input produces an error
#    def test_string(self):
#        with self.assertRaises(TypeError):
#            is_prime('1')
            

# TASK 4 - WORD COUNT FUNCTION
#--------------------------------------------------------------------------------------
#run in a separate file ot use
    
#class WordCountTest(unittest.TestCase):
#    
#    def test_result(self):
#        self.assertDictEqual({'hello': 2, 'friend': 1}, word_count("hello friend hello"))
#        
#    def test_input(self):
#        with self.assertRaises(AttributeError):
#            word_count(100)
#        
#if __name__ == "__main__":
#    unittest.main()
        



    