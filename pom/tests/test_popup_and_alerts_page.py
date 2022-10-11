from selenium.webdriver.support.wait import WebDriverWait
from pom.pages.home_page import HomePage
from pom.pages.popup_and_alerts_page import PopUpAlertsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Popup and alerts page")
@allure.story("Being on the popup and alerts page")
def test_being_on_popup_and_alerts_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text_on_page = driver.find_element(By.ID, 'main-header')
    print(check_text_on_page.text)
    assert 'Annoying Popup & Alerts!' in check_text_on_page.text


@allure.feature("Popup and alerts page")
@allure.story("click javascript alert button")
def test_click_javascript_alert_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click javascript alert button '):
        javascript_alert_button = driver.find_element(By.ID, 'button1')
        javascript_alert_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "I am an alert box!" in alert.text
    Alert(driver).accept()


@allure.feature("Popup and alerts page")
@allure.story("click in modal popup button")
def test_click_click_modal_popup_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click modal popup button'):
        modal_popup_button = driver.find_element(By.ID, 'button2')
        modal_popup_button.click()
    window_modal_popup = driver.find_element(By.CLASS_NAME, 'modal-content')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(window_modal_popup)
    )
    text_check = driver.find_element(By.CLASS_NAME, 'modal-title')
    print(text_check.text)
    assert 'It’s that Easy!! Well I think it is.....' in text_check.text
    close_button = driver.find_element(By.CLASS_NAME, 'close')
    close_button.click()


@allure.feature("Popup and alerts page")
@allure.story("click in ajax loader button")
def test_click_ajax_loader_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click modal popup button'):
        modal_popup_button = driver.find_element(By.ID, 'button3')
        modal_popup_button.click()
    driver.implicitly_wait(10)
    with allure.step('Click clickme button'):
        clickme_button = driver.find_element(By.ID, 'button1')
        clickme_button.click()
    window_ajax_loader = driver.find_element(By.CLASS_NAME, 'modal-content')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(window_ajax_loader)
    )
    new_text_check = driver.find_element(By.CLASS_NAME, 'modal-title')
    print(new_text_check.text)
    assert 'Well Done For Waiting....!!!' in new_text_check.text
    close_button = driver.find_element(By.CLASS_NAME, 'close')
    close_button.click()


@allure.feature("Popup and alerts page")
@allure.story("click in javascript confirm box button")
def test_click_javascript_confirm_box_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click javascript confirm box button '):
        javascript_confirm_box_button = driver.find_element(By.ID, 'button4')
        javascript_confirm_box_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "Press a button!" in alert.text
    Alert(driver).accept()


@allure.feature("Popup and alerts page")
@allure.story("click ok after click javascript confirm box button")
def test_click_ok_after_click_javascript_confirm_box_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click javascript confirm box button '):
        javascript_confirm_box_button = driver.find_element(By.ID, 'button4')
        javascript_confirm_box_button.click()
    with allure.step('Click OK'):
        alert = driver.switch_to.alert
        Alert(driver).accept()
    message_ok = driver.find_element(By.ID, 'confirm-alert-text')
    print(message_ok.text)
    assert "You pressed OK!" in message_ok.text


@allure.feature("Popup and alerts page")
@allure.story("click cancel after click javascript confirm box button")
def test_click_cancel_after_click_javascript_confirm_box_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open popup and alerts page'):
        popup_and_alerts_page = PopUpAlertsPage(driver)
        popup_and_alerts_page.open_popup_alerts_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click javascript confirm box button '):
        javascript_confirm_box_button = driver.find_element(By.ID, 'button4')
        javascript_confirm_box_button.click()
    with allure.step('Click cancel'):
        alert = driver.switch_to.alert
        Alert(driver).dismiss()
    message_cancel = driver.find_element(By.ID, 'confirm-alert-text')
    print(message_cancel.text)
    assert "You pressed Cancel!" in message_cancel.text
