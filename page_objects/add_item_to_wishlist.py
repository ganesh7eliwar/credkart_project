from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from datetime import datetime
import allure

now = datetime.now().strftime('%d%m%Y%H%M%S')


class AddItemToWishlist:
    add_to_wishlist_xpath = "//input[contains(@value,'Add to Wishlist')]"
    confirmation_txt_xpath = "//div[@class='alert alert-success']"
    wishlist_button_partial_link_text = "Wishlist"

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_wishlist_button(self):
        add_to_wishlist = self.driver.find_element(By.XPATH, self.add_to_wishlist_xpath)
        add_to_wishlist.click()

    def confirmation_text(self):
        confirmation_txt = self.driver.find_element(By.XPATH, self.confirmation_txt_xpath).text
        return confirmation_txt

    def wishlist_button(self):
        wishlist_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.wishlist_button_partial_link_text)
        wishlist_btn.click()

    def screenshot_on_pass(self):
        cnf_text = self.driver.find_element(By.XPATH, self.confirmation_txt_xpath)
        cnf_text.screenshot(f'./screenshots/Test_Add_Item_To_Wishlist_Pass_{now}.png')

    def screenshot_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_Add_Item_To_Wishlist_Fail_{now}.png')

    def allure_pass(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Add_Item_To_Wishlist_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Add_Item_To_Wishlist_Fail_{now}',
                      attachment_type=AttachmentType.PNG)
