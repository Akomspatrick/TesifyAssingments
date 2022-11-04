from selenium.webdriver.common.by import By
class SwitchToSoftwareTestingPOM:
    def __init__(self,browser):
        site = "https://academy.testifyltd.com/courses/switch-to-software-testing"
        browser.get(site)
        self.SwitchToTestingCreator = browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[12]/div/div/div[1]/div[2]/p')
        self.PayInDollarAmount = browser.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[2]/div/div[2]/p[3]')
        self.PayInNairaAmount = browser.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[2]/div/div[1]/p[3]')
        self.TestifyContact = browser.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[1]/div[1]/div/p')

        self.EnrollNowBtn = browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[8]/div/div[2]/div[1]/div[2]/button')

