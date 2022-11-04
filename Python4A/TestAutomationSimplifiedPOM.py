from selenium.webdriver.common.by import By
class TestAutomationSimplifiedPOM:
    def __init__(self,browser):
        site = "https://academy.testifyltd.com/courses/test-automation-simplified"
        browser.get(site)
        self.watchVideoBtn= browser.find_element(By.XPATH,'//*[@id="faq"]/div/div/div[5]/button')
        self.PayInDollarLink = browser.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[2]/div/div[2]/div/a')
        self.PayInNairaLink = browser.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[2]/div/div[1]/div/a')
        self.SendMsgLink = browser.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[1]/div/a')
        self.EnrollNowBtn= browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[8]/div/div[2]/div[1]/div[2]/button')

