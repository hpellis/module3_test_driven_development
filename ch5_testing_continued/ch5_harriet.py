# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:05:49 2019

@author: harri
"""

#--------------------------------------------------------------------------------------------------------------
# CHAPTER 5 - EXTERNAL TESTING TOOL
#----------------------------------------------------------------------------------------

#the main difference between unittest, pytest and nose is the amount of information they return
#pytest can tell you which variables inside a function fail
#nose can do a similar thing

import unittest
from ch5_calculator_harriet import Calculator

# TASK 1 - WRITE TEST FILE
#------------------------------------------------------------------------------------------

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2,2), 4)
        self.assertEqual(self.calc.add(-2, 2), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
    def test_args_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.add, 'two', 2)
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
    
        
if __name__ == 'main':
    unittest.main()
        
        
        
        
        