from pom.pages.home_page import HomePage
from pom.pages.login_portal_page import LoginPortalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import allure


@allure.feature("Login portal page")
@allure.story("Being on login portal page")
def test_being_on_login_portal_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open login portal page'):
        login_portal_page = LoginPortalPage(driver)
        login_portal_page.open_login_portal_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    url = driver.current_url
    print(url)
    assert url == 'http://webdriveruniversity.com/Login-Portal/index.html'


@allure.feature("Login portal page")
@allure.story("fill in the fields with correct data")
def test_fill_in_the_fields_with_correct_data(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open login portal page'):
        login_portal_page = LoginPortalPage(driver)
        login_portal_page.open_login_portal_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill username field '):
        username_field = driver.find_element(By.ID, 'text')
        username_field.send_keys('webdriver')
    with allure.step('Fill password field '):
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('webdriver123')
    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "validation succeeded" in alert.text
    Alert(driver).accept()


@allure.feature("Login portal page")
@allure.story("click login button with empty fields")
def test_click_login_button_with_empty_fields(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open login portal page'):
        login_portal_page = LoginPortalPage(driver)
        login_portal_page.open_login_portal_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "validation failed" in alert.text
    Alert(driver).accept()


@allure.feature("Login portal page")
@allure.story("fill form fields with empty username fields")
def test_fill_form_fields_with_empty_username_fields(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open login portal page'):
        login_portal_page = LoginPortalPage(driver)
        login_portal_page.open_login_portal_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill password field '):
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('webdriver123')
    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "validation failed" in alert.text
    Alert(driver).accept()


@allure.feature("Login portal page")
@allure.story("fill form fields with empty password fields")
def test_fill_form_fields_with_empty_password_field(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open login portal page'):
        login_portal_page = LoginPortalPage(driver)
        login_portal_page.open_login_portal_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill username field '):
        username_field = driver.find_element(By.ID, 'text')
        username_field.send_keys('webdriver')
    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "validation failed" in alert.text
    Alert(driver).accept()
