# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:42 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 8 - MOBILE DATA PURCHASE BUNDLE
#----------------------------------------------------------------------------------------------------------------------


def data_bundle_purchase(true_passcode, balance):
    if password_check(true_passcode):
        choice=choose_transaction()
        if choice==1 and balance_check(balance):
            print(f"Your balance is {balance}.")
            return (f"Customer balance is {balance}.")
        elif choice== 1:
            print ("\nYou have a negative balance.")
            return("Customer has a negative balance.") 
        elif choice == 2:
            if phone_confirm():
                print("\nYou have successfully confirmed your phone number.")
                if select_data(balance):
                    print("\nSuccessful transaction.")
                    return("Successful transaction.")
            else:
                print("Unsuccessful validation of phone number.")
                return ("Unsuccessful validation of phone number.")      
    else:
        print("\nYou have not entered your password correctly.")
        return "Wrong password."    
    
def balance_check(balance):
    if balance > 0:
        return True
    else:
        return False

    
def password_check(true_passcode):
    while True:
        try:
            attempt=input("Please enter your password: ")
            if attempt == true_passcode:
                return True
            else:
                attempt2=input("Second chance to enter your password: ")
                if attempt2 == true_passcode:
                    return True
                else:
                    attempt3=input("Final chance to enter your password: ")
                    if attempt3 == true_passcode:
                        return True
                    else:
                        return False
        except:
            pass
   
def choose_transaction():
    while True:
        try:
            choice=int(input("Enter 1 to check your credit balance, and 2 to purchase a data bundle. "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Invalid selection. Please enter 1 or 2.")
        except ValueError:
            print("Invalid selection made.")            
            
def phone_confirm():
    while True:
        try:
            phone1 = int(input("Please enter your phone number: "))
            phone2 = int(input("Please enter your phone number: "))
            if len(str(phone1)) == 11 and len(str(phone2)) == 11:
                if phone1 == phone2:
                    return True
                else:
                    print("Phone number not confirmed.")
            else:
                print("Please enter a valid 11-digit phone number.")
        except ValueError:
            print("Invalid selection made.")
            
def select_data(balance):
    while True:
       try:
           data_selection=int(input("How much do you want to spend on data? "))      
           if data_selection % 5 == 0:
               print (f"\nYou have selected to spend £{data_selection}.")
               if data_selection <= balance:
                   print("\nYou have sufficient balance for this transaction.")
                   return True
               else:
                   print("\nYou do not have sufficient balance for this transaction.")
           else:
                print ("\nInvalid selection. You must select a multiple of £5 and have sufficient balance in your account for this transaction.")
                
       except ValueError:
           print("Invalid selection made.")
                

    



    


