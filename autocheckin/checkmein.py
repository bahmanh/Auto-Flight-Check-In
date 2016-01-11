from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CheckMeIn(object): 
    
    def __init__(self, firstName, lastName, confNum):
        self.firstName = firstName
        self.lastName = lastName
        self.confNum = confNum
    
    #Using PhantomJS instead of Firefox so that this script can be run without a gui in the background
    def checkIn(self):
        try:
            driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs', service_log_path='/dev/null')
            driver.get("https://www.southwest.com/flight/retrieveCheckinDoc.html")
        except selenium.common.exceptions.WebDriverException as error:
            print error.msg
            print "PhantomJS not found"
            exit(0)

        print "\nSuccessfully logged on \n"

        #Getting elements on page
        firstNameElem = driver.find_element_by_id("firstName")
        lastNameElem = driver.find_element_by_id("lastName")
        confNumElem = driver.find_element_by_id("confirmationNumber")
        buttonElem = driver.find_element_by_id("submitButton")
        
        print "Entering Data \n"

        #Sending all data to webpage 
        firstNameElem.send_keys(self.firstName)
        lastNameElem.send_keys(self.lastName)
        confNumElem.send_keys(self.confNum)
        buttonElem.click()
        
        print "Done \n"
        driver.close()
        driver.quit()

