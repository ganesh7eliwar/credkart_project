from page_objects.add_item_to_cart import AddItemInCart
from page_objects.checkout import Checkout
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage, RCBillingShippingAddress, RCPayment, RCCardNumber, RCOrderPlaced
import random
import allure

class TestEndToEnd:
    log = Loggen.log_generator()
    email = RCLoginPage.email()
    password = RCLoginPage.password()
    first_name = RCBillingShippingAddress.first_name()
    last_name = RCBillingShippingAddress.last_name()
    phone = RCBillingShippingAddress.phone()
    address = RCBillingShippingAddress.address()
    zip_code = RCBillingShippingAddress.zip_code()
    owner = RCPayment.owner()
    cvv = RCPayment.cvv()
    card_number = RCCardNumber.card_number()
    confirmation_message = RCOrderPlaced.confirmation_msg()

    @allure.epic('Credkart Project')
    @allure.feature('End to End')
    @allure.story('End to End Test from Login to Checkout.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    # @allure.tag('smoke')
    @allure.link('https://automation.credence.in/shop', 'End to End')
    @allure.title('CredKart')
    @allure.description('This Test case is End to End Testcase that includes login into the WebSite and Checkout.')
    def test_end_to_end(self, setup):
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
                f'Both Expected Subtotal: {self.co.expected_subtotal()} and Actual Subtotal: {self.co.actual_subtotal()} are Equal.')

            if self.co.expected_grand_total() == self.co.actual_grand_total():
                self.log.info('Entered info Second If block.')
                self.log.info(
                    f'Both Expected Grand Total: {self.co.expected_grand_total()} and Actual Grand Total: {self.co.actual_grand_total()} are Equal.')
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
