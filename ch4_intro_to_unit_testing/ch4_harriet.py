# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:07:11 2019

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 4 - INTRODUCTION TO UNIT TESTING
#----------------------------------------------------------------------------------------------------------------------

#unit testing involves testing and validating the inputs and outputs of individual modules
#requires code to be 
#not interested in what is inside the function, just inputs and outputs
#as long as inputs/outputs stay the same, changes to the code of one function won't impact the rest of the workflow
#major advantage is that it also enables data validation - making sure that we get the expected results in different scenarios
#helps with debugging
#very useful when working in team, during development process

#the unittest library comes with some built in tools for testing
# import unittest
# this has assertion rules - e.g.:
# assertEqual(a, b) -- checks that a and b are equal
# assertNotEqual(a, b) -- checks that a and b are not equal
# assertIn(a, b) -- chceks that a is in item b
# assertFalse(a) -- checks that the value of a is false
# assertTrue(a) -- chceks that the value of a is True
# assertIsInstance(a, TYPE) -- checks that a is of type 'TYPE'
# assertRaises(ERROR, a, args) -- checks that when a is called with args that it raises 'ERROR'

# each test should test a single, specific property of the code and be named to clearly show this
#

import sys

# TASK 1 - PRIME NUMBERS
#--------------------------------------------------------------------------------------

#this script checks if a given input is a prime number
#then import this function in a test file to write tests for it
#need to check the first function first, and the other one uses it

#def is_prime(number):
#    for element in range(number):
#        if number % element == 0:
#            return False
#    return True
#
#def print_next_prime(number):
#    index = number
#    while True:
#        index += 1
#        if is_prime(index):
#            print(index)


# TASK 2 - REVISED PRIME NUMBERS
#--------------------------------------------------------------------------------------

#the test wasn't working on the previous function, because the range was dividing by 0, which raises an error in python


#def is_prime(number):
#    if number in (0, 1):
#        return False
#    
#    for element in range(2, number):
#        if number % element == 0:
#            return False
#    return True

#revise function again
def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def print_next_prime_number(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)


# TASK 3 - AN ALTERNATIVE METHOD OF TESTING PRIME FUNCTION
#--------------------------------------------------------------------------------------
#see test file


# TASK 4 - WORD COUNT FUNCTION
#--------------------------------------------------------------------------------------
#write a function that takes a single string argument and returns a dictionary
#the keys of the dictionary are the words in the body of text
#the values are the number of times that word appears

def word_count(x):
    words = x.split()
    count = {}  
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1        
    print(count)
    return count
            
#word_count('the quick brown fox jumps over the lazy dog')
        
    





