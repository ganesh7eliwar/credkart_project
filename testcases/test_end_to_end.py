from page_objects.add_item_to_cart import AddItemInCart
from page_objects.checkout import Checkout
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCBillingShippingAddress, RCPayment, RCCardNumber, RCOrderPlaced
import allure, json, pytest, random


class TestEndToEnd:
    """
    Test class for end-to-end e-commerce workflow of the CredKart application.

    This class contains comprehensive test methods that simulate a complete
    customer journey from login through checkout and order confirmation.
    It validates the entire shopping flow including cart management,
    billing details, and payment processing.

    Test Flow:
    1. Login with existing user credentials
    2. Add random number of items to cart
    3. Verify cart calculations (subtotal, grand total)
    4. Proceed to checkout with billing/shipping details
    5. Complete payment with card details
    6. Verify order confirmation and success message

    Dependencies:
    - Valid user data in test_data/user_details.json
    - Multiple page object classes (LoginPage, AddItemInCart, Checkout)
    - Configuration utilities for test data (addresses, payment details)
    - Logger utility for detailed test execution logs
    """
    log = Loggen.log_generator()
    phone = RCBillingShippingAddress.phone()
    address = RCBillingShippingAddress.address()
    zip_code = RCBillingShippingAddress.zip_code()
    cvv = RCPayment.cvv()
    card_number = RCCardNumber.card_number()
    confirmation_message = RCOrderPlaced.confirmation_msg()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('Complete Purchase Flow')
    @allure.story('End-to-End Purchase Journey from Login to Order Confirmation')
    @allure.title('End-to-End Purchase - Complete Customer Journey')
    @allure.description('Comprehensive end-to-end test validating the complete purchase flow: '
                        'user authentication, product discovery, cart management, checkout, '
                        'billing information entry, payment processing, and order confirmation.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'normal')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('regression', 'e2e', 'integration', 'user-journey', 'purchase-flow', 'critical-path',
                'checkout', 'payment', 'order-placement')
    @allure.link('https://automation.credence.in/shop', 'Complete Application')
    @pytest.mark.order(4)
    @pytest.mark.regression
    @pytest.mark.integration
    @pytest.mark.e2e
    @pytest.mark.user_journey
    @pytest.mark.purchase_flow
    @pytest.mark.checkout
    @pytest.mark.payment
    @pytest.mark.critical
    def test_end_to_end(self, setup, data_dir):
        """
        Test complete end-to-end e-commerce workflow.

        This test simulates a full customer purchase journey:
        1. Login with registered user credentials
        2. Add 3-5 random items to shopping cart
        3. Navigate to cart and verify subtotal/grand total calculations
        4. Proceed to checkout and fill billing/shipping information
        5. Enter payment details (card number, CVV, expiry)
        6. Complete purchase and verify order confirmation

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if entire flow completes successfully with order confirmation
            False if any step fails (calculations, payment, confirmation)

        Notes:
            - Uses random number of items (3-5) for varied test scenarios
            - Validates both subtotal and grand total calculations
            - Captures order number upon successful completion
        """

        with open(data_dir / "user_details.json", "r") as f:
            user_details = json.load(f)
            parts = user_details["name"].split()
            self.email = user_details["email"]
            self.password = user_details["password"]
            self.owner = user_details["name"]
            self.first_name = parts[0]
            self.last_name = parts[1]

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
        self.iteration_no = 0

        for product in range(1, random.randint(3, 5)):
            self.iteration_no += 1
            self.log.info(f'Interation No: {self.iteration_no}')
            self.ai.select_item()
            self.log.info('Item Selected.')
            self.ai.add_to_cart_button()
            self.log.info('Item Added To Cart.')
            self.ai.continue_shopping_button()
            self.log.info('Clicked on Continue Shopping Button.')

        self.ai.cart_button()
        self.log.info('Clicked on Cart Button.')

        self.co = Checkout(self.driver)
        if self.co.expected_subtotal() == self.co.actual_subtotal():
            self.log.info('Entered info First If block.')
            self.log.info(
                f'Both Expected Subtotal: {self.co.expected_subtotal()} '
                f'and Actual Subtotal: {self.co.actual_subtotal()} are Equal.')

            if self.co.expected_grand_total() == self.co.actual_grand_total():
                self.log.info('Entered info Second If block.')
                self.log.info(
                    f'Both Expected Grand Total: {self.co.expected_grand_total()} '
                    f'and Actual Grand Total: {self.co.actual_grand_total()} are Equal.')
                self.co.proceed_to_checkout_button()
                self.log.info('Clicked on Proceed to Checkout Button.')
                self.co.first_name(self.first_name)
                self.log.info(f'Entered First Name. --> {self.first_name}')
                self.co.last_name(self.last_name)
                self.log.info(f'Entered Last Name. --> {self.last_name}')
                self.co.phone(self.phone)
                self.log.info(f'Entered Phone Number. --> {self.phone}')
                self.co.address(self.address)
                self.log.info(f'Entered Address. --> {self.address}')
                self.co.zip_code(self.zip_code)
                self.log.info(f'Entered Zip Code. --> {self.zip_code}')
                self.co.city()
                self.log.info('Entered City Name.')
                self.co.owner(self.owner)
                self.log.info(f'Entered Owner Details. --> {self.owner}')
                self.co.cvv(self.cvv)
                self.co.card_number(self.card_number)
                self.log.info(f'Entered Card Number. --> {self.card_number}')
                self.co.expiry_year()
                self.log.info('Entered Expiry Year.')
                self.co.expiry_month()
                self.log.info('Entered Expiry Month.')
                self.co.continue_to_checkout_button()
                self.log.info('Clicked on Continue to Checkout Button.')

                if self.confirmation_message == self.co.confirmation_message():
                    self.log.info('Entered info Third If block.')
                    self.log.info(f'Order Placed Successfully, Order Number is: "{self.co.order_number()}".')
                    self.co.screenshot_on_pass()
                    self.log.info('Captured Screenshot.')
                    self.co.allure_pass()
                    self.lp.logout_dd_button()
                    self.log.info('Clicked on Logout Dropdown Button.')
                    self.lp.logout_button()
                    self.log.info('Clicked on Logout Button.')
                    self.log.info('Test "End To End" Passed.')
                    assert True

                else:
                    self.log.info('Entered into Else Block.')
                    self.co.screenshot_on_fail()
                    self.log.info('Captured Screenshot.')
                    self.co.allure_fail()
                    self.log.info('Test "End To End" Failed.')
                    assert False

        self.log.info('========== Test Session Finished. ==========')
