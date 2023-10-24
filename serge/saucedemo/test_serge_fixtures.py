from selenium.webdriver.common.by import By
from random import randint
from serge.saucedemo.data import URL, CORRECT_USER_ID, CORRECT_USER_PASS
import serge.saucedemo.saucedemo_locators as locators


def test_add_item_catalogue_verify_button_text_changed(driver):
    driver.get(URL)

    driver.find_element(By.CSS_SELECTOR, locators.user_name_input_textbox).send_keys(CORRECT_USER_ID)
    driver.find_element(By.CSS_SELECTOR, locators.user_pass_input_textbox).send_keys(CORRECT_USER_PASS)
    driver.find_element(By.CSS_SELECTOR, locators.login_button).click()

    add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, locators.add_button_elements)  #getting all 'Add to Cart' buttons
    add_to_cart_random_element = add_to_cart_buttons[randint(0, len(add_to_cart_buttons) - 1)]  # selecting a random button
    random_element_id = add_to_cart_random_element.get_attribute('id')  #getting id of a random button
    random_element_item_name = driver.find_element(By.XPATH, locators.item_link.format(id = random_element_id)).text  #getting the item name that belongs to the random button
    print(random_element_item_name)
    add_to_cart_random_element.click()

# getting the button that belongs to the added item
    new_cart_button_text = driver\
        .find_element(By.LINK_TEXT, random_element_item_name)\
        .find_element(By.XPATH,'ancestor::div[@class="inventory_item_description"]//button').text
    assert new_cart_button_text == 'Remove'  # verifying the button text changed

    driver.find_element(By.CSS_SELECTOR, locators.shopping_cart_link).click()
    shopping_cart_items_list = driver.find_elements(By.CSS_SELECTOR, locators.shopping_cart_items)  # getting a list of the shopping cart items
    assert len(shopping_cart_items_list) == 1

    found_added_item = 0
    for item in shopping_cart_items_list:  #looping through the shopping cart items
        found_added_item += item.find_element(By.CSS_SELECTOR, 'a').text == random_element_item_name
    print(found_added_item)
    assert found_added_item  # verifying the added item is within the list of SC items