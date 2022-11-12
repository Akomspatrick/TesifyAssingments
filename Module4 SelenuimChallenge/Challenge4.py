#Navigate to the website https://academy.testifyltd.com/
#Get the element with the text "© 2022 Testify Limited. All rights reserved."
#Print out the element text, and properties, and it attributes

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def locate_by_TAG_NAME(driver):
    path = '//*[contains(text(),"Around the UK")]'
    elements = driver.find_elements(By.TAG_NAME, 'li')
    return elements



def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site='https://www.bbc.com/'
    browser.get(site)

    #element = locate_by_XPathExplore(browser)
    path = 'ssrcss-1tr1co8-Grid e1t3y6kh0'
    elements = locate_by_TAG_NAME(browser)
    for x in elements:
        print(x.text)

    browser.close()

if __name__ == '__main__' :
 main()