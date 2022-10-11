from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class HiddenElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_hidden_elements_page(self):
        self.find_element(loc.hidden_elements_button).click()
