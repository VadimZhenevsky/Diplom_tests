import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    print('\nSTART\n')
    options = Options()
    service = Service(executable_path='C:/Windows/chromedriver.exe')
    chrom_driver = webdriver.Chrome(service=service, options=options)
    chrom_driver.maximize_window()
    chrom_driver.implicitly_wait(10)
    yield chrom_driver
    print('\nEND\n')
    chrom_driver.quit()
