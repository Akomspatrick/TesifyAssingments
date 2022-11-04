from selenium.webdriver.common.by import By
class AboutUsPage:
    def __init__(self,browser):
        site = "https://www.testifyltd.com/about"
        browser.get(site)
        self.title = browser.find_element(By.TAG_NAME,'h1')
