from serge.demoqa.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from serge.demoqa.locators.interactions_locators import InteractionsLocators


class InteractionsPage(BasePage):

    locator = InteractionsLocators()

    def open_droppable_page(self):
        self.driver.find_element(*self.locator.DROPPABLE_MENU).click()

    def drag_and_drop(self, drag, drop):
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
