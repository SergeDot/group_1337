import time
from serge.demoqa.data.demoqa_data import DemoqaData
from serge.demoqa.locators.interactions_locators import InteractionsLocators
from serge.demoqa.pages.interactions_page import InteractionsPage


class TestInteractions:
    locator = InteractionsLocators()

    def open_page(self, driver):
        page = InteractionsPage(driver)
        page.open_page()
        page.click_interactions()
        time.sleep(5)
        return page

    def test_drag_and_drop_and_drop(self, driver):
        page = self.open_page(driver)
        page.open_droppable_page()

        drag = driver.find_element(*self.locator.DRAG)
        drop = driver.find_element(*self.locator.DROP)
        time.sleep(3)

        page.drag_and_drop(drag, drop)
        page.wait_visibility(self.locator.DROP_TEXT)
        text = driver.find_element(*self.locator.DROP_TEXT).text
        assert text == DemoqaData.DROP_TEXT


