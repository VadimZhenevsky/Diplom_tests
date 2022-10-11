from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_start_page(self):
        self.driver.get('http://webdriveruniversity.com/index.html')




