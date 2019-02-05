# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:06:37 2019

@author: harri
"""

#--------------------------------------------------------------------------------------------------------------
# CHAPTER 5 - EXTERNAL TESTING TOOL
#----------------------------------------------------------------------------------------


# TASK 1  - WRITE FUNCTION FILE
#------------------------------------------------------------------------------------------

class Calculator():
    def add (self, a, b):
        number_types = (int, float, complex)
        if isinstance (a, number_types) and isinstance (b, number_types):
            return a + b
        else:
            raise ValueError
