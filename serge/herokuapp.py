import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--window-size=1680,920')
    options.add_argument('--incognito')
    return options

@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print(f'\nQuitting browser...')
    driver.quit()

def test_broken_image(driver):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    img_link = driver.find_element(By.CSS_SELECTOR, '.example img:nth-of-type(1)').get_attribute('src')

    driver.get(img_link)
    page_source = driver.page_source
    print(page_source)
    print('Not Found' in page_source)
    assert 'Not Found' in page_source
    img_list = driver.find_elements(By.TAG_NAME, 'img')
    print(len(img_list))
    assert len(img_list) == 0

def test_valid_image(driver):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    img_element = driver.find_element(By.CSS_SELECTOR, '.example img:nth-of-type(3)')
    img_size = img_element.size
    print(img_size)
    img_width = img_element.size['width']
    print(img_width)

def test_broken_image_size(driver):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    img_element = driver.find_element(By.CSS_SELECTOR, '.example img:nth-of-type(1)')
    img_size = img_element.size
    print(img_size)
    img_width = img_element.size['width']
    print(img_width)

