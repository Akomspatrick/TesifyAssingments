#Get the element with the text "© 2022 Testify Limited. All rights reserved."

#Print out the element text, and properties, and it attributes
import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def printElementProperty(element):
    print("Check State: ", element.get_property('checked'))


def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site='https://www.w3.org/WAI/ARIA/apg/example-index/checkbox/checkbox-mixed'
    browser.get(site)
    lettucechk = browser.find_element(By.ID, 'cond1')
    tomatocechk=browser.find_element(By.ID,'cond2')
    mustardchk = browser.find_element(By.ID, 'cond3')
    sprchk = browser.find_element(By.ID, 'cond4')
    printElementProperty(lettucechk)
    printElementProperty(tomatocechk)
    printElementProperty(mustardchk)
    printElementProperty(sprchk)
    time.sleep(30)
    browser.close()


if __name__ == '__main__' :
 main()