import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon



def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://www.testifyltd.com/contact"
    browser.get(site)
    form= browser.find_element(By.TAG_NAME,'form')
    print(" Form States: ", form.is_displayed(),form.is_enabled())
    submitbtn= browser.find_element(By.TAG_NAME,'button')
    print(" Form States: ", submitbtn.is_displayed(),submitbtn.is_enabled())
    browser.maximize_window();
    time.sleep(2)
    browser.refresh()
    time.sleep(2)
    browser.find_element(By.LINK_TEXT,'About us').click()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.forward()
    time.sleep(2)
    browser.close()

if __name__ == '__main__' :
 main()