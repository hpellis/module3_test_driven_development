# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:09:54 2019

@author: 612383249
"""


#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 6 - INTEGRATION TESTING
#----------------------------------------------------------------------------------------------------------------------
#integration testing involves testing dependencies between functions
#testing how functions work together
#aka functional tests, black box tests, acceptance tests, end-to-end tests
#end-to-end testing involves specifically checking the flow of the application, and the events that a user experience journey includes


#example test

class TestEngine():
    def __init__(self):
        self.pb = Phonebook()
        
    def test_check_db(self):
        self.checked = self.pb.check_db()
        return self.checked
    
    def test_connect_db(self):
        self.test_check_db()
        if self.checked:
            connected = self.pb.connect_db()
            if connected:
                self.connected = True
                return self.connected
            else:
                self.connected = False
                return self.connected
        else:
            print("Database does not exist.")
            
    def test_query_db(self):
        query = "SELECT * FROM business;"
        results = self.pb.query_db(query)
        if results:
            self.queried = True
        else:
            self.query = False
        return self.queried
    
    def run_tests(self):
        print(self.test_check_db())
        print(self.test_connect_db())
        print(self.test_query_db())

        
if __name__ == "main":
    newTest = TestEngine()
    TestEngine.run_tests()
            
        