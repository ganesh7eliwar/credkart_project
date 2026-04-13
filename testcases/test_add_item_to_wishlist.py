from page_objects.add_item_to_cart import AddItemInCart
from page_objects.add_item_to_wishlist import AddItemToWishlist
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage, RCWishlist
import allure, pytest


class TestAddItemToWishlist:
    log = Loggen.log_generator()
    email = RCLoginPage.email()
    password = RCLoginPage.password()
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
    @pytest.mark.order(6)
    def test_add_item_to_wishlist(self, setup):

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
