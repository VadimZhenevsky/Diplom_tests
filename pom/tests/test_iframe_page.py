from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pom.pages.home_page import HomePage
from pom.pages.iframe_page import IframePage
from selenium.webdriver.common.by import By
import allure


@allure.feature("Iframe page")
@allure.story("Being on the allure page")
def test_being_on_iframe_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open iframe page'):
        iframe_page = IframePage(driver)
        iframe_page.open_iframe_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    text_in_header = driver.find_element(By.XPATH, '/html/body/nav/div/div/a')
    print(text_in_header.text)
    assert 'WebdriverUniversity.com (IFrame)' in text_in_header.text


@allure.feature("Iframe page")
@allure.story("Being on the allure page")
def test_click_find_out_more_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open iframe page'):
        iframe_page = IframePage(driver)
        iframe_page.open_iframe_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Switch to iframe'):
        i_frame = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(i_frame)
    with allure.step('Click find out more button'):
        find_out_more_button = driver.find_element(By.ID, 'button-find-out-more')
        find_out_more_button.click()
    popup = driver.find_element(By.CLASS_NAME, 'modal-content')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(popup)
    )
    text_check_in_popup = driver.find_element(By.CLASS_NAME, 'modal-title')
    print(text_check_in_popup.text)
    assert 'Welcome to webdriveruniversity.com' in text_check_in_popup.text
