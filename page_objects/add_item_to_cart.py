"""
Add Item to Cart Page Object Module

Encapsulates cart management interactions including item selection, 
cart operations, and confirmation verification.
"""

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from datetime import datetime
import allure
import random

now = datetime.now().strftime('%d%m%Y%H%M%S')


class AddItemInCart:
    """Page Object for Add Item to Cart functionality."""

    # Product listing and cart element selectors
    item_list_xpath = "//div[@class='caption text-center']/a/h3"  # Product names
    add_to_cart_xpath = "//input[@value='Add to Cart']"  # Add to cart button
    product_in_cart_xpath = "//tr/td[2]/a"  # Items in cart
    continue_shopping_xpath = "//a[@class='btn btn-primary btn-lg']"  # Continue shopping button
    cnf_text_xpath = "//div[@class='alert alert-success']"  # Success confirmation message
    cart_partial_link_text = "Cart"  # Cart navigation link

    def __init__(self, driver):
        """Initialize with WebDriver instance."""
        self.driver = driver

    def select_item(self):
        """Randomly selects a product from the product list."""
        item_list = self.driver.find_elements(By.XPATH, self.item_list_xpath)
        random.choice(item_list).click()

    def cart_button(self):
        """Clicks the Cart navigation link."""
        cart_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.cart_partial_link_text)
        cart_btn.click()

    def add_to_cart_button(self):
        """Clicks the Add to Cart button on product detail page."""
        add_to_cart_button = self.driver.find_element(By.XPATH, self.add_to_cart_xpath)
        add_to_cart_button.click()

    def continue_shopping_button(self):
        """Clicks Continue Shopping button to return to product listing."""
        con_shop_btn = self.driver.find_element(By.XPATH, self.continue_shopping_xpath)
        con_shop_btn.click()

    def confirmation_text(self):
        """
        Retrieves the success confirmation message after adding item to cart.
        
        Returns:
            str: Confirmation message (e.g., 'Item was added to your cart!')
        """
        cnf_text = self.driver.find_element(By.XPATH, self.cnf_text_xpath).text
        return cnf_text

    def screenshot_on_pass(self):
        """Captures confirmation message screenshot on successful add."""
        cnf_text = self.driver.find_element(By.XPATH, self.cnf_text_xpath)
        cnf_text.screenshot(f'./screenshots/Test_Add_Item_To_Cart_Pass_{now}.png')

    def screenshot_on_fail(self):
        """Captures full page screenshot on failed add to cart."""
        self.driver.save_screenshot(f'./screenshots/Test_Add_Item_To_Cart_Fail_{now}.png')

    def allure_pass(self):
        """Attaches screenshot to Allure report on pass."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Add_Item_To_Cart_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        """Attaches screenshot to Allure report on fail."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Add_Item_To_Cart_fail_{now}',
                      attachment_type=AttachmentType.PNG)
