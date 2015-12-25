from selenium import webdriver
from selinium.webdriver.common.keys import Keys

class CheckMeIn(object): 
    

    def __init__(self, firstName, lastName, confNum):
        self.firstName = firstName
        self.lastName = lastName
        self.confNum = confNum

