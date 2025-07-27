from page_objects.add_item_to_cart import AddItemInCart
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage, RCAddItem


class TestAddItemToCart:
    log = Loggen.log_generator()
    email = RCLoginPage.email()
    password = RCLoginPage.password()
    name = RCLoginPage.name()
    confirmation_text = RCAddItem.confirmation_text()

    def test_add_item_to_cart(self, setup):

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

        if self.confirmation_text in self.ai.confirmation_text():
            self.log.info('Entered info If block.')
            self.log.info('Item Added Successfully.')
            self.ai.ss_on_pass()
            self.log.info('Captured Screenshot.')
            self.ai.continue_shopping_button()
            self.log.info('Clicked on Continue Shopping Button.')
            self.lp.logout_dd_button()
            self.log.info('Clicked on Logout Dropdown Button.')
            self.lp.logout_button()
            self.log.info('Clicked on Logout Button.')
            self.log.info('Test "Add Item To Cart" Passed.')
            assert True

        else:
            self.log.info('Entered into Else Block.')
            self.ai.ss_on_fail()
            self.log.info('Captured Screenshot.')
            self.log.info('Test "Add Item To Cart" Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
