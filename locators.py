from selenium.webdriver.common.by import By

# LOCATORS

TEST_LOCATOR = 'test'
HOME_PAGE = "https://magento.softwaretestingboard.com/"
TRANING_PAGE = "https://magento.softwaretestingboard.com/training.html"
TRANING_MENU = (By.XPATH, "//a[@id='ui-id-7']/span[last()]")
TRANING_TEXT = (By.CSS_SELECTOR, "#page-title-heading span")
SHOP_BY_TEXT = (By.CSS_SELECTOR, "div[class='title'] strong")
VIDEO_DOWNLOAD = (By.CSS_SELECTOR, "li[class='item'] a")
COMPARE_PRODUCTS_TEXT = (By.CSS_SELECTOR, "#block-compare-heading")
MY_WISH_LIST_TEXT = (By.CSS_SELECTOR, "div[class='block block-wishlist'] strong[role='heading']")
BLOCK1 = (By.XPATH, "//a[@class='block-promo training-main']")
BLOCK1_TEXT = (By.CSS_SELECTOR, "a[class='block-promo training-main'] span[class='content']")
BLOCK1_IMG = (By.CSS_SELECTOR, "a[class='block-promo training-main'] img")