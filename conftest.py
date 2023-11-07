import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--window-size=1880,1220')
    return options

@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print(f'\nQuitting browser...')
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait
