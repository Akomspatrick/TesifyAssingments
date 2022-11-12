from time import sleep

from selenium import  webdriver
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import   ChromeDriverManager
from webdriver_manager.firefox import  GeckoDriverManager
from selenium.webdriver.common.by import By
#from  webdriver_manager.microsoft import EdgeChromiumDriverManager

def startChromeUsingManager():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
    return driver

def startFireFoxUsingManager():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()) )
    return driver


def startChrome():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    return driver

def startFireFox():
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    return driver
def PerformactionOnSite(driver):
    element = driver.find_element(By.TAG_NAME,"h1")
    print(element.text)

def getSite(driver,site):
    driver.get(site)

def SleepandClose(driver):
    sleep(10)
    driver.close()

#driver= startChrome();
#driver =startChromeUsingManager();

#driver =startFireFox()
site="https://www.testifyltd.com"

driver = startFireFoxUsingManager()
getSite(driver,site)
PerformactionOnSite(driver)
SleepandClose(driver)
print("Done....")