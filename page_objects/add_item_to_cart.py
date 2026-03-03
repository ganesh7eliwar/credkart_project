from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from datetime import datetime
import allure
import random

now = datetime.now().strftime('%d%m%Y%H%M%S')


class AddItemInCart:
    item_list_xpath = "//div[@class='caption text-center']/a/h3"
    add_to_cart_xpath = "//input[@value='Add to Cart']"
    product_in_cart_xpath = "//tr/td[2]/a"
    continue_shopping_xpath = "//a[@class='btn btn-primary btn-lg']"
    cnf_text_xpath = "//div[@class='alert alert-success']"
    cart_partial_link_text = "Cart"

    def __init__(self, driver):
        self.driver = driver

    def select_item(self):
        item_list = self.driver.find_elements(By.XPATH, self.item_list_xpath)
        random.choice(item_list).click()

    def cart_button(self):
        cart_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.cart_partial_link_text)
        cart_btn.click()

    def add_to_cart_button(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, self.add_to_cart_xpath)
        add_to_cart_button.click()

    def continue_shopping_button(self):
        con_shop_btn = self.driver.find_element(By.XPATH, self.continue_shopping_xpath)
        con_shop_btn.click()

    def confirmation_text(self):
        cnf_text = self.driver.find_element(By.XPATH, self.cnf_text_xpath).text

        return cnf_text

    def screenshot_on_pass(self):
        cnf_text = self.driver.find_element(By.XPATH, self.cnf_text_xpath)
        cnf_text.screenshot(f'./screenshots/Test_Add_Item_To_Cart_Pass_{now}.png')

    def screenshot_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_Add_Item_To_Cart_Fail_{now}.png')

    def allure_pass(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Add_Item_To_Cart_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Add_Item_To_Cart_fail_{now}',
                      attachment_type=AttachmentType.PNG)
