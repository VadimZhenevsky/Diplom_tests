from pom.pages.home_page import HomePage
from pom.pages.file_upload_page import FileUploadPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import allure


@allure.feature("File upload page")
@allure.story("Being on file upload page")
def test_being_on_file_upload_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open file upload page'):
        file_upload_page = FileUploadPage(driver)
        file_upload_page.open_file_upload_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text_on_page = driver.find_element(By.CLASS_NAME, 'text-center')
    assert 'File Upload' in check_text_on_page.text
    print(check_text_on_page.text)


@allure.feature("File upload page")
@allure.story("click button send without upload file")
def test_click_button_send_without_upload_file(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open file upload page'):
        file_upload_page = FileUploadPage(driver)
        file_upload_page.open_file_upload_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click button send'):
        send_button = driver.find_element(By.ID, 'submit-button')
        send_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "You need to select a file to upload!" in alert.text
    Alert(driver).accept()


@allure.feature("File upload page")
@allure.story("upload and send file")
def test_send_file(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open file upload page'):
        file_upload_page = FileUploadPage(driver)
        file_upload_page.open_file_upload_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Upload file'):
        file_uploading = driver.find_element(By.ID, 'myFile').find_element(By.XPATH, "//input[@type='file']")
        file_uploading.send_keys("C:/Users/v.zhenevskiy/Desktop/diplom_tests/Diplom_tests/pom/files/FOTO.jpg")
    with allure.step('Click send button'):
        send_button = driver.find_element(By.ID, 'submit-button')
        send_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "Your file has now been uploaded!" in alert.text
    Alert(driver).accept()
