# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:14:29 2019

@author: 612383249
"""

import unittest
from ch4_harriet import word_count
import sys

# TASK 4 - WORD COUNT FUNCTION
#--------------------------------------------------------------------------------------

class WordCountTest(unittest.TestCase):
    
    def test_result(self):
        self.assertDictEqual({'hello': 2, 'friend': 1}, word_count("hello friend hello"))
        
    def test_input(self):
        with self.assertRaises(AttributeError):
            word_count(100)
        
if __name__ == "__main__":
    unittest.main()
  