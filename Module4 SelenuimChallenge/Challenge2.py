#Using    the    firefox    browser    navigate    to
# https://www.google.com/
# enter  the  text  Python  in  thesearch  box,
# then  send  the  Enter  key.
# Get  the  text  from  theWikipedia  brief  on  the  right  side
# and  print  the  value  in  theconsole.

#Navigate to the website https://www.facebook.com/
#Find the email box and enter an email value
#Find the password box and enter a password value
#Find the Login button and click it
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import   Service
from webdriver_manager.firefox import  GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def locateElementbyName(browser,elenamename):
    element = browser.find_element(By.NAME,elenamename)
    return element

def sendKeyToBrowser(elementname,*keys):
    elementname.send_keys(keys)

def main():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    site="https://www.google.com/ "
    #key='PAtrick'
    browser.get(site)
    searchelement= locateElementbyName(browser,'q')
    time.sleep(1)
    sendKeyToBrowser(searchelement, 'Python')

    searchbtn= locateElementbyName(browser,'btnK')

    time.sleep(3)
    searchbtn.click();

    time.sleep(5)
    browser.close()

if __name__ == '__main__' :
 main()