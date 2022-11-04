from selenium.webdriver.common.by import By
class ContactPage:
    def __init__(self,browser):
        self.brw = browser
        site = "https://www.testifyltd.com/contact"
        browser.get(site)
        self.firstnameInput = browser.find_element(By.NAME,'firstname')

        self.lastnameInput = browser.find_element(By.NAME, 'lastname')
        self.emailnameInput = browser.find_element(By.NAME, 'email')
        self.messageTextbox = browser.find_element(By.NAME, 'message')
        self.submitBtn = browser.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME,'button')

    def sendkey(self):
        self.firstnameInput = self.brw.find_element(By.NAME, 'firstname')
        self.firstnameInput.send_keys('Initat Constructor')
