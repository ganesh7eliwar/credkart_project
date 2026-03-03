import random, allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class Checkout:
    price_list_xpath = "//tbody/tr/td[4]"
    proceed_to_checkout_partial_link_text = "Proceed to Checkout"
    first_name_id = 'first_name'
    last_name_id = 'last_name'
    phone_id = 'phone'
    address_id = 'address'
    zip_id = 'zip'
    state_xpath = "//select[@id='state']"
    owner_id = 'owner'
    cvv_id = 'cvv'
    card_number_id = 'cardNumber'
    expiry_year_xpath = "//select[@id='exp_year']"
    expiry_month_xpath = "//select[@id='exp_month']"
    continue_to_checkout_id = 'confirm-purchase'
    confirmation_message_xpath = "//p[@class='lead w-lg-50 mx-auto']"
    order_placed_screenshot_xpath = "//div[@class='container text-center']"
    order_number_xpath = "//div/p/a[@href='#']"

    def __init__(self, driver):
        self.driver = driver

    def expected_subtotal(self):
        price_of_products = [price.text for price in self.driver.find_elements(By.XPATH, self.price_list_xpath)]
        exp_subtotal = 0

        for item in price_of_products[:-3]:
            original_price = item.replace('$', '')
            price = float(original_price)
            exp_subtotal += price

        return round(exp_subtotal, 2)

    def actual_subtotal(self):
        price_of_products = [price.text for price in self.driver.find_elements(By.XPATH, self.price_list_xpath)]
        act_subtotal = price_of_products[-3]
        x = act_subtotal.replace('$', '')
        actual_sub_total = x.replace(',', '')

        return round(float(actual_sub_total), 2)

    def expected_grand_total(self):
        exp_grand_total = self.expected_subtotal() + (self.expected_subtotal() * .13)

        return round(exp_grand_total, 2)

    def actual_grand_total(self):
        price_of_products = [price.text for price in self.driver.find_elements(By.XPATH, self.price_list_xpath)]
        final_total = price_of_products[-1]
        x = final_total.replace('$', '')
        actual_grand_total = x.replace(',', '')

        return round(float(actual_grand_total), 2)

    def proceed_to_checkout_button(self):
        proceed_to_checkout_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                                           self.proceed_to_checkout_partial_link_text)
        proceed_to_checkout_btn.click()

    def first_name(self, f_name):
        first_name_txt_box = self.driver.find_element(By.ID, self.first_name_id)
        first_name_txt_box.send_keys(f_name)

    def last_name(self, l_name):
        last_name_txt_box = self.driver.find_element(By.ID, self.last_name_id)
        last_name_txt_box.send_keys(l_name)

    def phone(self, phone_number):
        phone_text_box = self.driver.find_element(By.ID, self.phone_id)
        phone_text_box.send_keys(phone_number)

    def address(self, address):
        address_text_box = self.driver.find_element(By.ID, self.address_id)
        address_text_box.send_keys(address)

    def zip_code(self, zip_code):
        zip_text_box = self.driver.find_element(By.ID, self.zip_id)
        zip_text_box.send_keys(zip_code)

    def city(self):
        select_city = Select(self.driver.find_element(By.XPATH, self.state_xpath))
        select_city.select_by_index(random.randint(1, 5))

    def owner(self, owner_name):
        owner_name_txt_box = self.driver.find_element(By.ID, self.owner_id)
        owner_name_txt_box.send_keys(owner_name)

    def cvv(self, cvv_number):
        cvv_text_box = self.driver.find_element(By.ID, self.cvv_id)
        cvv_text_box.send_keys(cvv_number)

    def card_number(self, card_details):

        for part in card_details:
            card_number_details = self.driver.find_element(By.ID, self.card_number_id)
            card_number_details.send_keys(part)

    def expiry_year(self):
        exp_year = Select(self.driver.find_element(By.XPATH, self.expiry_year_xpath))
        exp_year.select_by_index(random.randint(4, 6))

    def expiry_month(self):
        exp_month = Select(self.driver.find_element(By.XPATH, self.expiry_month_xpath))
        exp_month.select_by_index(random.randint(1, 12))

    def continue_to_checkout_button(self):
        continue_to_co_btn = self.driver.find_element(By.ID, self.continue_to_checkout_id)
        continue_to_co_btn.click()

    def confirmation_message(self):
        confirmation_msg = self.driver.find_element(By.XPATH, self.confirmation_message_xpath).text
        return confirmation_msg

    def order_number(self):
        order_no = self.driver.find_element(By.XPATH, self.order_number_xpath).text
        return order_no

    def screenshot_on_pass(self):
        order_placed_screenshot = self.driver.find_element(By.XPATH, self.order_placed_screenshot_xpath)
        order_placed_screenshot.screenshot(f'./screenshots/Test_End_To_End_Pass_{now}.png')

    def screenshot_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_End_To_End_Fail_{now}.png')

    def allure_pass(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_End_To_End_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_End_To_End_Fail_{now}',
                      attachment_type=AttachmentType.PNG)
