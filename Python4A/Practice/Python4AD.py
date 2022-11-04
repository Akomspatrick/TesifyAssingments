#Navigate to the website https://academy.testifyltd.com/
#Get the element with the text "© 2022 Testify Limited. All rights reserved."
#Print out the element text, and properties, and it attributes
import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def locate_by_XPathExplore(driver):
    path = '//*[contains(text(),"2022 Testify")]'
    element = driver.find_element(By.XPATH, path)
    return element


def printElementFields(elemt):
    print("PRINTING THE ELEMENT PROPERTIES")
    print("Id",elemt.id)
    print("Text", elemt.text)
    print("Tag Name", elemt.tag_name)
    print("location", elemt.location)
    print("accessible_name ", elemt.accessible_name)
    print("aria_role", elemt.aria_role)
    print("rect ", elemt.rect)

def printAttributes(elemt):
    print("PRINTING THE ELEMENT ATTRIBUTES")
    print("Id: ",elemt.get_attribute('id'))
    print("Class: ", elemt.get_attribute('class'))
    print("Style: ", elemt.get_attribute('style'))
    print("InnerText : ", elemt.get_attribute('innerText'))
    print("innerHTML : ", elemt.get_attribute('innerHTML'))

def locateElementbyPath(browser,path):
    element = browser.find_element(By.XPATH,path)
    return element

def locateElementbyTagName(browser,elenamename):
    element = browser.find_element(By.TAG_NAME,elenamename)
    return element

def locateElementbyName(browser,elenamename):
    element = browser.find_element(By.NAME,elenamename)
    return element

def sendKeyToBrowser(elementname,*keys):
    elementname.send_keys(keys)

def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://www.testifyltd.com/contact"
    #key='PAtrick'
    browser.get(site)
    element= locateElementbyName(browser,'firstname')
    sendKeyToBrowser(element, 'Adeolu')
    element= locateElementbyName(browser,'message')
    sendKeyToBrowser(element, 'Testify training on selenium by Adewale')
    element= locateElementbyName(browser,'lastname')
    sendKeyToBrowser(element, 'Kemi')
    element= locateElementbyName(browser,'email')
    sendKeyToBrowser(element, 'Olusola@gui.com')
    element = locateElementbyName(browser, 'phone')
    sendKeyToBrowser(element, Keys.COMMAND,'v')

    formelement= locateElementbyTagName(browser,'form')
    submitButton = locateElementbyTagName(formelement, 'button')
    hiringcheckelement=locateElementbyPath(formelement,'//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[3]/div/div[3]')
    hiringcheckelement.click()
    submitButton.click()
    #element = locate_by_XPathExplore(browser)
    #printElementFields(element)
    #printAttributes(element)
    time.sleep(10)
    browser.close()

if __name__ == '__main__' :
 main()