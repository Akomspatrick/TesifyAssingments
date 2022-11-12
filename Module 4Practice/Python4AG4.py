from selenium.webdriver.common.by import By
class ContactPage:
    def __int__(self,browser):
        self.firstnameInput = browser.find_element(By.NAME,'firstname')
        self.lastnameInput = browser.find_element(By.NAME, 'lastname')
        self.emailnameInput = browser.find_element(By.NAME, 'email')
        self.messageTextbox = browser.find_element(By.NAME, 'message')
        self.submitBtn = browser.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME,'button')