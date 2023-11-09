from locators import *
from selenium.webdriver.support import expected_conditions as EC

def test_TC_010_001_001_open_Traning_page(driver, wait):
    driver.get(HOME_PAGE)
    traning_button = wait.until(EC.element_to_be_clickable(TRANING_MENU))
    traning_button.click()
    assert driver.current_url == "https://magento.softwaretestingboard.com/training.html"


# Verify that the text on the left side is displayed
def test_TC_010_001_002_text_is_displayed(driver, wait):
    driver.get(TRANING_PAGE)
    training_text = wait.until(EC.visibility_of_element_located(TRANING_TEXT))
    shop_by_text = wait.until(EC.visibility_of_element_located(SHOP_BY_TEXT))
    video_download_text = wait.until(EC.visibility_of_element_located(VIDEO_DOWNLOAD))
    compare_products_text = wait.until(EC.visibility_of_element_located(COMPARE_PRODUCTS_TEXT))
    my_wish_list_text = wait.until(EC.visibility_of_element_located(MY_WISH_LIST_TEXT))
    assert training_text.is_displayed(), "Training text is not displayed"
    assert shop_by_text.is_displayed(), "Shop By text is not displayed"
    assert video_download_text.is_displayed(), "Video Download text is not displayed"
    assert compare_products_text.is_displayed(), "Compare Products text is not displayed"
    assert my_wish_list_text.is_displayed(), "My Wish List text is not displayed"


# Verify Video Download is clickable
def test_TC_010_003_001_Video_Download_is_clickable(driver, wait):
    driver.get(TRANING_PAGE)
    video_download_link = wait.until(EC.element_to_be_clickable(VIDEO_DOWNLOAD))
    assert video_download_link.is_displayed(), "Video Download link is not clickable"


# Redirection to the Video Download page
def test_TC_010_003_002_redirect_to_video_download_page(driver, wait):
    driver.get(TRANING_PAGE)
    video_download_link = wait.until(EC.element_to_be_clickable(VIDEO_DOWNLOAD))
    video_download_link.click()
    assert driver.current_url == "https://magento.softwaretestingboard.com/training/training-video.html"


# Verify Block 1 is displayed
def test_TC_010_004_001_Block1_is_displayed(driver, wait):
    driver.get(TRANING_PAGE)
    block1 = wait.until(EC.presence_of_element_located(BLOCK1))
    assert block1.is_displayed(), "Block1 is not displayed"


# Verify Block 1 consists text
def test_TC_010_004_002_Block1_text_is_displayed(driver, wait):
    driver.get(TRANING_PAGE)
    block1_list = wait.until(EC.presence_of_all_elements_located(BLOCK1_TEXT))
    assert 'Motivate yourself.\nReach goals.\nBoost ambition.\nMax fitness.\nUpgrade lifestyle.' in block1_list[0].text


# Verify the size of Block 1
def test_TC_010_004_003_Block1_size_is_correct(driver, wait):
    driver.get(TRANING_PAGE)
    block1_img = wait.until(EC.presence_of_element_located(BLOCK1_IMG))
    assert block1_img.size['height'] == 372 and block1_img.size['width'] == 1280, "Block1 height and width is not correct"
