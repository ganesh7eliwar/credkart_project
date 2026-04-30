"""Empty Cart and Wishlist Page Object Module."""

from selenium.webdriver.common.by import By
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class EmptyCartOrWishlist:
    """Page Object for emptying cart and wishlist functionality."""

    empty_cart_xpath = "//input[contains(@value,'Empty Cart')]"
    empty_wishlist_xpath = "//input[contains(@value,'Empty Wishlist')]"
    cart_cleared_confirmation_xpath = "//div[contains(text(),'Your cart has been cleared!')]"
    wishlist_cleared_confirmation_xpath = "//div[contains(text(),'Your wishlist has been cleared!')]"

    def __init__(self, driver):
        """Initialize with WebDriver instance."""
        self.driver = driver

    def empty_cart_button(self):
        """Clicks the Empty Cart button."""
        empty_cart_btn = self.driver.find_element(By.XPATH, self.empty_cart_xpath)
        empty_cart_btn.click()

    def empty_wishlist_button(self):
        """Clicks the Empty Wishlist button."""
        empty_wishlist_btn = self.driver.find_element(By.XPATH, self.empty_wishlist_xpath)
        empty_wishlist_btn.click()

    def cart_empty_confirmation(self):
        """Returns the cart cleared confirmation message."""
        confirmation_text = self.driver.find_element(By.XPATH, self.cart_cleared_confirmation_xpath).text
        return confirmation_text

    def wishlist_empty_confirmation(self):
        """Returns the wishlist cleared confirmation message."""
        confirmation_text = self.driver.find_element(By.XPATH, self.wishlist_cleared_confirmation_xpath).text
        return confirmation_text

    def empty_cart_screenshot_on_pass(self):
        """Captures confirmation screenshot when cart successfully emptied."""
        confirmation_txt = self.driver.find_element(By.XPATH, self.cart_cleared_confirmation_xpath)
        confirmation_txt.screenshot(f'./screenshots/Test_Empty_Cart_Pass_{now}.png')

    def empty_cart_screenshot_on_fail(self):
        """Captures full page screenshot on cart empty failure."""
        self.driver.save_screenshot(f'./screenshots/Test_Empty_Cart_Fail_{now}.png')

    def empty_wishlist_screenshot_on_pass(self):
        """Captures confirmation screenshot when wishlist successfully emptied."""
        confirmation_txt = self.driver.find_element(By.XPATH, self.wishlist_cleared_confirmation_xpath)
        confirmation_txt.screenshot(f'./screenshots/Test_Empty_Wishlist_Pass_{now}.png')

    def empty_wishlist_screenshot_on_fail(self):
        """Captures full page screenshot on wishlist empty failure."""
        self.driver.save_screenshot(f'./screenshots/Test_Empty_Wishlist_Fail_{now}.png')
