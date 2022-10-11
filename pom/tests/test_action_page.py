from selenium.webdriver import ActionChains
from pom.pages.home_page import HomePage
from pom.pages.actions_page import ActionPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import allure


@allure.feature("Action Page")
@allure.story("Being on action page")
def test_being_on_action_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open action page'):
        action_page = ActionPage(driver)
        action_page.open_action_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text = driver.find_element(By.ID, 'main-header')
    print(check_text.text)
    assert 'The Key to Success is to take massive ACTION!' in check_text.text


@allure.feature("Action Page")
@allure.story("Drag and drop test")
def test_drag_and_drop(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open action page'):
        action_page = ActionPage(driver)
        action_page.open_action_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Drag and drop process'):
        left_element = driver.find_element(By.ID, 'draggable')
        right_element = driver.find_element(By.ID, 'droppable')
        ActionChains(driver).drag_and_drop(left_element, right_element).perform()
    print(right_element.text)
    assert 'Dropped!' in right_element.text


@allure.feature("Action Page")
@allure.story("Double click ")
def test_double_click(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open action page'):
        action_page = ActionPage(driver)
        action_page.open_action_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Double click process'):
        double_click_element = driver.find_element(By.ID, 'double-click')
        ActionChains(driver).double_click(double_click_element).perform()
        color_double_click_element_after_click = double_click_element.value_of_css_property('background-color')
    print(color_double_click_element_after_click)
    assert color_double_click_element_after_click == 'rgba(147, 203, 90, 1)'


@allure.feature("Action Page")
@allure.story("Click in the drop down menu")
def test_click_in_the_drop_down_menu(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open action page'):
        action_page = ActionPage(driver)
        action_page.open_action_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click in the drop down menu'):
        hover_button = driver.find_element(By.CLASS_NAME, 'dropbtn')
        list_1 = driver.find_element(By.CLASS_NAME, 'list-alert')
        ActionChains(driver).move_to_element(hover_button).click(list_1).perform()
    alert = driver.switch_to.alert
    print(alert.text)
    assert "Well done you clicked on the link!" in alert.text
    Alert(driver).accept()


@allure.feature("Action Page")
@allure.story("Click and hold ")
def test_click_and_hold(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open action page'):
        action_page = ActionPage(driver)
        action_page.open_action_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click and hold button'):
        click_and_hold_element = driver.find_element(By.ID, 'click-box')
        ActionChains(driver).click_and_hold(click_and_hold_element).perform()
    check_text = driver.find_element(By.ID, 'click-box')
    print(check_text.text)
    assert 'Well done! keep holding that click now.....' in check_text.text
