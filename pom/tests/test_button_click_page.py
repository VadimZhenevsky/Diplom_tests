from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pom.pages.home_page import HomePage
from pom.pages.button_click_page import ButtonClickPage
from selenium.webdriver.common.by import By
import allure


@allure.feature("Button click page")
@allure.story("Being on the button click page")
def test_being_on_button_click_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open button click page'):
        sample_page = ButtonClickPage(driver)
        sample_page.open_button_click_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text = driver.find_element(By.CLASS_NAME, 'text-center')
    print(check_text.text)
    assert 'Lets Get Clicking!' in check_text.text


@allure.feature("Button click page")
@allure.story("test click me button")
def test_click_me_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open button click page'):
        sample_page = ButtonClickPage(driver)
        sample_page.open_button_click_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click on click me button'):
        click_me_button = driver.find_element(By.XPATH, '//span[@id="button1"]')
        click_me_button.click()
    popup = driver.find_element(By.CLASS_NAME, 'modal-content')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(popup)
        )
    text_check = driver.find_element(By.CLASS_NAME, 'modal-title')
    print(text_check.text)
    assert 'Congratulations!' in text_check.text
