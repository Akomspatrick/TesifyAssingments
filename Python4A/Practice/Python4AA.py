import time
from selenium import webdriver
from selenium.webdriver .chrome.service import   Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def locate_by_Id(driver):
    print("calinnnnn")
    emailelement = driver.find_element(By.ID,"email")
    print("Email", emailelement.text)
    passelement = driver.find_element(By.ID,"pass")
    print("ID", passelement.text)
def locate_by_Name(driver):
    firstname= driver.find_element(By.NAME,'firstname')
    print("NAME ", firstname.text)

def locate_by_className(driver):
    rr= driver.find_elements(By.CLASS_NAME,'react-reveal')
    for r in rr:
        print("CLASS_NAME", r.text)

def locate_by_tagName(driver):
    rr = driver.find_elements(By.TAG_NAME, 'input')
    for r in rr:
      print("TAG_NAME", r.text)


def locate_by_CSSSelector(driver):
    rr = driver.find_elements(By.CSS_SELECTOR, 'div.relative')
    for r in rr:
      print("CSS_SELECTOR", r.text)

def locate_by_XPath(driver):
    value='//*[@id="__next"]/main/section[1]/div/div[1]/div[2]'
    rr = driver.find_elements(By.XPATH, '//form[1]')
    for r in rr:
      print("XPATH", r.text)


def locate_by_LinkTex(driver):
    value = 'Academy'
    rr = driver.find_elements(By.LINK_TEXT, value)
    for r in rr:
        print("Lin Text: ", r.text)


def locate_by_Partail(driver):
    value = 'adem'
    rr = driver.find_elements(By.PARTIAL_LINK_TEXT, value)
    for r in rr:
        print("Partial Link", r.text)


def locatesubelementWithId(driver):
    rr = driver.find_element(By.TAG_NAME, 'form')
    # locate email of the first form
    emailElement = rr.find_element(By.NAME, 'email')
    print("The email name is", emailElement.accessible_name)
    return emailElement

def printElementFields(elemt):
    print("PRINTING THE ELEMENT PROPERTIES")
    print("Id",elemt.id)
    print("Text", elemt.text)
    print("Tag Name", elemt.tag_name)
    print("location", elemt.location)
    print("accessible_name ", elemt.accessible_name)
    print("aria_role", elemt.aria_role)
    print("rect ", elemt.rect)

def printAttributes(elemt):
    print("PRINTING THE ELEMENT ATTRIBUTES")
    print("Id: ",elemt.get_attribute('id'))
    print("Class: ", elemt.get_attribute('class'))
    print("Style: ", elemt.get_attribute('style'))
    print("InnerText : ", elemt.get_attribute('innerText'))
    print("innerHTML : ", elemt.get_attribute('innerHTML'))



def main():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get("https://facebook.com")
    #locate_by_Id(driver)
    driver.get("https://www.testifyltd.com/contact")
   # locate_by_tagName(driver)
    #locate_by_CSSSelector(driver)
    #locate_by_XPath(driver)
    #locate_by_Name(driver)
    #locate_by_LinkTex(driver)

    #locate_by_Partail(driver)

    #locate_by_className(driver)
    emailElement= locatesubelementWithId(driver)
    printElementFields(emailElement)
    printAttributes(emailElement)
    driver.close()


main()
