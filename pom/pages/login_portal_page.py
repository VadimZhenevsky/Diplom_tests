from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class LoginPortalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login_portal_page(self):
        self.find_element(loc.login_portal_button).click()
