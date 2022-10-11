from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_contact_us(self):
        self.find_element(loc.contact_us_page_button).click()
