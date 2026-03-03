from selenium.webdriver.common.by import By
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class EmptyCartOrWishlist:
    empty_cart_xpath = "//input[contains(@value,'Empty Cart')]"
    empty_wishlist_xpath = "//input[contains(@value,'Empty Wishlist')]"
    cart_cleared_confirmation_xpath = "//div[contains(text(),'Your cart has been cleared!')]"
    wishlist_cleared_confirmation_xpath = "//div[contains(text(),'Your wishlist has been cleared!')]"

    def __init__(self, driver):
        self.driver = driver

    def empty_cart_button(self):
        empty_cart_btn = self.driver.find_element(By.XPATH, self.empty_cart_xpath)
        empty_cart_btn.click()

    def empty_wishlist_button(self):
        empty_wishlist_btn = self.driver.find_element(By.XPATH, self.empty_wishlist_xpath)
        empty_wishlist_btn.click()

    def cart_empty_confirmation(self):
        confirmation_text = self.driver.find_element(By.XPATH, self.cart_cleared_confirmation_xpath).text
        return confirmation_text

    def wishlist_empty_confirmation(self):
        confirmation_text = self.driver.find_element(By.XPATH, self.wishlist_cleared_confirmation_xpath).text
        return confirmation_text

    def empty_cart_screenshot_on_pass(self):
        confirmation_txt = self.driver.find_element(By.XPATH, self.cart_cleared_confirmation_xpath)
        confirmation_txt.screenshot(f'./screenshots/Test_Empty_Cart_Pass_{now}.png')

    def empty_cart_screenshot_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_Empty_Cart_Fail_{now}.png')

    def empty_wishlist_screenshot_on_pass(self):
        confirmation_txt = self.driver.find_element(By.XPATH, self.wishlist_cleared_confirmation_xpath)
        confirmation_txt.screenshot(f'./screenshots/Test_Empty_Wishlist_Pass_{now}.png')

    def empty_wishlist_screenshot_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_Empty_Wishlist_Fail_{now}.png')
