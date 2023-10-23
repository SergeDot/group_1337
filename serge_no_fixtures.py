from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
import time



CORRECT_USER_ID = 'standard_user'
CORRECT_USER_PASS = 'secret_sauce'
INCORRECT_USER_ID = 'standard_user1'
INCORRECT_USER_PASS = 'standard_user1'
URL = 'https://www.saucedemo.com/'

user_name_input_textbox = '#user-name'
user_pass_input_textbox = '#password'
login_button = '#login-button'
inventory_container = '#contents_wrapper > #inventory_container'
error_locator = 'h3'
error_message = 'Epic sadface: Username and password do not match any user in this service'
add_button_elements = '.btn_inventory'
item_link = '//button[@id="{id}"]/ancestor::div[@class="inventory_item"]//div[@class="inventory_item_label"]//a'
shopping_cart_link = '.shopping_cart_link'
shopping_cart_items = '.cart_list .cart_item'

def test_login_form_correct_data():
    driver = webdriver.Chrome()
    driver.get(URL)
# login
    username_field = driver.find_element(By.CSS_SELECTOR, user_name_input_textbox)
    username_field.send_keys(CORRECT_USER_ID)
    password_field = driver.find_element(By.CSS_SELECTOR, user_pass_input_textbox)
    password_field.send_keys(CORRECT_USER_PASS)
    login_button_element = driver.find_element(By.CSS_SELECTOR, login_button)
    login_button_element.click()
#inventory_container
    inventory = driver.find_element(By.CSS_SELECTOR, inventory_container)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert inventory.is_displayed()
    driver.quit()

def test_login_form_incorrect_data():
    driver = webdriver.Chrome()
    driver.get(URL)
# login
    username_field = driver.find_element(By.CSS_SELECTOR, user_name_input_textbox)
    username_field.send_keys(INCORRECT_USER_ID)
    password_field = driver.find_element(By.CSS_SELECTOR, user_pass_input_textbox)
    password_field.send_keys(INCORRECT_USER_PASS)
    login_button_element = driver.find_element(By.CSS_SELECTOR, login_button)
    login_button_element.click()

    error_message_element = driver.find_element(By.CSS_SELECTOR, error_locator)
    inventory_locator = driver.find_elements(By.CSS_SELECTOR, inventory_container)  # checking if inventory_cntainer is present

    assert len(inventory_locator) == 0
    assert error_message_element.is_displayed()
    assert error_message_element.text == error_message

    driver.quit()

def test_add_item_catalogue_verify_button_text_changed():
    driver = webdriver.Chrome()
    driver.get(URL)

    username_field = driver.find_element(By.CSS_SELECTOR, user_name_input_textbox)
    username_field.send_keys(CORRECT_USER_ID)
    password_field = driver.find_element(By.CSS_SELECTOR, user_pass_input_textbox)
    password_field.send_keys(CORRECT_USER_PASS)
    login_button_element = driver.find_element(By.CSS_SELECTOR, login_button)
    login_button_element.click()

    add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, add_button_elements)  #getting all 'Add to Cart' buttons
    add_to_cart_random_element = add_to_cart_buttons[randint(0, len(add_to_cart_buttons) - 1)]  # selecting a random button
    random_element_id = add_to_cart_random_element.get_attribute('id')  #getting id of a random button
    random_element_item_name = driver.find_element(By.XPATH, item_link.format(id = random_element_id)).text  #getting the item name that belongs to the random button
    print(random_element_item_name)
    add_to_cart_random_element.click()

# getting the button that belongs to the added item
    new_cart_button_text = driver\
        .find_element(By.LINK_TEXT, random_element_item_name)\
        .find_element(By.XPATH,'ancestor::div[@class="inventory_item_description"]//button').text
    assert new_cart_button_text == 'Remove'  # verifying the button text changed

    driver.find_element(By.CSS_SELECTOR, shopping_cart_link).click()
    shopping_cart_items_list = driver.find_elements(By.CSS_SELECTOR, shopping_cart_items)  # getting a list of the shopping cart items
    assert len(shopping_cart_items_list) == 1

    found_added_item = 0
    for item in shopping_cart_items_list:  #looping through the shopping cart items
        found_added_item += item.find_element(By.CSS_SELECTOR, 'a').text == random_element_item_name
    print(found_added_item)
    assert found_added_item  # verifying the added item is within the list of SC items

    driver.quit()