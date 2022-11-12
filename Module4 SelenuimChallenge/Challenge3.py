#Navigate any browser to https://weather.com/ get thecurrent  temperature  and
# print  it  out  in  the  terminal.  Thenprint out the temperature for Morning,
# Afternoon, Evening,and Overnight.4. Navigate to https://www.bbc.com/  and
# print  out  thetop 10 latest news from the home page.


import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExptedCond

def locateElementbyName(browser,elenamename):
    element = browser.find_element(By.NAME,elenamename)
    return element

def locate_by_XPathExplore(driver):
    path='/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/div[1]/span'
    path='//*[@id="WxuSavedLocations-header-9aea3e61-fbf8-4da4-9e07-f96abf18cdf1"]/div/div/div/div[1]/div/div/div/a[1]/span/text()[1]'
    element = driver.find_element(By.XPATH, path)
    return element

def sendKeyToBrowser(elementname,*keys):
    elementname.send_keys(keys)


def waitToBeVisible(browser):
    browserWait= WebDriverWait(browser,20)
    #browserWait.until(ExptedCond.element_to_be_clickable((By.CLASS_NAME, 'styles--temperature--3YaGV')))
    #academyLink = browser.find_element(By.CLASS_NAME, 'styles--temperature--3YaGV')
    path = '//*[@id="WxuSavedLocations-header-9aea3e61-fbf8-4da4-9e07-f96abf18cdf1"]/div/div/div/div[1]/div/div/div/a[1]/span/text()[1]'

    browserWait.until(ExptedCond.element_to_be_clickable((By.CLASS_NAME, 'styles--temperature--3YaGV')))
    academyLink = browser.find_elements(By.CLASS_NAME, 'styles--temperature--3YaGV')
    for x in academyLink :
       print(x.text)
def waitToBeLocated(browser):
    browserWait= WebDriverWait(browser,20)
    browserWait.until(ExptedCond.element_located_to_be_selected((By.CLASS_NAME, 'styles--temperature--3YaGV')))
    academyLink = browser.find_element(By.CLASS_NAME, 'styles--temperature--3YaGV')
    print(academyLink.text)

def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://weather.com/"
    browser.get(site)
    #waitToBeLocated(browser)
    waitToBeVisible(browser)






if __name__ == '__main__' :
 main()


