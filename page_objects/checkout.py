"""
Checkout Page Object Module

Encapsulates the entire checkout flow including cart validation,
billing/shipping address entry, payment processing, and order confirmation.

This is the most complex page object due to multi-step form interactions,
price calculations, dropdown selections, and order validation.
"""

import random, allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class Checkout:
    """
    Page Object for the checkout process.
    
    Handles:
    - Cart total validation (subtotal, tax, grand total)
    - Billing and shipping address entry
    - Payment information entry
    - Order submission and confirmation
    """

    # ========================= PRICE/TOTAL ELEMENTS =========================
    price_list_xpath = "//tbody/tr/td[4]"  # All price cells in cart items table

    # ========================= CART NAVIGATION =========================
    proceed_to_checkout_partial_link_text = "Proceed to Checkout"

    # ========================= BILLING FORM FIELDS =========================
    first_name_id = 'first_name'
    last_name_id = 'last_name'
    phone_id = 'phone'
    address_id = 'address'
    zip_id = 'zip'
    state_xpath = "//select[@id='state']"  # State/city dropdown

    # ========================= PAYMENT FORM FIELDS =========================
    owner_id = 'owner'  # Cardholder name
    cvv_id = 'cvv'
    card_number_id = 'cardNumber'
    expiry_year_xpath = "//select[@id='exp_year']"
    expiry_month_xpath = "//select[@id='exp_month']"
    continue_to_checkout_id = 'confirm-purchase'  # Order submission button

    # ========================= ORDER CONFIRMATION ELEMENTS =========================
    confirmation_message_xpath = "//p[@class='lead w-lg-50 mx-auto']"
    order_placed_screenshot_xpath = "//div[@class='container text-center']"
    order_number_xpath = "//div/p/a[@href='#']"

    def __init__(self, driver):
        """Initialize with WebDriver instance."""
        self.driver = driver

    # ========================= PRICE CALCULATION METHODS =========================

    def expected_subtotal(self):
        """
        Calculates expected subtotal by summing individual item prices.
        
        Returns:
            float: Sum of all item prices (excluding subtotal/tax/total rows)
        """
        price_of_products = [price.text for price in self.driver.find_elements(By.XPATH, self.price_list_xpath)]
        exp_subtotal = 0

        # Sum all prices except last 3 rows (subtotal, tax, grand total)
        for item in price_of_products[:-3]:
            original_price = item.replace('$', '')
            price = float(original_price)
            exp_subtotal += price

        return round(exp_subtotal, 2)

    def actual_subtotal(self):
        """
        Retrieves the subtotal displayed on the page.
        
        Returns:
            float: Subtotal shown in the cart summary
        """
        price_of_products = [price.text for price in self.driver.find_elements(By.XPATH, self.price_list_xpath)]
        act_subtotal = price_of_products[-3]
        x = act_subtotal.replace('$', '')
        actual_sub_total = x.replace(',', '')

        return round(float(actual_sub_total), 2)

    def expected_grand_total(self):
        """
        Calculates expected grand total with 13% tax applied.
        Formula: subtotal + (subtotal * 0.13)
        
        Returns:
            float: Expected total including tax
        """
        exp_grand_total = self.expected_subtotal() + (self.expected_subtotal() * .13)

        return round(exp_grand_total, 2)

    def actual_grand_total(self):
        """
        Retrieves the grand total displayed on the page.
        
        Returns:
            float: Grand total shown after tax calculation
        """
        price_of_products = [price.text for price in self.driver.find_elements(By.XPATH, self.price_list_xpath)]
        final_total = price_of_products[-1]
        x = final_total.replace('$', '')
        actual_grand_total = x.replace(',', '')

        return round(float(actual_grand_total), 2)

    # ========================= CHECKOUT FLOW METHODS =========================

    def proceed_to_checkout_button(self):
        """Clicks Proceed to Checkout button, navigating to billing form."""
        proceed_to_checkout_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                                           self.proceed_to_checkout_partial_link_text)
        proceed_to_checkout_btn.click()

    # ========================= BILLING ADDRESS METHODS =========================

    def first_name(self, f_name):
        """Enters first name in billing form."""
        first_name_txt_box = self.driver.find_element(By.ID, self.first_name_id)
        first_name_txt_box.send_keys(f_name)

    def last_name(self, l_name):
        """Enters last name in billing form."""
        last_name_txt_box = self.driver.find_element(By.ID, self.last_name_id)
        last_name_txt_box.send_keys(l_name)

    def phone(self, phone_number):
        """Enters phone number in billing form."""
        phone_text_box = self.driver.find_element(By.ID, self.phone_id)
        phone_text_box.send_keys(phone_number)

    def address(self, address):
        """Enters street address in billing form."""
        address_text_box = self.driver.find_element(By.ID, self.address_id)
        address_text_box.send_keys(address)

    def zip_code(self, zip_code):
        """Enters postal/zip code in billing form."""
        zip_text_box = self.driver.find_element(By.ID, self.zip_id)
        zip_text_box.send_keys(zip_code)

    def city(self):
        """Randomly selects a state/city from dropdown."""
        select_city = Select(self.driver.find_element(By.XPATH, self.state_xpath))
        select_city.select_by_index(random.randint(1, 5))

    # ========================= PAYMENT METHODS =========================

    def owner(self, owner_name):
        """Enters cardholder name."""
        owner_name_txt_box = self.driver.find_element(By.ID, self.owner_id)
        owner_name_txt_box.send_keys(owner_name)

    def cvv(self, cvv_number):
        """Enters CVV (Card Verification Value)."""
        cvv_text_box = self.driver.find_element(By.ID, self.cvv_id)
        cvv_text_box.send_keys(cvv_number)

    def card_number(self, card_details):
        """
        Enters card number in parts (for PCI compliance).
        
        Args:
            card_details (list): List of card number parts [part1, part2, part3, part4]
        """
        for part in card_details:
            card_number_details = self.driver.find_element(By.ID, self.card_number_id)
            card_number_details.send_keys(part)

    def expiry_year(self):
        """Randomly selects expiry year from dropdown."""
        exp_year = Select(self.driver.find_element(By.XPATH, self.expiry_year_xpath))
        exp_year.select_by_index(random.randint(4, 6))

    def expiry_month(self):
        """Randomly selects expiry month from dropdown."""
        exp_month = Select(self.driver.find_element(By.XPATH, self.expiry_month_xpath))
        exp_month.select_by_index(random.randint(1, 12))

    # ========================= ORDER SUBMISSION =========================

    def continue_to_checkout_button(self):
        """Clicks the Confirm Purchase button to submit order."""
        continue_to_co_btn = self.driver.find_element(By.ID, self.continue_to_checkout_id)
        continue_to_co_btn.click()

    # ========================= ORDER CONFIRMATION METHODS =========================

    def confirmation_message(self):
        """
        Retrieves the order confirmation message.
        
        Returns:
            str: Confirmation text displayed after successful order placement
        """
        confirmation_msg = self.driver.find_element(By.XPATH, self.confirmation_message_xpath).text
        return confirmation_msg

    def order_number(self):
        """
        Retrieves the order number from confirmation page.
        
        Returns:
            str: Unique order number/ID
        """
        order_no = self.driver.find_element(By.XPATH, self.order_number_xpath).text
        return order_no

    # ========================= SCREENSHOT CAPTURE METHODS =========================

    def screenshot_on_pass(self):
        """Captures confirmation page screenshot on successful order."""
        order_placed_screenshot = self.driver.find_element(By.XPATH, self.order_placed_screenshot_xpath)
        order_placed_screenshot.screenshot(f'./screenshots/Test_End_To_End_Pass_{now}.png')

    def screenshot_on_fail(self):
        """Captures full page screenshot on checkout failure."""
        self.driver.save_screenshot(f'./screenshots/Test_End_To_End_Fail_{now}.png')

    # ========================= ALLURE REPORTING METHODS =========================

    def allure_pass(self):
        """Attaches confirmation screenshot to Allure report on pass."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_End_To_End_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        """Attaches failure screenshot to Allure report on fail."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_End_To_End_Fail_{now}',
                      attachment_type=AttachmentType.PNG)
