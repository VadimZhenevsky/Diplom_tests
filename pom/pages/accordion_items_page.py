from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class AccordionItemsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_accordion_items_page(self):
        self.find_element(loc.accordion_items_button).click()