#Visit the website https://academy.testifyltd.com/
#Locate the button with the text "Explore Courses" and print out the element
#Locate the element with the text "Subscribe to receive training updates from Testify" and print it.

from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def locate_by_XPathExplore(driver):
    path = '//button[contains(span/text(),"EXPLORE COURSES")]'
    rr = driver.find_element(By.XPATH, path)
    print("The Element is", rr)
    print("The Text value is",rr.text)

def locate_by_XPath_Subscribe(driver):
    path = '//h2'
    rr = driver.find_elements(By.XPATH, path)
    for r in rr:
        if r.accessible_name.__contains__("Subscribe to receive training updates from Testify"):
         print("The Element is ", r)
         print("The  tagname is ", r.tag_name)
         print("The value is ",r.accessible_name)






def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_XPathExplore(driver)
    locate_by_XPath_Subscribe(driver)
    driver.close()


if __name__ == '__main__' :
 main()