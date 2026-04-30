from page_objects.add_item_to_cart import AddItemInCart
from page_objects.add_item_to_wishlist import AddItemToWishlist
from page_objects.empty_cart_wishlist import EmptyCartOrWishlist
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCEmptyCartWishlist
import allure, json, pytest


class TestEmptyWishlist:
    """
    Test class for emptying wishlist functionality of the CredKart application.

    This class contains test methods to verify removing all items from the user's wishlist,
    including adding items first, then emptying the wishlist, and verifying the empty state.

    Test Flow:
    1. Login with existing user credentials
    2. Add an item to the wishlist (prerequisite)
    3. Navigate to wishlist and click empty wishlist
    4. Verify wishlist is empty via confirmation message
    5. Logout

    Dependencies:
    - Valid user data in test_data/user_details.json
    - AddItemInCart, AddItemToWishlist, EmptyCartOrWishlist, and LoginPage page object classes
    - Logger utility for detailed test execution logs
    """
    log = Loggen.log_generator()
    confirmation_text = RCEmptyCartWishlist.empty_wishlist_confirmation()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('Wishlist Management')
    @allure.story('Empty Wishlist - Remove All Saved Items')
    @allure.title('Empty Wishlist - Bulk Item Removal from Saved Items')
    @allure.description('Verifies the empty wishlist functionality by adding a product to wishlist, '
                        'then removing all items. Validates wishlist state transitions and confirmation.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'normal')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('regression', 'wishlist-management', 'shopping', 'cleanup', 'state-management')
    @allure.link('https://automation.credence.in/shop', 'Wishlist Page')
    @pytest.mark.order(7)
    @pytest.mark.regression
    @pytest.mark.wishlist_management
    @pytest.mark.shopping
    @pytest.mark.cleanup
    def test_empty_wishlist(self, setup, data_dir):
        """
        Test emptying all items from the user's wishlist.

        This test verifies the wishlist emptying functionality by first adding an item
        to the wishlist, then removing all items and confirming the wishlist is empty.

        Steps:
        1. Read user credentials from JSON file
        2. Login to the application
        3. Select a product from the catalog
        4. Add the selected item to wishlist
        5. Navigate to wishlist page
        6. Click the empty wishlist button to remove all items
        7. Verify wishlist is empty through confirmation message
        8. Logout

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if wishlist successfully emptied (confirmation message matches)
            False if emptying fails or confirmation not received

        Notes:
            - Requires adding an item to wishlist first to test the empty functionality
            - Uses configured confirmation text for verification
            - Tests the complete wishlist management workflow
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

        # Step 1: Login to application with registered user credentials
        self.lp.login()
        self.log.info('Clicked on Login Button Link and navigate to Login Page.')
        self.lp.user_email(self.email)
        self.log.info(f'Entered Name in Name Text Box. --> {self.email}')
        self.lp.user_password(self.password)
        self.log.info(f'Entered Password in Password Text Box. --> {self.password}')
        self.lp.login_button()
        self.log.info('Clicked on Login Button.')

        # Step 2: Select an item from catalog
        self.ai = AddItemInCart(self.driver)
        self.ai.select_item()
        self.log.info('Item Selected.')

        # Step 3: Add selected item to wishlist
        self.aiw = AddItemToWishlist(self.driver)
        self.aiw.add_item_to_wishlist_button()
        self.log.info('Item was Added to Wishlist.')

        # Step 4: Navigate to wishlist page
        self.aiw.wishlist_button()
        self.log.info('Clicked on Wishlist Button.')

        # Step 5: Empty the wishlist (remove all items) and verify
        self.ec = EmptyCartOrWishlist(self.driver)
        self.ec.empty_wishlist_button()
        self.log.info('Clicked on Empty Wishlist Button.')

        # Step 6: Verify wishlist is empty by checking confirmation message
        if self.confirmation_text == self.ec.wishlist_empty_confirmation():
            self.log.info('Entered info If block.')
            self.log.info('Item Removed From Wishlist Successfully.')
            self.ec.empty_wishlist_screenshot_on_pass()
            self.log.info('Captured Screenshot.')
            self.lp.allure_pass()

            # Step 7: Logout from application
            self.lp.logout_dd_button()
            self.log.info('Clicked on Logout Dropdown Button.')
            self.lp.logout_button()
            self.log.info('Clicked on Logout Button.')
            self.log.info('Test "Test Empty Wishlist" Passed.')
            assert True

        else:
            self.log.info('Entered into Else Block.')
            self.ec.empty_wishlist_screenshot_on_fail()
            self.log.info('Captured Screenshot.')
            self.lp.allure_fail()
            self.log.info('Test "Test Empty Wishlist" Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
