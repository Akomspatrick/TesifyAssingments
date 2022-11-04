#Navigate to the website https://academy.testifyltd.com/
#Get the element with the text "© 2022 Testify Limited. All rights reserved."
#Print out the element text, and properties, and it attributes

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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

def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site='https://academy.testifyltd.com/'
    browser.get(site)

    element = locate_by_XPathExplore(browser)
    printElementFields(element)
    printAttributes(element)

    browser.close()

if __name__ == '__main__' :
 main()