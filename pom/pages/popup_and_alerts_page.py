from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class PopUpAlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_popup_alerts_page(self):
        self.find_element(loc.popup_alerts_button).click()
