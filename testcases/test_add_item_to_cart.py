from page_objects.add_item_to_cart import AddItemInCart
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCAddItem
import allure, json, pytest


class TestAddItemToCart:
    """
    Test class for shopping cart functionality of the CredKart application.

    This class contains test methods to verify adding items to the shopping cart,
    including login, item selection, cart addition, and success verification.

    Test Flow:
    1. Login with existing user credentials
    2. Navigate to products and select an item
    3. Add item to shopping cart
    4. Verify successful addition via confirmation message
    5. Continue shopping and logout

    Dependencies:
    - Valid user data in test_data/user_details.json
    - AddItemInCart and LoginPage page object classes
    - Logger utility for detailed test execution logs
    """
    log = Loggen.log_generator()
    confirmation_text = RCAddItem.confirmation_text()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('Shopping Cart Management')
    @allure.story('Add Single Item to Shopping Cart')
    @allure.title('Add Item to Cart - Single Product Addition with Confirmation')
    @allure.description('Verifies ability to add products to shopping cart. Tests complete flow: '
                        'user login, product selection, add to cart, and confirmation message verification.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'normal')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('regression', 'cart-management', 'shopping', 'critical-path', 'product-addition')
    @allure.link('https://automation.credence.in/shop', 'Shopping Cart Page')
    @pytest.mark.order(5)
    @pytest.mark.regression
    @pytest.mark.cart_management
    @pytest.mark.shopping
    @pytest.mark.product_management
    @pytest.mark.critical
    def test_add_item_to_cart(self, setup, data_dir):
        """
        Test adding an item to the shopping cart.

        This test verifies the complete flow of adding a product to the cart,
        including user authentication, product selection, and confirmation.

        Steps:
        1. Read user credentials from JSON file
        2. Login to the application
        3. Select a product from the catalog
        4. Add the selected item to cart
        5. Verify success through confirmation message
        6. Continue shopping and logout

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if item successfully added to cart (confirmation message appears)
            False if addition fails or confirmation not received

        Notes:
            - Assumes at least one product is available in the catalog
            - Uses configured confirmation text for verification
            - Captures screenshots on pass/fail for reporting
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

        # Step 1: Login with registered user
        with allure.step("Login to the application"):
            self.lp.login()
            self.log.info('Clicked on Login Button Link and navigate to Login Page.')
            self.lp.user_email(self.email)
            self.log.info(f'Entered Name in Name Text Box. --> {self.email}')
            self.lp.user_password(self.password)
            self.log.info(f'Entered Password in Password Text Box. --> {self.password}')
            self.lp.login_button()
            self.log.info('Clicked on Login Button.')

        # Step 2: Select and add item to cart
        self.ai = AddItemInCart(self.driver)
        with allure.step("Select product from catalog"):
            self.ai.select_item()
            self.log.info('Item Selected.')

        with allure.step("Add selected item to shopping cart"):
            self.ai.add_to_cart_button()
            self.log.info('Item Added To Cart.')

        # Step 3: Verify cart addition
        if self.confirmation_text in self.ai.confirmation_text():
            with allure.step("Verify item successfully added to cart"):
                self.log.info('Entered info If block.')
                self.log.info('Item Added Successfully.')
                self.ai.screenshot_on_pass()
                self.log.info('Captured Screenshot.')
                self.ai.allure_pass()

            # Step 4: Cleanup - continue shopping and logout
            with allure.step("Continue shopping and logout"):
                self.ai.continue_shopping_button()
                self.log.info('Clicked on Continue Shopping Button.')
                self.lp.logout_dd_button()
                self.log.info('Clicked on Logout Dropdown Button.')
                self.lp.logout_button()
                self.log.info('Clicked on Logout Button.')
                self.log.info('Test "Add Item To Cart" Passed.')

            assert True

        else:
            with allure.step("Verify item addition failure"):
                self.log.info('Entered into Else Block.')
                self.ai.screenshot_on_fail()
                self.log.info('Captured Screenshot.')
                self.ai.allure_fail()
                self.log.info('Test "Add Item To Cart" Failed.')

            assert False

        self.log.info('========== Test Session Finished. ==========')
