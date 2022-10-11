from pom.pages.base_page import BasePage
from pom.pages.locators import home_page_locators as loc


class FileUploadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_file_upload_page(self):
        self.find_element(loc.file_upload_button).click()

