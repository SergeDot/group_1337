from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from serge.demoqa.locators.base_page_locators import BasePageLocators
import serge.demoqa.conf as conf

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = conf.DEMOQA_BASE_URL

    def open_page(self):
        self.driver.get(self.url)

    def scroll_into_view(self, webelement):
        self.driver.execute_script('arguments[0].scrollIntoView();', webelement)

    def click_interactions(self):
        self.driver.find_element(*BasePageLocators.INTERACTIONS_TILE_TEXT).click()

    def wait_visibility(self, webelement):
        return wait(self.driver, 5).until(EC.visibility_of(self.driver.find_element(*webelement)))