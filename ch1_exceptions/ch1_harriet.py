# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:38:31 2019

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 1 - EXCEPTIONS
#----------------------------------------------------------------------------------------------------------------------
# python has in-built error codes, and you can also write your own exceptions
# built-in error codes include ValueError, TypeError, SyntaxError
# Exception is a superclass, containing the other classes of errors
# you can create your own subclasses for specific errors
# it is useful to refer to these built-in exceptions when creating your own
# these are used to print specific error messages if something doesn't execute properly
# different blocks of code are involved in this: try, except, else and finally
# 

# TASK 1 - ERROR MESSAGES
#--------------------------------------------------------------------------------------

# example 1 - missing file extension

f = open('testfile')

## this will give a generic python error message
#
## alternatively, you can use try and except blocks 
## if the try block cannot be executed, the except block will be executed
#
try: 
    f = open('testfile')
except Exception:
    print('Error!')
    
## you can also make these statements more specific

try: 
    open('testfile')
except Exception:
    print('Sorry, this file does not exist or the file name was not as expected.')


# TASK 2 - MULTIPLE ERRORS
#--------------------------------------------------------------------------------------
  
## example 2 - dealing with multiple errors
## want to ensure that the exception is linked to a specific error
## instead of using the keyword Exception in the except block, refer to a specific error message so you know what part of the code didn't execute
#    
#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name was not as expected.')
#
#
## add another except to catch an error in the s1 part of the code
#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name was not as expected.')
#except Exception:
#    print('Sorry. Something went wrong after the open function.')
#    

# TASK 3 - USING A VARIABLE
#--------------------------------------------------------------------------------------

# e is a variable containing the error
# this prints the standard error message
try:
    f = open('testfile.txt')
    s1 = not_exists
except Exception as e:
    print(e)
 
    
# TASK 4 - ELSE BLOCK
#--------------------------------------------------------------------------------------
    
# use an else block too, which will only be executed if the exception wasn't triggered 

try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()


# TASK 5 - FINALLY BLOCK
#--------------------------------------------------------------------------------------
    
# a finally block is executed regardless of what happens inside the try/except blocks
# it is useful for ensuring that everything is closed after the code has run (i.e. file, database)
 
# with error in try statement
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally statement.)

# without error in try statement 
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally statement.)


# TASK 6 - MANUALLY RAISE AN EXCEPTION
#--------------------------------------------------------------------------------------
   
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print('File names are the same.')







