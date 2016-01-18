from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class CheckMeIn(object): 
    
    def __init__(self, firstName, lastName, confNum):
        self.firstName = firstName
        self.lastName = lastName
        self.confNum = confNum
    
    #Using PhantomJS instead of Firefox so that this script can be run without a gui in the background
    def checkIn(self):
        try:
            #service_log_path is set so no logs are generated
            driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs', service_log_path='/dev/null')
            driver.get("https://www.southwest.com/flight/retrieveCheckinDoc.html")
        except WebDriverException as error:
            print error.msg
            print "PhantomJS not found"
            sys.exit(1)

        print "\nSuccessfully logged on \n"

        #Getting elements on page
        firstNameElem = driver.find_element_by_id("firstName")
        lastNameElem = driver.find_element_by_id("lastName")
        confNumElem = driver.find_element_by_id("confirmationNumber")
        submitButtonElem = driver.find_element_by_id("submitButton")
         
        print "Entering Data \n"

        #Sending all data to webpage 
        firstNameElem.send_keys(self.firstName)
        lastNameElem.send_keys(self.lastName)
        confNumElem.send_keys(self.confNum)
        submitButtonElem.click()
        
        #next page
        try: 
            checkinButtonElem = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "printDocumentsButton"))
            )
            checkinButtonElem.click()
        except TimeoutException:
            print "***Incorrect name or confirmation number. Try again!***"
        finally:
            print "Done \n"
            driver.close()
            driver.quit()
