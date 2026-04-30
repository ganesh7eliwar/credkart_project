from page_objects.add_item_to_cart import AddItemInCart
from page_objects.empty_cart_wishlist import EmptyCartOrWishlist
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCEmptyCartWishlist
import allure, json, pytest


class TestEmptyCart:
    """
    Test class for emptying shopping cart functionality of the CredKart application.

    This class contains test methods to verify removing all items from the shopping cart,
    including adding items first, then emptying the cart, and verifying the empty state.

    Test Flow:
    1. Login with existing user credentials
    2. Add an item to the cart (prerequisite)
    3. Navigate to cart and click empty cart
    4. Verify cart is empty via confirmation message
    5. Logout

    Dependencies:
    - Valid user data in test_data/user_details.json
    - AddItemInCart, EmptyCartOrWishlist, and LoginPage page object classes
    - Logger utility for detailed test execution logs
    """
    log = Loggen.log_generator()
    confirmation_text = RCEmptyCartWishlist.empty_cart_confirmation()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('Shopping Cart Management')
    @allure.story('Empty Shopping Cart - Remove All Items')
    @allure.title('Empty Shopping Cart - Bulk Item Removal Functionality')
    @allure.description('Verifies the empty cart functionality by adding a product, then removing all items. '
                        'Validates cart state transitions and confirmation of empty cart status.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'normal')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('regression', 'cart-management', 'shopping', 'cleanup', 'state-management')
    @allure.link('https://automation.credence.in/shop', 'Shopping Cart Page')
    @pytest.mark.order(6)
    @pytest.mark.regression
    @pytest.mark.cart_management
    @pytest.mark.shopping
    @pytest.mark.cleanup
    def test_empty_cart(self, setup, data_dir):
        """
        Test emptying all items from the shopping cart.

        This test verifies the cart emptying functionality by first adding an item
        to the cart, then removing all items and confirming the cart is empty.

        Steps:
        1. Read user credentials from JSON file
        2. Login to the application
        3. Add an item to cart (to have something to empty)
        4. Click the empty cart button
        5. Verify cart is empty through confirmation message
        6. Logout

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if cart successfully emptied (confirmation message matches)
            False if emptying fails or confirmation not received

        Notes:
            - Requires adding an item first to test the empty functionality
            - Uses configured confirmation text for verification
            - Tests the complete cart management workflow
        """

        with open(data_dir / "user_details.json", "r") as f:
            user_details = json.load(f)
            self.email = user_details["email"]
            self.password = user_details["password"]

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.lp.login()
        self.log.info('Clicked on Login Button Link and navigate to Login Page.')
        self.lp.user_email(self.email)
        self.log.info(f'Entered Name in Name Text Box. --> {self.email}')
        self.lp.user_password(self.password)
        self.log.info(f'Entered Password in Password Text Box. --> {self.password}')
        self.lp.login_button()
        self.log.info('Clicked on Login Button.')

        self.ai = AddItemInCart(self.driver)
        self.ai.select_item()
        self.log.info('Item Selected.')
        self.ai.add_to_cart_button()
        self.log.info('Item Added To Cart.')

        self.ec = EmptyCartOrWishlist(self.driver)
        self.ec.empty_cart_button()
        self.log.info('Clicked on Empty Cart Button.')

        if self.confirmation_text == self.ec.cart_empty_confirmation():
            self.log.info('Entered info If block.')
            self.log.info('Item Removed From Cart Successfully.')
            self.ec.empty_cart_screenshot_on_pass()
            self.log.info('Captured Screenshot.')
            self.lp.allure_pass()
            self.lp.logout_dd_button()
            self.log.info('Clicked on Logout Dropdown Button.')
            self.lp.logout_button()
            self.log.info('Clicked on Logout Button.')
            self.log.info('Test "Test Empty Cart" Passed.')
            assert True

        else:
            self.log.info('Entered into Else Block.')
            self.ec.empty_cart_screenshot_on_fail()
            self.log.info('Captured Screenshot.')
            self.lp.allure_fail()
            self.log.info('Test "Test Empty Cart" Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
