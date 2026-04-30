from page_objects.add_item_to_cart import AddItemInCart
from page_objects.add_item_to_wishlist import AddItemToWishlist
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCWishlist
import allure, json, pytest


class TestAddItemToWishlist:
    """
    Test class for wishlist functionality of the CredKart application.

    This class contains test methods to verify adding items to the user wishlist,
    including login, item selection, wishlist addition, and success verification.

    Test Flow:
    1. Login with existing user credentials
    2. Navigate to products and select an item
    3. Add item to wishlist
    4. Verify successful addition via confirmation message
    5. Logout

    Dependencies:
    - Valid user data in test_data/user_details.json
    - AddItemInCart, AddItemToWishlist, and LoginPage page object classes
    - Logger utility for detailed test execution logs
    """
    log = Loggen.log_generator()
    confirmation_text = RCWishlist.confirmation_text()

    @allure.epic('Credkart Project')
    @allure.feature('Add Item.')
    @allure.story('Add Item to Wishlist.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    # @allure.tag('smoke')
    @allure.link('https://automation.credence.in/shop', 'Wishlist')
    @allure.title('CredKart')
    @allure.description('This Test Case adds new Item into the Wishlist.')
    @pytest.mark.order(8)
    def test_add_item_to_wishlist(self, setup, data_dir):
        """
        Test adding an item to the user wishlist.

        This test verifies the wishlist functionality by adding a product to
        the user's wishlist and confirming the successful addition.

        Steps:
        1. Read user credentials from JSON file
        2. Login to the application
        3. Select a product from the catalog
        4. Add the selected item to wishlist
        5. Verify success through confirmation message
        6. Logout

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if item successfully added to wishlist (confirmation message appears)
            False if addition fails or confirmation not received

        Notes:
            - Assumes at least one product is available in the catalog
            - Uses configured confirmation text for verification
            - Wishlist persists across sessions for logged-in users
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

        self.aiw = AddItemToWishlist(self.driver)
        self.aiw.add_item_to_wishlist_button()
        self.log.info('Item was Added to Wishlist.')

        if self.confirmation_text == self.aiw.confirmation_text():
            self.log.info('Entered info If block.')
            self.log.info('Item Added Wishlist Successfully.')
            self.aiw.screenshot_on_pass()
            self.log.info('Captured Screenshot.')
            self.aiw.allure_pass()
            self.lp.logout_dd_button()
            self.log.info('Clicked on Logout Dropdown Button.')
            self.lp.logout_button()
            self.log.info('Clicked on Logout Button.')
            self.log.info('Test "Add Item To Wishlist" Passed.')
            assert True

        else:
            self.log.info('Entered into Else Block.')
            self.aiw.screenshot_on_fail()
            self.log.info('Captured Screenshot.')
            self.aiw.allure_fail()
            self.log.info('Test "Add Item To Wishlist" Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
