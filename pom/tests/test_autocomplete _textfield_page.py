from selenium.webdriver import ActionChains
from pom.pages.home_page import HomePage
from pom.pages.autocomplete_textfield_page import AutocompleteTextfieldPage
from selenium.webdriver.common.by import By
import allure


@allure.feature("Autocomplete textfield page")
@allure.story("Being on the autocomplete textfield page")
def test_being_on_autocomplete_textfield_page(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open autocomplete textfield page'):
        autocomplete_textfield_page = AutocompleteTextfieldPage(driver)
        autocomplete_textfield_page.open_autocomplete_textfield_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    check_text = driver.find_element(By.CLASS_NAME, 'section_header')
    print(check_text.text)
    assert 'Autocomplete TextField' in check_text.text


@allure.feature("Autocomplete textfield page")
@allure.story("Fill food item with word duck")
def test_fill_food_item_with_word_duck(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open_start_page()
    with allure.step('Open autocomplete textfield page'):
        autocomplete_textfield_page = AutocompleteTextfieldPage(driver)
        autocomplete_textfield_page.open_autocomplete_textfield_page()
    with allure.step('Switch to new tab'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Entering the letter d in the field'):
        food_item_field = driver.find_element(By.ID, 'myInput')
        food_item_field.send_keys('d')
    with allure.step('Hover over the word duck and click'):
        item_duck = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/section'
                                        '/div/div[2]/form/div/div/div[3]')
        ActionChains(driver).move_to_element(item_duck).click().perform()
    with allure.step('click submit button'):
        submit_button = driver.find_element(By.ID, 'submit-button')
        submit_button.click()
    url = driver.current_url
    print(url)
    assert url == 'http://webdriveruniversity.com/Autocomplete-TextField' \
                  '/autocomplete-textfield.html?food-item=Duck'
