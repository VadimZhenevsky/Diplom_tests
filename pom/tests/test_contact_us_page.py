from pom.pages.home_page import HomePage
from pom.pages.contact_us_page import ContactUsPage
from selenium.webdriver.common.by import By
import allure


@allure.feature("Contact us page")
@allure.story("Being on contact us page")
def test_being_on_contact_us_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text_on_page = driver.find_element(By.CLASS_NAME, 'section_header')
    print(check_text_on_page.text)
    assert 'CONTACT US' in check_text_on_page.text


@allure.feature("Contact us page")
@allure.story("Fill out the entire form")
def test_fill_out_the_form(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill first name field'):
        first_name_field = driver.find_element(By.NAME, 'first_name')
        first_name_field.send_keys('vadzim')
    with allure.step('Fill last name field'):
        last_name_field = driver.find_element(By.NAME, 'last_name')
        last_name_field.send_keys('zhaneuski')
    with allure.step('Fill email field'):
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys('vadzim@gmail.com')
    with allure.step('Fill comment field'):
        comment_field = driver.find_element(By.NAME, 'message')
        comment_field.send_keys('ЗАПОЛНИЛ')
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.XPATH, '//input[@value="SUBMIT"]')
        submit_button.click()
    text_check = driver.find_element(By.ID, 'contact_reply')
    print(text_check.text)
    assert 'Thank You for your Message!' in text_check.text


@allure.feature("Contact us page")
@allure.story("Fill out the form without first name")
def test_fill_out_the_form_without_first_name_field(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill last name field'):
        last_name_field = driver.find_element(By.NAME, 'last_name')
        last_name_field.send_keys('zhaneuski')
    with allure.step('Fill email field'):
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys('vadzim@gmail.com')
    with allure.step('Fill comment field'):
        comment_field = driver.find_element(By.NAME, 'message')
        comment_field.send_keys('ЗАПОЛНИЛ')
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.XPATH, '//input[@value="SUBMIT"]')
        submit_button.click()
    check_error_message = driver.find_element(By.TAG_NAME, 'body')
    print(check_error_message.text)
    assert "Error: all fields are required" in check_error_message.text


@allure.feature("Contact us page")
@allure.story("Fill out the form without last name")
def test_fill_out_the_form_without_last_name_field(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill first name field'):
        first_name_field = driver.find_element(By.NAME, 'first_name')
        first_name_field.send_keys('vadzim')
    with allure.step('Fill email field'):
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys('vadzim@gmail.com')
    with allure.step('Fill comment field'):
        comment_field = driver.find_element(By.NAME, 'message')
        comment_field.send_keys('ЗАПОЛНИЛ')
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.XPATH, '//input[@value="SUBMIT"]')
        submit_button.click()
    check_error_message = driver.find_element(By.TAG_NAME, 'body')
    print(check_error_message.text)
    assert "Error: all fields are required" in check_error_message.text


@allure.feature("Contact us page")
@allure.story("Fill out the form without email")
def test_fill_out_the_form_without_email_field(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill first name field'):
        first_name_field = driver.find_element(By.NAME, 'first_name')
        first_name_field.send_keys('vadzim')
    with allure.step('Fill last name field'):
        last_name_field = driver.find_element(By.NAME, 'last_name')
        last_name_field.send_keys('zhaneuski')
    with allure.step('Fill comment field'):
        comment_field = driver.find_element(By.NAME, 'message')
        comment_field.send_keys('ЗАПОЛНИЛ')
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.XPATH, '//input[@value="SUBMIT"]')
        submit_button.click()
    check_error_message = driver.find_element(By.TAG_NAME, 'body')
    print(check_error_message.text)
    assert "Error: all fields are required" in check_error_message.text


@allure.feature("Contact us page")
@allure.story("Fill out the form without comment")
def test_fill_out_the_form_without_comment(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Fill first name field'):
        first_name_field = driver.find_element(By.NAME, 'first_name')
        first_name_field.send_keys('vadzim')
    with allure.step('Fill last name field'):
        last_name_field = driver.find_element(By.NAME, 'last_name')
        last_name_field.send_keys('zhaneuski')
    with allure.step('Fill email field'):
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys('vadzim@gmail.com')
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.XPATH, '//input[@value="SUBMIT"]')
        submit_button.click()
    check_error_message = driver.find_element(By.TAG_NAME, 'body')
    print(check_error_message.text)
    assert "Error: all fields are required" in check_error_message.text


@allure.feature("Contact us page")
@allure.story("Click on the submit button without filling in the fields")
def test_click_on_the_submit_button_without_filling_in_the_fields(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open contact us page'):
        contact_us_page = ContactUsPage(driver)
        contact_us_page.open_contact_us()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.XPATH, '//input[@value="SUBMIT"]')
        submit_button.click()
    check_error_message = driver.find_element(By.TAG_NAME, 'body')
    print(check_error_message.text)
    assert "Error: all fields are required" and "Error: Invalid email address" in check_error_message.text
