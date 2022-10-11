import allure
from pom.pages.home_page import HomePage
from pom.pages.accordion_items_page import AccordionItemsPage
from selenium.webdriver.common.by import By


@allure.feature("According items Page")
@allure.story("Being on the accordion items page")
def test_being_on_accordion_items_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open accordion_items_page'):
        accordion_items_page = AccordionItemsPage(driver)
        accordion_items_page.open_accordion_items_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    url = driver.current_url
    print(url)
    assert url == 'http://webdriveruniversity.com/Accordion/index.html'


@allure.feature("According items Page")
@allure.story("Click manual testing button ")
def test_click_on_manual_testing_button(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open accordion items page'):
        accordion_items_page = AccordionItemsPage(driver)
        accordion_items_page.open_accordion_items_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Click manual testing button'):
        manual_testing_button = driver.find_element(By.ID, 'manual-testing-accordion')
        manual_testing_button.click()
    text_in_dropdown_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/p')
    print(text_in_dropdown_button.text)
    assert text_in_dropdown_button.is_displayed()
