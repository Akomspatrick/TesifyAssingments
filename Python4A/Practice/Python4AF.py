import time

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

def scrollToElement(action,element):
    action.move_to_element(element).perform()

def scrollByOffset(action,deltaY):
    action.scroll_by_amount(0,deltaY).perform()

def rightClickContext(action,element):
     scrollToElement(action,element)
     action.context_click(element).perform()

def highlightElement1(action,element,limit=15):
    action.drag_and_drop_by_offset(element,0,limit)
    action.perform()

def highlightElement2(action,element,limit=15):
    action.move_to_element(element)
    action.move_by_offset(0,10)
    action.click_and_hold(on_element=None)
    action.move_by_offset(0, 20)
    action.release(on_element=None)
    action.perform()


def main():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    site="https://www.testifyltd.com/contact"
    browser.get(site)
    action= ActionChains(browser)
    #scrollToElement(action,browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[1]'))
    scrollToElement(action, browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[3]'))
    time.sleep(1)
    scrollByOffset(action,400)
    time.sleep(2)
    scrollByOffset(action, -1000)
    # rightClickContext(action,browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[2]/div/div/div[2]/div[1]/span/img'))
    #highlightElement1(action,browser.find_element(By.TAG_NAME,'h2'))
    highlightElement2(action, browser.find_element(By.TAG_NAME, 'h2'),50)
    #element = locate_by_XPathExplore(browser)
    #printElementFields(element)
    #printAttributes(element2
    time.sleep(5)
    browser.close()

if __name__ == '__main__' :
 main()