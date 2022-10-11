from selenium.webdriver.support.wait import WebDriverWait
from pom.pages.home_page import HomePage
from pom.pages.ajax_loader_page import AjaxLoaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Ajax loader page")
@allure.story("Click click me button")
def test_click_modal_popup_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open ajax loader page'):
        ajax_loader_page = AjaxLoaderPage(driver)
        ajax_loader_page.open_ajax_loader_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(10)
    with allure.step('Click click me button'):
        click_me_button = driver.find_element(By.ID, 'button1')
        click_me_button.click()
    popup = driver.find_element(By.CLASS_NAME, 'modal-content')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(popup)
    )
    text_check_in_window = driver.find_element(By.CLASS_NAME, 'modal-title')
    print(text_check_in_window.text)
    assert 'Well Done For Waiting....!!!' in text_check_in_window.text
