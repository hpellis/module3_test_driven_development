# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:14:42 2019

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 2 - VALIDATION
#----------------------------------------------------------------------------------------------------------------------
# data validation is the process of ensuring data quality by assessing data against rules, constraints and routines
# validation is used during or after system integration
# it ensures that a programme operates on clean, correct and useful data
# often used for validating user input
# data type validation - verifies that individual characters are consistent with the expected data type (integer, float, string)
# range and constraint validation - checks that input is consistent with a range and has an expected sequence of characters (length check, uniqueness, special characters)
# presence check - checks that required input is given
# cross-field check - verifying the data against rules or requirements, and may involve looking at a separate database
# fixed-value check - checks if data appears elsewhere
# verification - checking that the data being entered into a form matches the source of the data
# double data entry verification - re-entering a password


# TASK 1 - REVISING USER INPUT
#--------------------------------------------------------------------------------------

#user input always returns a string data type

print("What is your age?")
age=input()

age2 = input("What is your age?")


# TASK 2 - CASTING USER INPUT TO AN INTEGER
#--------------------------------------------------------------------------------------

print("What is your age?")
age3=int(input())
print(type(age3))

# alternative
age4=int(input("What is your age?"))

# cast a variable
# not effient becuase requires two spaces in memory
age5=input("What is your age?")
age_int=int(age5)


# TASK 3 - VALIDATING A STRING
#--------------------------------------------------------------------------------------

# may require string input to be in upper or lower case
option=input("Please input yes or no.").lower()

option2=input("Please input yes or no.").upper()


# TASK 4 - VALIDATING STRING LENGTH
#--------------------------------------------------------------------------------------

password = input("Please enter a password.")
if len(password) <= 8 or len(password) >= 20:
    password = input("Please enter a password. Passwords must have between 8 and 20 characters.")

def get_password():
    password = input("Please enter a password.")
    while len(password) <= 8 or len(password) >=20:
        password = input("Please enter a password with between 8 and 20 characters.")
    return password
  
phone_number = input("Please enter a phone number.")
if len(phone_number) != 11:
    phone_number = input("Please enter a valid phone number.")
    

# TASK 5 & 6 - VALIDATING USER INPUT
#--------------------------------------------------------------------------------------

def take_user_input():
    choice=0
    choice=int(input("Select 1 to print name, 2 to print age or 3 to print city."))
    while choice != 1 or choice != 2 or choice != 3:
        choice=int(input("Select 1 to print name, 2 to print age or 3 to print city."))
        break
    if choice == 1:
        print("Harriet")
    elif choice == 2:
        print("30")
    elif choice == 3:
        print("London")
    else:
        print("Invalid selection made.")
        
take_user_input()
    

# using try and exception blocks

print("Enter 1 to print name, 2 to print age or 3 to print city.")
choice=0
while True:
    try:
        while choice < 1 or choice > 3:
            choice=int(input("What is your choice?"))
#            break
    except ValueError:
        print("Please enter a number.")
    if choice == 1:
        print("Harriet")
        break
    elif choice == 2:
        print("30")
        break
    elif choice == 3:
        print("London")
        break
    else:
        print("Invalid selection made.")
        break


# TASK 7 - CLASS-BASED USER INPUT VALIDATION
#--------------------------------------------------------------------------------------

 asser statements help to detect problems in the programme early, where the cause is clear, rather than later on as a side-effect of some other operation
 the assert condition tells the programme to test that condition, and immediately trigger an error if the condition is false
 in python, it looks like this:
 if not condition:
        raise AssertionError()

class Spam(object):
    def __init__(self, description, value):
        if not description or value <= 0:
            raise ValueError
        self.description = description
        self.value = value

# an object with parameters in the correct range is allowed        
s = Spam('s', 5)

# an object with parameters outside the correct range is not allowed
s2 = Spam('', -1)

# you can use assert statements to do this

class Spam2 (object):
    def __init__(self, description, value):
        assert description != ""
        assert value > 0
        self.description = description
        self.value = value


