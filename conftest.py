import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--window-size=1880,1220')
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options

@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print(f'\nQuitting browser...')
    driver.quit()

