#Create a page object model for this page https://academy.testifyltd.com/courses/test-automation-simplified
#Create another object model for this page https://academy.testifyltd.com/courses/switch-to-software-testing
#The web elements in each of your object models should not be more than 5.

import time
from SwitchToSoftwareTestingPOM  import SwitchToSoftwareTestingPOM
from  TestAutomationSimplifiedPOM import TestAutomationSimplifiedPOM
from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon



def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    switchToSoftwareTestingPOM= SwitchToSoftwareTestingPOM(browser)
    print('Testify Programme Leader    =>: ', switchToSoftwareTestingPOM.SwitchToTestingCreator.text)
    print('Contact    Caption =>: ', switchToSoftwareTestingPOM.TestifyContact.text)
    print('Payment In Dollar        Caption=>: ', switchToSoftwareTestingPOM.PayInDollarAmount.text)
    print('Payment in Naira =>: ', switchToSoftwareTestingPOM.PayInNairaAmount.text)
    print('Enroll Now   Caption =>: ', switchToSoftwareTestingPOM.EnrollNowBtn.text)
    print('________________________________________________________________________')

    testAutomationSimplifiedPOM=TestAutomationSimplifiedPOM(browser)

    print('Watch Video       Caption =>: ', testAutomationSimplifiedPOM.watchVideoBtn.text)
    print('Enroll Button     Caption =>: ', testAutomationSimplifiedPOM.EnrollNowBtn.text)
    print('Pay In Naira       Caption=>: ', testAutomationSimplifiedPOM.PayInNairaLink.text)
    print('Send Message Link Caption =>: ', testAutomationSimplifiedPOM.SendMsgLink.text)
    print('Pay In Dollar     Caption =>: ', testAutomationSimplifiedPOM.PayInDollarLink.text)
    #site="https://www.testifyltd.com/contact"
    #browser.get(site)
    time.sleep(1)

if __name__ == '__main__' :
 main()