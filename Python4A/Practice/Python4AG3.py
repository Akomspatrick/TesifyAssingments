import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By





def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://www.testifyltd.com/contact"
    browser.get(site)
    browser.execute_script("""
    const forms = document.getElementsByTagName('form')
    for (const form of forms){
      form.style.backgroundColor ='red'
    } 
    const links = document.getElementsByTagName('a')
    for (const link of links){
      link.style.backgroundColor ='green'
      link.style.color ='yellow'
    } 

    """)
    time.sleep(4)
    browser.execute_script("alert('heloooooo world')")
    #waitToBeLocated(browser)





    time.sleep(5)
    browser.close()

if __name__ == '__main__' :
 main()