import time
from ContanctPage  import ContactPage
from  AboutUsPage import AboutUsPage
from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon



def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #site="https://www.testifyltd.com/contact"
    #browser.get(site)
    contactpage= ContactPage(browser)
    contactpage.sendkey()
    contactpage.submitBtn.click()

    print('First Name : ', contactpage.firstnameInput.text)
    time.sleep(2)
    aboutus=AboutUsPage(browser)

    print('Title : ', aboutus.title.text)


    #site="https://www.testifyltd.com/contact"
    #browser.get(site)
    time.sleep(5)

if __name__ == '__main__' :
 main()