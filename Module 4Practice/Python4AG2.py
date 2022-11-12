import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExptedCond


def waitToBeVisible(browser):
    browserWait= WebDriverWait(browser,20)
    browserWait.until(ExptedCond.element_to_be_clickable((By.LINK_TEXT, 'About us')))
    academyLink = browser.find_element(By.LINK_TEXT, 'About us')
    academyLink.click()

def waitToBeLocated(browser):
    browserWait= WebDriverWait(browser,20)
    browserWait.until(ExptedCond.element_located_to_be_selected((By.LINK_TEXT, 'Academy')))
    academyLink = browser.find_element(By.LINK_TEXT, 'Academy')
    academyLink.click()

def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://www.testifyltd.com/contact"
    browser.get(site)
    #waitToBeLocated(browser)
    waitToBeVisible(browser)




    time.sleep(5)
    browser.close()

if __name__ == '__main__' :
 main()