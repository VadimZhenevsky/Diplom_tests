from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pom.pages.home_page import HomePage
from pom.pages.hidden_elements_page import HiddenElementsPage
from selenium.webdriver.common.by import By
import allure


@allure.feature("Hidden elements page")
@allure.story("Being on hidden elements page")
def test_being_on_hidden_elements_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open hidden elements page'):
        hidden_element_page = HiddenElementsPage(driver)
        hidden_element_page.open_hidden_elements_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text = driver.find_element(By.ID, 'main-header')
    print(check_text.text)
    assert 'Hidden Elements..' in check_text.text


@allure.feature("Hidden elements page")
@allure.story("Click zero opacity button")
def test_zero_opacity_click(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open hidden elements page'):
        hidden_element_page = HiddenElementsPage(driver)
        hidden_element_page.open_hidden_elements_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click zero opacity button'):
        zero_opacity_element = driver.find_element(By.ID, 'button3')
        zero_opacity_element.click()
    popup_message = driver.find_element(By.CLASS_NAME, 'modal-content')
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element(popup_message)
    )
    assert popup_message.is_enabled()
