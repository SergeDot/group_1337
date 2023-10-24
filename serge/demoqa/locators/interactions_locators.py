from selenium.webdriver.common.by import By


class InteractionsLocators:
    DROPPABLE_MENU = (By.XPATH, '//span[text()="Droppable"]')
    DRAG = (By.CSS_SELECTOR, 'div#draggable')
    DROP = (By.CSS_SELECTOR, 'div#droppable')
    DROP_TEXT = By.CSS_SELECTOR, 'div#droppable > p'