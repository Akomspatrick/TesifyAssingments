#Navigate to the website https://www.facebook.com/
#Find the email box and enter an email value
#Find the password box and enter a password value
#Find the Login button and click it
import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def locateElementbyName(browser,elenamename):
    element = browser.find_element(By.NAME,elenamename)
    return element

def sendKeyToBrowser(elementname,*keys):
    elementname.send_keys(keys)

def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://www.facebook.com/"
    #key='PAtrick'
    browser.get(site)
    element= locateElementbyName(browser,'email')
    sendKeyToBrowser(element, 'Akomspatrick@yahoo.com')
    element= locateElementbyName(browser,'pass')
    #sendKeyToBrowser(element, 'xxxx')
    time.sleep(3)
    sendKeyToBrowser(element, Keys.COMMAND, 'v')
    #I will paste the password
    submitButton=locateElementbyName(browser,'login')
    time.sleep(3)
    submitButton.click();

    time.sleep(5)
    browser.close()

if __name__ == '__main__' :
 main()